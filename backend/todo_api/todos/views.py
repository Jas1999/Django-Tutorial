from django.shortcuts import render

# Create your views here. 
from rest_framework import generics

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response  

from .models import Todo
from .serializers import TodoSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

'''
class AddTodo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer

    def post(self,request,*args,**kargs):
        #Todo.objects.create(title='first todo')
        print(request)
        pass
'''