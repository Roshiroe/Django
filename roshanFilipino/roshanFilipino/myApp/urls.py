from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
  path("", views.helloworld, name = 'helloworld'),
  path("abouts/", views.abouts, name = 'abouts')
]
