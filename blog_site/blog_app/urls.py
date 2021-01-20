
from django.urls import path
from .views import *

urlpatterns = [

    path('', UserLogin.as_view(), name='login')
]