from django.urls import path
from .views import post_list

app_name = 'forum'

urlpatterns = [
   #list all the posts 
   path('', post_list, name='list'),
]