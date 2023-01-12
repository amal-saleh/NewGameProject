from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path ('rules/', views.about, name='rules'),
    path ('about/', views.about, name='about'),
    path ('questions/', views.about, name='questions'),
    path ('achievements/', views.about, name='achievements'),
]