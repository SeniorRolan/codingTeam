from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from .serializers import FoodListSerializer
from .models import Food, FoodCategory


def only_published_food(request):
    serializer = FoodListSerializer
    queryset = FoodCategory.objects.filter(food__is_publish=True).distinct()
    response = serializer(queryset, many=True)
    return JsonResponse(response.data, safe=False, json_dumps_params={'ensure_ascii': False})
