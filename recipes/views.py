from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import TemplateView

from recipes.models import Recipe, RecipeCategory

from .forms import RecipeForm


class RecipeCategoryDetailView(View):
    template_name = "recipes/recipe_category_detail.html"
    recipes_per_page = 5

    def get(self, request, category_name):
        category = get_object_or_404(RecipeCategory, name=category_name)
        recipes = Recipe.objects.filter(category=category)
        paginator = Paginator(recipes, self.recipes_per_page)
        page = request.GET.get("page", 1)

        try:
            recipes = paginator.page(page)
        except PageNotAnInteger:
            recipes = paginator.page(1)
        except EmptyPage:
            recipes = paginator.page(paginator.num_pages)

        context = {"category": category, "recipes": recipes}
        return render(request, self.template_name, context)


class RecipeDetailView(View):
    template_name = "recipes/recipe_detail.html"

    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        context = {"recipe": recipe}
        return render(request, self.template_name, context)


class IndexView(TemplateView):
    template_name = "recipes/index.html"

    def get_context_data(self, **kwargs):
        categories = RecipeCategory.objects.all()
        recipes = Recipe.objects.all()
        context = super().get_context_data(**kwargs)
        context["categories"] = categories
        context["recipes"] = recipes
        random_recipes = Recipe.objects.order_by("?")[:5]
        context["random_recipes"] = random_recipes
        return context


class AddRecipeView(View):
    template_name = "add_recipe.html"
    form_class = RecipeForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        categories = RecipeCategory.objects.all()
        return render(
            request, self.template_name, {"form": form, "categories": categories}
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        categories = RecipeCategory.objects.all()
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()
            return redirect("index")
        return render(
            request, self.template_name, {"form": form, "categories": categories}
        )


class EditRecipeView(View):
    template_name = "recipes/edit_recipe.html"
    form_class = RecipeForm

    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        form = self.form_class(instance=recipe)
        return render(request, self.template_name, {"form": form, "recipe": recipe})

    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipe_detail", pk=recipe.pk)
        return render(request, self.template_name, {"form": form, "recipe": recipe})
