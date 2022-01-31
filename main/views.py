from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth import logout
from django.forms.forms import Form
from django.http import JsonResponse, request
import json
import datetime
from .models import * 

def category(request, slug ):
    feeds = Feedback.objects.all()
    i=slug
    ims = Product.objects.filter(name=slug)
    context= {'feeds':feeds, 'ims':ims,'i':i}
    return render(request, 'main\Category.html', context)

def index(request):
    feeds = Feedback.objects.all()
	
    context = {'feeds':feeds}
    return render(request, 'main\main.html', context)

def feedback(request):
    if request.method == "POST":
	    name=request.POST['name']
	    x= Feedback.objects.create(name=name)
	    x.save()
	    return redirect('/')
    return render(request, 'main\Feedback.html')

def admin1(request):
    return render(request, 'main\Admin1.html')

def add_image(request):
    feeds = Feedback.objects.all()
    context = {'feeds':feeds}
    
    if request.method == "POST":
        n=request.POST["name"]
        image=request.POST['images']
        m=request.POST['message']
        x= Product.objects.create(name=n, image =image, message=m)
        x.save()
        return redirect('/')
    
    
    return render(request, 'main\Add_Images.html', context)

def contact(request):
    return render(request, 'main\contact_us.html')
