from django.shortcuts import render

def about_view(request):
    return render(request, 'pages/about.html')

def rules_view(request):
    return render(request, 'pages/rules.html')

def index_view(request):
    return render(request, 'pages/index.html')
