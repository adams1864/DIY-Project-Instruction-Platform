from django.urls import path
from .views import DIYProjectListCreate, DIYProjectDetailUpdateDelete, CategoryListCreate, TagListCreate
#from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('projects/', DIYProjectListCreate.as_view(), name='projects-list-create'),
    path('projects/<int:pk>/', DIYProjectDetailUpdateDelete.as_view(), name='projects-detail-update-delete'),
    path('categories/', CategoryListCreate.as_view(), name='categories-list-create'),
    path('tags/', TagListCreate.as_view(), name='tags-list-create'),
   # path('api-token-auth/', obtain_jwt_token, name='api-token-auth'),
]
