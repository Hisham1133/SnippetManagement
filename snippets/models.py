from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SnipetNotes(models.Model):
    body = models.TextField(blank=True)

    def __str__(self):
        return self.body[0:10]


class Tag(models.Model):
    tag_name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.tag_name


class Snipets(models.Model):
    snippet_title = models.CharField(max_length=120)
    snippet_body = models.ForeignKey(SnipetNotes,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    tag = models.OneToOneField(Tag,on_delete=models.CASCADE,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.snippet_title






