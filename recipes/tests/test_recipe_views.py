from re import A
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
    

    def test_recipe_home_view_load_recipes(self):
        need_title = 'This is a home page'

        # Need a recipe for this test
        self.make_recipe(title=need_title)

        response = self.client.get(reverse('recipes:home'))
        self.assertIn(need_title, response.content.decode('utf-8'))


    def test_recipe_home_view_recipes_dont_publish_is_hidden(self):
        need_title = 'This is a recipe test not published in home page'

         # Need a recipe for this test
        self.make_recipe(title=need_title, is_publish=False)
         
        response = self.client.get(reverse('recipes:home'))
        self.assertNotIn(need_title,
                            response.content.decode('utf-8'))


    def test_recipe_home_template_show_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('No recipes found here',
                        response.content.decode('utf-8'))


    # views.recipe
    def test_recipe_detail_view_function_is_correct(self):
        self.make_recipe()  # Make recipe in database
        view = resolve(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id': 1
                }
            )
        )
        self.assertIs(view.func, views.recipe)


    def test_recipe_detail_view_status_code_is_200(self):
        self.make_recipe()  # Make recipe in database
        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id': 1
                }
            )
        )
        self.assertEqual(response.status_code, 200)


    def test_recipe_detail_view_load_correct_template(self):
        self.make_recipe()  # Make recipe in database
        template = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id': 1
                }
            )
        )
        self.assertTemplateUsed(template,
                                'recipes/pages/recipe-view.html')


    def test_recipe_detail_view_load_recipes(self):
        need_title = 'This is a detail page'

        # Need a recipe for this test
        self.make_recipe(title=need_title)

        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id': 1
                }
            )
        )
        self.assertIn(need_title, response.content.decode('utf-8'))


    def test_recipe_detail_view_recipes_dont_publish_is_hidden(self):
        need_title = 'This is a recipe test not \
                        published in detail page'

        # Need a reicipe for this test
        self.make_recipe(title=need_title, is_publish=False)

        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id': 1
                }
            )
        )
        self.assertNotIn(need_title, response.content.decode('utf-8'))


    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id': 1000
                }
            )
        )
        self.assertEqual(response.status_code, 404)


    # views.category
    def test_recipe_category_view_function_is_correct(self):
        self.make_recipe()  # Make recipe in database
        view = resolve(
            reverse(
                'recipes:category',
                kwargs={
                    'category_id': 1
                }
            )
        )
        self.assertIs(view.func, views.category)
    

    def test_recipe_category_view_status_code_is_200(self):
        self.make_recipe()  # Make recipe in database
        response = self.client.get(
            reverse(
                'recipes:category',
                kwargs={'category_id': 1
                }
            )
        )
        self.assertEqual(response.status_code, 200)


    def test_recipe_category_view_load_correct_template(self):
        self.make_recipe()  # Make recipe in database
        template = self.client.get(
            reverse(
                'recipes:category',
                kwargs={
                    'category_id': 1
                }
            )
        )
        self.assertTemplateUsed(template, 'recipes/pages/category.html')


    def test_recipe_category_view_load_recipes(self):
        need_title = 'This is a category page'
        
        # Need a recipe for this test
        self.make_recipe(title=need_title)

        response = self.client.get(
            reverse(
                'recipes:category',
                kwargs={
                    'category_id': 1
                }
            )
        )
        self.assertIn(need_title, response.content.decode('utf-8'))


    def test_recipe_category_view_recipes_dont_publish_is_hidden(self):
        need_title = 'This is a recipe test not \
                        published in category page'
        
        # Need a recipe for this test
        self.make_recipe(title=need_title, is_publish=False)

        response = self.client.get(
            reverse(
                'recipes:category',
                kwargs={
                    'category_id': 1
                }
            )
        )
        self.assertNotIn(need_title, response.content.decode('utf-8'))


    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse(
                'recipes:category',
                kwargs={
                    'category_id': 1000
                    }
                )
            )
        self.assertEqual(response.status_code, 404)
