from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path(
        'category/<slug:category_slug>/',
        views.category_posts,
        name='category'
    ),
]
