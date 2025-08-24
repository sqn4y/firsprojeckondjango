from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Главная страница</h1>')

def about(request):
    return HttpResponse('<h1>О нас</h1>')

def shop(request):
    return HttpResponse('<h1>Наши товары</h1>')