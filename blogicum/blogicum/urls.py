"""blogicum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# blogicum/urls.py

# blogicum/urls.py

from django.contrib import admin
from django.urls import path, include
from pages.views import index, about, rules, detail, category

from django.contrib import admin
from django.urls import path, include
from pages.views import index, about, rules, detail, category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', index, name='index'),
    path('pages/index.html', index, name='index_html'),
    path('pages/about/', about, name='about'),
    path('pages/about.html', about, name='about_html'),
    path('pages/rules/', rules, name='rules'),
    path('pages/rules.html', rules, name='rules_html'),
    path('pages/detail/', detail, name='detail'),
    path('pages/detail.html', detail, name='detail_html'),
    path('pages/category/', category, name='category'),
    path('pages/category.html', category, name='category_html'),
]
