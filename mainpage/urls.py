from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path ('rules/', views.rules, name='rules'),
    path ('about/', views.about, name='about'),
    path ('questions/', views.questions, name='questions'),
    path ('achievements/', views.achievements, name='achievements'),
    #these two links should be written in other page for all user page links.
    path ('sign-in/', views.sign_in, name='signin'),
    path ('sign-up/', views.sign_up, name='signup'),
]