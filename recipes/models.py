from django.contrib.auth.models import User
from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    steps = models.TextField()
    cooking_time = models.PositiveIntegerField()
    image = models.ImageField(upload_to="recipe_images/", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")

    def __str__(self):
        return self.title


class RecipeCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.recipe.title} - {self.ingredient.name}"


class RecipeCategoryRelation(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(RecipeCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.recipe.title} - {self.category.name}"
