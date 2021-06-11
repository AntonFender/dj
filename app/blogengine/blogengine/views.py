from django.http import HttpResponse    #Импортируем библиотеку HttpResponse


def hello(request): #Все функции обработчики принимают обзательный аргумент request
    return HttpResponse('<h1>Hello world</h1>')
