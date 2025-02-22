# pages/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def rules(request):
    return render(request, 'rules.html')

def detail(request):
    return render(request, 'detail.html')

def category(request):
    return render(request, 'category.html')

