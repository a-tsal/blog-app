from django.contrib.auth.views import LoginView
from django.shortcuts import render
from rest_framework.response import Response

from .forms import AuthenticationFormCustom
from .models import *
from .serializers import WriterSerializer, BlogSerializer
from rest_framework.decorators import api_view


# Create your views here.
class UserLogin(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationFormCustom

#crud writer


@api_view(['GET'])
def writers_list(request):
    writers = Writer.objects.all()
    serializer = WriterSerializer(writers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def writer_details(request, pk):
    writers = Writer.objects.get(id=pk)
    serializer = WriterSerializer(writers, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def writer_create(request):
    serializer = WriterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def writer_update(request, pk):
    writer = Writer.objects.get(id=pk)
    serializer = WriterSerializer(instance=writer, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def writer_delete(request, pk):
    writer = Writer.objects.get(id=pk)
    writer.delete()
    return Response('Deleted')


# crud blog


@api_view(['GET'])
def blogs_list(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def blog_details(request, pk):
    blogs = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blogs, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def blog_create(request):
    serializer = BlogSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def blog_update(request, pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(instance=blog, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def blog_delete(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    return Response('Deleted')
