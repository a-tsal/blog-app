from django.urls import path
from . import views

urlpatterns = [

    path('', views.writers_list, name='writers'),
    path('/detail/<str:pk>/',  views.writer_details, name='detail'),
    path('/create', views.writer_create, name='create'),
    path('/update/<str:pk>/',  views.writer_update, name='update'),
    path('/delete/<str:pk>/',  views.writer_delete, name='delete')
]