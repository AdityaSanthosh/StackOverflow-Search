from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('search_result', views.SearchUser, name='search_result'),
    path('', views.SearchQuery, name='search_query'),
]
