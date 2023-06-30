from django.shortcuts import render
from rest_framework import generics

from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

from .models import Post


# Create your views here.


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly , )
    queryset = Post.objects.all()
    serializer_class = PostSerializer