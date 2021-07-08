from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Articles

class UserSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'articles']

class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Articles
        fields = ['id', 'title', 'body', 'owner', 'view']

class ArticleByUserView(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ['id', 'title', 'body', 'view', 'owner']