from rest_framework import generics, serializers
from .models import DIYProject, Category, Tag
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class DIYProjectSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = DIYProject
        fields = '__all__'

# DIY Projects
class DIYProjectListCreate(generics.ListCreateAPIView):
    queryset = DIYProject.objects.all()
    serializer_class = DIYProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] #add this line

class DIYProjectDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = DIYProject.objects.all()
    serializer_class = DIYProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] #add this line

# Categories
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly] #add this line

# Tags
class TagListCreate(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] #add this line
