from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Женская страница')

def categories(request):
    return HttpResponse('<h1>Стати по категориям</h1>')