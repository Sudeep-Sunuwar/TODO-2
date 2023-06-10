from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, 'core/base.html')

def app_home(request):
    return render (request, 'app_pages/home.html')

def add(request):
    return render (request,'app_pages/add.html')