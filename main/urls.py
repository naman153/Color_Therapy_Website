from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path("", views.index, name='home'),
    path("admin1/", views.admin1, name='admin1'),
    path("Add_Category/", views.feedback, name='feedback'),
    path("Add_Image/", views.add_image, name='Add_Images'),
    path("Contact/", views.contact, name='Contact'),
    path("Category/<slug:slug>", views.category, name='Category'),


]