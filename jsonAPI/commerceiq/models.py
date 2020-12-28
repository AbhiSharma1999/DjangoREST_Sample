from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    posts = models.IntegerField(default=0)


class Post(models.Model):
    author = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    reviews = models.IntegerField(default = 0)
    views = models.IntegerField(default = 0)

    def __str__(self):
        return self.title
