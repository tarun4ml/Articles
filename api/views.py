from rest_framework import generics, permissions
from api import serializers
from api.models import Articles
from django.contrib.auth.models import User
from api.permissions import IsOwnerOrReadOnly


class Userlist(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class Userdetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class Articlelist(generics.ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = serializers.ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class Articledetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = serializers.ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]