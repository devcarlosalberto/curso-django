from django.shortcuts import get_list_or_404, get_object_or_404, render

from recipes.models import Recipe


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'title': 'Página Inicial',
        'recipes': Recipe.objects.filter(
            is_publish=True
        ).order_by('-id'),
    })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_publish=True
        )
    )

    return render(request, 'recipes/pages/category.html', context={
        'title': recipes[0].category.name,
        'recipes': recipes
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id, is_publish=True)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'title': 'Receitas',
        'recipe': recipe,
        'is_detail_page': True,
    })
