from rest_framework import serializers
from . models import City, Weather, Coordinates

class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ('__all__')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name',)

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ('__all__')

