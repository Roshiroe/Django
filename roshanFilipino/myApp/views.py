from django.shortcuts import render
from django.urls import path
from .models import AddBook 

# Create your views here.

def home(request):
    return render(request, 'home.html')

def projects(request):
    return render(request, 'projects.html')

def abouts(request):
    return render(request, 'abouts.html')

def contacts(request):
    if request.method == "POST":
        Full_Name = request.POST['author']
        Email = request.POST['title']
        Give_us_feedback = request.POST['desc']

        new_book = AddBook(author=Full_Name, title=Email, description=Give_us_feedback)
        new_book.save()

    return render(request, 'contacts.html', {})

