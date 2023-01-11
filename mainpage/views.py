from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse('Hello World, muna test')
    return render(request, 'mainpage/index.html')


def about(request):
    #return HttpResponse('Hello World, muna test')
    return render(request, 'mainpage/rules.html')

def about(request):
    #return HttpResponse('Hello World, muna test')
    return render(request, 'mainpage/about.html')


def about(request):
    #return HttpResponse('Hello World, muna test')
    return render(request, 'mainpage/questions.html')

def about(request):
    #return HttpResponse('Hello World, muna test')
    return render(request, 'mainpage/achievements.html')