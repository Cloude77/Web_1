from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Главная</h1>")


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(requests):
    return HttpResponse("<h3>Контакты</h3>")


def products(requests, productid = 1):
    output = "<h2>Продукт № {0}</h2>".format(productid)
    return HttpResponse(output)


def users(requests, id, name):
    output = "<h2>Пользователь</h2><h3>id: {0} Имя: {1}</h3>".format(id, name)
    return HttpResponse(output)
