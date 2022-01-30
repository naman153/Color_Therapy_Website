from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.base import Model

class Feedback(models.Model):
    name = models.CharField(max_length=50, null=False)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    image = models.ImageField(null=True)
    message= models.CharField(max_length=250, null=True)
	
    @property
    def imageURL(self):
	    try:
		    url = self.image.url
	    except:
		    url = ''
	    return url