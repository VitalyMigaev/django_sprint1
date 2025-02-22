from django.urls import path
from .views import index, about, rules, detail, category

app_name = 'pages'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('rules/', rules, name='rules'),
    path('detail/', detail, name='detail'),
    path('category/', category, name='category'),
]
