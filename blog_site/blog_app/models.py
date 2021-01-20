from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Writer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=False)


class Article(models.Model):
    title = models.CharField(max_length=30, null=False)
    writer = models.ForeignKey(Writer, on_delete=models.SET_NULL, null=True)


class Blog(models.Model):
    title = models.CharField(max_length=30, null=False)
    article = models.ManyToManyField(Article)

    def get_articels(self):
        return Article.objects.filter(blog=self)
