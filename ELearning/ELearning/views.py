from django.shortcuts import render
from http.server import HTTPServer

from . import models


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request,  'about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        ins = models.contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("Save in Database")
    return render(request, 'contact.html')

def java(request):
    return render(request,  'java.html')

def python(request):
    return render(request,  'python.html')

