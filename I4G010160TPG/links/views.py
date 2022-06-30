from pyexpat import model
from venv import create
from django import views
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ( ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView)
from links.models import Link
from links.serializers import LinkSerializer

# Create your views here.
class PostListApi(ListAPIView):
    model = Link
    queryset = Link.objects.filter(active=True)
serializer_class = LinkSerializer

class PostCreateApi(CreateAPIView):
    model = Link
    queryset = Link.objects.filter(active=True)
serializer_class = LinkSerializer

class PostDetailApi(RetrieveAPIView):
    model = Link
    queryset = Link.objects.filter(active=True)
serializer_class = LinkSerializer

class PostUpdateApi(UpdateAPIView):
    model = Link
queryset = Link.objects.filter(active=True)
serializer_class = LinkSerializer

class PostDeleteApi(DestroyAPIView):
    model = Link
queryset= Link.objects.filter(active=True)
serializer_class = LinkSerializer
