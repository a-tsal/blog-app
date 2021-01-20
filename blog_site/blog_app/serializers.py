from rest_framework import serializers
from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(source='get_articels', many=True)

    class Meta:
        model = Blog
        fields = "__all__"
