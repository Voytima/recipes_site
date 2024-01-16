from django.urls import path

from .views import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "category/<str:category_name>/",
        RecipeCategoryDetailView.as_view(),
        name="recipe_category_detail",
    ),
    path(
        "recipes/add_recipe/",
        AddRecipeView.as_view(template_name="recipes/add_recipe.html"),
        name="add_recipe",
    ),
    path(
        "category/<str:category_name>/",
        RecipeCategoryDetailView.as_view(),
        name="recipe_category_detail",
    ),
    path("recipe/<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("recipes/edit/<int:pk>/", EditRecipeView.as_view(), name="edit_recipe"),
]
