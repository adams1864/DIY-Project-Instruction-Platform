from rest_framework import generics
from .models import DIYProject, Category, Tag
from .serializers import DIYProjectSerializer, CategorySerializer, TagSerializer

# DIY Projects
class DIYProjectListCreate(generics.ListCreateAPIView):
    queryset = DIYProject.objects.all()
    serializer_class = DIYProjectSerializer

class DIYProjectDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = DIYProject.objects.all()
    serializer_class = DIYProjectSerializer

# Categories
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Tags
class TagListCreate(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
