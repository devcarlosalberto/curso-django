from django.http import HttpResponse
from django.shortcuts import render


def home(req):
    return render(req, 'recipes/index.html')


def contato(req):
    return HttpResponse('CONTATO')


def sobre(req):
    return HttpResponse('SOBRE')
