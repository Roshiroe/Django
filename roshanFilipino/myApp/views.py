from django.shortcuts import render
from django.urls import path 

# Create your views here.
def helloworld (request) :
    return render(request,"helloworld.html")