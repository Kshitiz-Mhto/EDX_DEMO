from django.urls import path
from .views import (city_create_view, index,
            list_create_city_view, add_coordinates)

urlpatterns = [
    path('', index, name="index"),
    path('api/city/', city_create_view, name="city-post"),
    path('api/city/weather/', list_create_city_view, name="city-weather"),
    path('api/city/weather/coordinates/', add_coordinates, name="city-weather-coordinates"),

]
