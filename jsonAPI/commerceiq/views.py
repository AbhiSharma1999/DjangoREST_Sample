from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.

class Posts_API(APIView):
    serializers_classes = serializers.Post_Serializer

    def get(self , request):
        posts = models.Post.objects.all()
        
        params = request.query_params
        title = params.get('title',None)
        author = params.get('author',None)
        idparam = params.get('id',None)
        postsparams = params.get('posts',None)
        q = params.get('q',None)
        sort = params.get('_sort',None)
        order = params.get('_order',None)

        if title is not None : 
            posts=posts.filter(title=title)
        if author is not None :
            posts=posts.filter(author=author)
        if idparam is not None :
            posts=posts.filter(id=idparam)
        if q is not None :
            posts = posts.filter(title=q)
        if sort is not None :
            if order is "dsc" :
                posts = posts.order_by(f'{sort}')
            else :
                posts = posts.order_by(f'-{sort}')

        serializer = self.serializers_classes(posts , many = True)

        return Response(serializer.data , status = status.HTTP_200_OK)

    def post(self , request):
        serializer_data = request.data
        serializer = self.serializers_classes(models.Post.objects.create() , data = serializer_data , partial=False)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data , status = status.HTTP_200_OK)



class Authors_API(APIView):
    serializers_classes = serializers.Author_Serializer

    def post(self , request):
        serializer_data = request.data
        serializer = self.serializers_classes(models.Author.objects.create() , data = serializer_data , partial=False)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data , status = status.HTTP_200_OK)

    def get(self , request):
        authors = models.Author.objects.all()
        
        serializer = self.serializers_classes(authors , many = True)

        return Response(serializer.data , status = status.HTTP_200_OK)


class Authors_ID(APIView) :
    serializers_classes = serializers.Author_Serializer


    def get(self , request , pk):
        try:
            authors = models.Author.objects.get(id=pk)
        except Authors.DoesNotExist :
            raise Http404
        
        serializer = self.serializers_classes(authors)

        return Response(serializer.data , status = status.HTTP_200_OK)

    def delete(self,request,pk):
        try:
            authors = models.Author.objects.get(id=pk)
        except Authors.DoesNotExist :
            raise Http404

        authors.delete()
        return Response(status = status.HTTP_200_OK)

    def put(self,request,pk):
        try:
            authors = models.Author.objects.get(id=pk)
        except Authors.DoesNotExist :
            raise Http404

        serializer_data = request.data
        serializer = self.serializers_classes(authors , data = serializer_data , partial=False)
        serializer.is_valid(raise_exception = True)
        serializer.save()  
        return Response(serializer.data , status = status.HTTP_200_OK)
        