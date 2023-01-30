from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse('Hello World, muna test')
    return render(request, 'mainpage/index.html')


def rules(request):
    #return HttpResponse('Hello World, muna test')
    return render(request, 'mainpage/rules.html')

def about(request):
    #return HttpResponse('Hello World, muna test')
    return render(request, 'mainpage/about.html')


def questions(request):
    #return HttpResponse('Hello World, muna test')
    return render(request, 'mainpage/questions.html')

def achievements(request):
    #return HttpResponse('Hello World, muna test')
    return render(request, 'mainpage/achievements.html')

#these two should be written in other page for all user page links.

def sign_in(request):
    #return HttpResponse('Hello World, muna test')
    return render(request, 'pages/sign-in.html')

def sign_up(request):
    #return HttpResponse('Hello World, muna test')
    return render(request, 'pages/sign-up.html')