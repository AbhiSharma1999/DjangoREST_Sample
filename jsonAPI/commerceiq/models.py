from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    posts = models.IntegerField(default=0)
    
    def __str__(self):
        return self.first_name+self.last_name


class Post(models.Model):
    author = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    reviews = models.IntegerField(default = 0)
    views = models.IntegerField(default = 0)

    def __str__(self):
        return self.title
