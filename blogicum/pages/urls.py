# pages/urls.py
from django.urls import path
from .views import about_view, rules_view

app_name = 'pages'

urlpatterns = [
    path('about/', about_view, name='about'),
    path('rules/', rules_view, name='rules'),
    path('', about_view, name='index'),
]
