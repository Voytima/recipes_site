from recipes.models import RecipeCategory


def recipe_categories(request):
    categories = RecipeCategory.objects.all()
    return {"all_categories": categories}
