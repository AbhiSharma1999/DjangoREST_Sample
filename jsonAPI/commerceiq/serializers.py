from rest_framework import serializers
from . import models

class Author_Serializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only = True)

    class Meta:
        model = models.Author
        fields = ['id' , 'first_name' , 'last_name' , 'posts']

class Post_Serializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only = True)

    class Meta:
        model = models.Post
        fields = ['id' , 'title' , 'author' , 'views' , 'reviews']
