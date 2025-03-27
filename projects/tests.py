from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework import status
from .models import DIYProject, Category, Tag
from .serializers import DIYProjectSerializer, CategorySerializer, TagSerializer

class DIYProjectTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.category = Category.objects.create(name='Woodworking')
        self.tag1 = Tag.objects.create(name='Beginner')
        self.tag2 = Tag.objects.create(name='Easy')
        self.project1 = DIYProject.objects.create(
            title='Simple Shelf',
            description='A basic shelf project',
            category=self.category,
            instructions="test instructions" #added this line
        )
        self.project1.tags.add(self.tag1, self.tag2)
        self.project2 = DIYProject.objects.create(
            title='Advanced Table',
            description='A complex table project',
            category=self.category,
            instructions="test instructions" #added this line
        )
        self.project2.tags.add(self.tag2)

    def test_project_list_create(self):
        url = '/api/projects/' #added /api/
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2) #changed this line

        new_project_data = {
            'title': 'New Project',
            'description': 'A brand new project',
            'category': self.category.id,
            'instructions': 'test instructions', #added this line
            'tags': [self.tag1.id]
        }
        response = self.client.post(url, new_project_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DIYProject.objects.count(), 3)

    def test_project_detail_update_delete(self):
        url = f'/api/projects/{self.project1.id}/' #added /api/
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Simple Shelf')

        updated_data = {
            'title': 'Updated Shelf',
            'description': 'An updated shelf project',
            'category': self.category.id,
            'instructions': 'test instructions', #added this line
            'tags': [self.tag2.id]
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(DIYProject.objects.get(id=self.project1.id).title, 'Updated Shelf')

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(DIYProject.objects.count(), 1)

    def test_category_list_create(self):
        url = '/api/categories/' #added /api/
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1) #changed this line

        new_category_data = {'name': 'Electronics'}
        response = self.client.post(url, new_category_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)

    def test_tag_list_create(self):
        url = '/api/tags/' #added /api/
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2) #changed this line

        new_tag_data = {'name': 'Intermediate'}
        response = self.client.post(url, new_tag_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tag.objects.count(), 3)

    def test_unauthenticated_access(self):
        self.client.logout()
        url = '/api/projects/' #added /api/
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK) # or HTTP_403_FORBIDDEN if you want to restrict read access

        response = self.client.post(url, {'title': 'Unauthorized', 'description': 'test', 'category': self.category.id, 'instructions': 'test'}, format='json') #added description and category
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
