from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        # post = Post.objects.get(slug__iexact=slug)  # Получаем объект БД по slug
        obj = get_object_or_404(self.model, slug__iexact=slug)   #Post класс модели, а slug__iexact=slug это то что ищем
        return render(request, self.template, context={self.model.__name__.lower(): obj})