from django.shortcuts import render
from utils.recipes.factory import make_recipe

from recipes.models import Category, Recipe


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'title': 'Página Inicial',
        'recipes': [recipe for recipe in Recipe.objects.filter(
            is_publish=True
        ).order_by('-id')],
    })


def category(request, category_id):
    return render(request, 'recipes/pages/category.html', context={
        'title': f'Categoria de {Category.objects.filter(id=category_id).first().name}',
        'recipes': [recipe for recipe in Recipe.objects.filter(
            category__id=category_id,
            is_publish=True
        ).order_by('-id')]
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'title': 'Receitas',
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
