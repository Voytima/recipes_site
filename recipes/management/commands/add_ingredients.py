from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from recipes.models import Ingredient


class Command(BaseCommand):
    help = "Add ingredients to the database"

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(is_superuser=True).exists():
            raise CommandError("This command can only be run by a superuser")

        ingredients = [
            {"name": "огурец"},
            {"name": "томат"},
            {"name": "сыр"},
            {"name": "соль"},
            {"name": "перец"},
            {"name": "свекла"},
            {"name": "картофель"},
            {"name": "свинина"},
            {"name": "говядина"},
            {"name": "курятина"},
            {"name": "молоко"},
            {"name": "сметана"},
            {"name": "майонез"},
            {"name": "хлеб"},
            {"name": "батон"},
            {"name": "яйца куриные"},
            {"name": "яйца перепелиные"},
            {"name": "яйца страусиные"},
            {"name": "морской коктейль"},
            {"name": "креветки"},
            {"name": "кальмар"},
            {"name": "рыба речная"},
            {"name": "рыба морская"},
            {"name": "рыба атлантическая"},
            {"name": "рак"},
            {"name": "краб"},
            {"name": "морковь"},
            {"name": "специи"},
            {"name": "баклажан"},
            {"name": "апельсин"},
            {"name": "яблоко"},
            {"name": "банан"},
            {"name": "ананас"},
            {"name": "киви"},
            {"name": "мандарин"},
            {"name": "гранат"},
            {"name": "лимон"},
            {"name": "лайм"},
            {"name": "икра красная"},
            {"name": "икра черная"},
            {"name": "икра заморская, баклажанная"},
            {"name": "морская капуста"},
            {"name": "крабовые палочки"},
            {"name": "крабовое мясо"},
            {"name": "вино красное"},
            {"name": "вино белое"},
            {"name": "редис"},
            {"name": "лук"},
            {"name": "лук-шалот"},
            {"name": "батат"},
            {"name": "фарш"},
            {"name": "сельдерей"},
            {"name": "тофу"},
            {"name": "телятина"},
            {"name": "крольчатина"},
            {"name": "индюшатина"},
            {"name": "макароны"},
            {"name": "рис"},
            {"name": "гречка"},
            {"name": "перловка"},
            {"name": "огурец соленый"},
            {"name": "сливки"},
            {"name": "томатная паста"},
            {"name": "сахар"},
            {"name": "уксус"},
            {"name": "винный уксус"},
            {"name": "соевый соус"},
            {"name": "бальзамический уксус"},
            {"name": "творожный сыр"},
            {"name": "сухарики"},
            {"name": "плавленый сырок"},
            {"name": "брокколи"},
            {"name": "цветная капуста"},
            {"name": "стручковая фасоль"},
            {"name": "кукуруза маринованная"},
            {"name": "горошек маринованный"},
            {"name": "чеснок"},
        ]

        for ingredient_data in ingredients:
            Ingredient.objects.create(**ingredient_data)

        self.stdout.write(self.style.SUCCESS("Ingredients added successfully"))
