from django.contrib import admin
from django.utils.safestring import mark_safe

from recipes.models import Ingredient, Recipe, RecipeCategory, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "cooking_time")
    search_fields = ("title", "author__username")
    inlines = [RecipeIngredientInline]
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                '<img src="{url}" width="{width}" height={height} />'.format(
                    url=obj.image.url,
                    width=obj.image.width,
                    height=obj.image.height,
                )
            )
        return "No Image"

    image_preview.short_description = "Image Preview"


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(RecipeCategory)
class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
