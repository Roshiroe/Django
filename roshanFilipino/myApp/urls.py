from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("projects/", views.projects, name='projects'),
    path("abouts/", views.abouts, name='abouts'),
    path("contacts/", views.contacts, name='contacts'),
]