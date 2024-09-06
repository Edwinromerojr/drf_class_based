from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

# Create your views here.
class BlogPostListCreate(generics.ListCreateView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
