from django.shortcuts import render
from django.http import HttpResponse

def posts_list(request):
    return HttpResponse('<h1>Привет Мир</h1>')

def posts_list1(request):
    return HttpResponse('<h1>Привет Мир!!!!!!!!!!!</h1>')
