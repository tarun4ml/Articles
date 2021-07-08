from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from api import serializers
from api.models import Articles
from django.contrib.auth.models import User
from api.permissions import IsOwnerOrReadOnly
from django.db.models import Sum
import json


class Userlist(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    


class Userdetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
   

class Articlelist(generics.ListCreateAPIView):
    queryset = Articles.objects.all().order_by('-view')
    serializer_class = serializers.ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class Articledetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = serializers.ArticleSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    def get_queryset(self, **kwargs):
        pk = self.kwargs['pk']
        user = self.request.user
        article = Articles.objects.get(id=pk)
        jsonDec = json.decoder.JSONDecoder()
        myViewList = jsonDec.decode(article.viewList)
        if str(user.username) not in myViewList:
            myViewList.append(str(user.username))
            article.viewList = json.dumps(myViewList)
            article.view+=1
            article.save()
        
        return Articles.objects.all()

class ViewArticleByUserView(generics.ListAPIView):
    serializer_class = serializers.ArticleByUserView
    queryset = Articles.objects.all()
    
    def get_queryset(self,**kwargs):
        userid = self.kwargs['pk']
        data = Articles.objects.filter(owner = userid).order_by('-view')
        return data

class UserViewList(APIView):
    def get(self, request, format = None):
        a = Articles.objects.values('owner__username').order_by('owner').annotate(sum= Sum('view')).order_by('-sum')
        return Response({a})