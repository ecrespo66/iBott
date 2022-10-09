from django.db import models
from rest_framework.authtoken.admin import User
from django_editorjs import EditorJsField
# Create your models here.


class Subscriber(models.Model):
    mail = models.EmailField()


class Category(models.Model):
    name = models.CharField(max_length=255)


class Tags(models.Model):
    name = models.CharField(max_length=255)


class Comment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()


class Post(models.Model):
    url = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    excerpt = models.TextField(null=True, blank=True)
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tags, blank=True)
    comments = models.ManyToManyField(Comment, blank=True)
    content = EditorJsField(
            editorjs_config={
                "tools": {
                    "Link": {
                        "config": {
                            "endpoint":
                                '/linkfetching/'
                        }
                    },
                    "Image": {
                        "config": {
                            "endpoints": {
                                "byFile": '/uploadi/',
                                "byUrl": '/uploadi/'
                            },

                        }
                    },
                    "Attaches": {
                        "config": {
                            "endpoint": '/uploadf/'
                        }
                    }
                }
            },
            null=True,
            blank=True)

    def __str__(self):
        return self.title
