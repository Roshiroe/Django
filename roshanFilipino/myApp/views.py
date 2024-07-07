from django.shortcuts import render
from django.urls import path 

# Create your views here.

def home(request):
    return render(request, 'home.html')

def projects(request):
    return render(request, 'projects.html')

def abouts(request):
    return render(request, 'abouts.html')
