from django.urls import path
from .views import PostListView

app_name = 'forum'

urlpatterns = [
   #list all the posts 
   path('', PostListView.as_view(), name='list'),
]