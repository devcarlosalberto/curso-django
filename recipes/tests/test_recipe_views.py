from unittest import skip

from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):

    # views.home
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_status_code_is_200(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_load_correct_template(self):
        template = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(template, 'recipes/pages/home.html')
    
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        # Delete all recipes in database for check template if no found recipes
        self.delete_recipes()  # RecipeTestBase.delete_recipes()

        response = self.client.get(reverse('recipes:home'))
        self.assertIn('No recipes found here', response.content.decode('utf-8'))

    def test_recipe_home_view_load_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        response_recipe = response.context['recipes'].first()
        self.assertEqual(response_recipe.title, 'Recipe Title')


    # views.recipe
    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_status_code_is_200(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_load_correct_template(self):
        template = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertTemplateUsed(template, 'recipes/pages/recipe-view.html')

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)


    # views.category
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)
    
    def test_recipe_category_view_status_code_is_200(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_recipe_category_view_load_correct_template(self):
        template = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertTemplateUsed(template, 'recipes/pages/category.html')

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)
