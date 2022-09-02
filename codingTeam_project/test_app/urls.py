from django.urls import path

from .views import only_published_food

urlpatterns = [
    path("api/v1/foods/", only_published_food),
]
