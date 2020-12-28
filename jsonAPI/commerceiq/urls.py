from django.urls import path 
from . import views


urlpatterns = [
    path('posts', views.Posts_API.as_view() ),
    path('authors', views.Authors_API.as_view() ),
    path('authors/<int:pk>',views.Authors_ID.as_view())
]