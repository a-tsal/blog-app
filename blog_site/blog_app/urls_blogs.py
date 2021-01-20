from django.urls import path
from . import views

urlpatterns = [

    path('', views.blogs_list, name='blogs'),
    path('/detail/<str:pk>/', views.blog_details, name='detail'),
    path('/create', views.blog_create, name='create'),
    path('/update/<str:pk>/', views.blog_update, name='update'),
    path('/delete/<str:pk>/', views.blog_delete, name='delete'),
]