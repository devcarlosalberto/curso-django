from django.shortcuts import render


def home(req):
    return render(req, 'recipes/pages/index.html')
