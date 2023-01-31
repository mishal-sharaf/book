from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Books
from api.serializer import BooksSerializers,BooksModelSerializer
from rest_framework import viewsets

class BookStoreView(APIView):
    def get(self,*args,**kwargs):
        qs=Books.objects.all()
        serializer=BooksSerializers(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=BooksSerializers(data=request.data)
        if serializer.is_valid():
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
class BooksDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get(id="id")
        qs=Books.objects.get(id=id)
        serializer=BooksSerializers(qs,many=False)
        return Response(data=serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Books.objects.filter(id=id).update(**request.data)
        qs=Books.objects.get(id=id)
        serializer=BooksSerializers(qs,many=False)
        return Response(data=serializer.data)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Books.objects.filter(id=id).delete()
        return Response(data="product deleted")

class ProductViewsetView(viewsets.ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Books.objects.all()
        serializer=BooksModelSerializer(qs,many=True)
        return Response(serializer.data)
    def create(self,request,*args,**kwargs):
        serializer=BooksModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        else:
            return Response(serializer.errors)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Books.objects.get(id=id)
        seriealizer=BooksModelSerializer(qs,many=False)
        return Response(data=seriealizer.data)
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Books.objects.get(id=id)
        serializer=BooksModelSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(serializer.errors)
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Books.objects.get(id=id).delete()
        return Response('deleted')
