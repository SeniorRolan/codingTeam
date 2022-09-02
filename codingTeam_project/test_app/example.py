from decimal import Decimal
from models import Food, FoodCategory

drinks = FoodCategory.objects.get(pk=1)
food = FoodCategory.objects.get(pk=2)

Food.objects.create(category=drinks, code=1, name_ru='Фанта', cost=Decimal('9.99'))
Food.objects.create(category=food, code=2, name_ru='Чизбургер', cost=Decimal('2.99'))