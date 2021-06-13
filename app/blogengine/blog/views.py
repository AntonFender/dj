from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})

def post_detail(request, slug): # slug мы ждем от сюда path('post/<str:slug>/'...

    post = Post.objects.get(slug__iexact=slug)  #Получаем объект БД по slug
    return render(request, 'blog/post_detail.html', context={'post': post})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', context={'tag': tag})