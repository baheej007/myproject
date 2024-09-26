from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # The empty path will now map to the home view
    path('search/', views.search_by_hashtag, name='search_by_hashtag'),  # Search URL
]
