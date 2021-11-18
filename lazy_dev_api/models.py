from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=128)
    online = models.BooleanField()
    collection = ArrayField(models.IntegerField(), null=True, blank=True)

class Guide(models.Model):
    name = models.CharField(max_length=32)
    author_id = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    likes = models.IntegerField()
    content = models.CharField(max_length=1024)
    image = models.ImageField(upload_to='images', blank=True)
    rating = models.IntegerField()
