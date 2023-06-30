from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .serializers import PostSerializer , UserSerializer
from .permissions import IsAuthorOrReadOnly

from .models import Post


# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
#class PostDetail(generics.RetrieveUpdateDestroyAPIView):
 #   permission_classes = (IsAuthorOrReadOnly , )
  #  queryset = Post.objects.all()
   # serializer_class = PostSerializer
    
    
    
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
    
    
#class UserDetail (generics.RetrieveUpdateDestroyAPIView):
 #   queryset = get_user_model().objects.all()
  #  serializer_class = UserSerializer