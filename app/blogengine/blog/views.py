from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})

def post_detail(request, slug): # slug мы ждем от сюда path('post/<str:slug>/'...

    post = Post.objects.get(slug__iexact=slug)  #Получаем объект БД по slug
    return render(request, 'blog/post_detail.html', context={'post': post})