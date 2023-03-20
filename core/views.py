from django.shortcuts import render
#import requests
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import CitySerializer, WeatherSerializer, CoordinatesSerializer
from .models import City, Weather, Coordinates
from django.conf import settings
from rest_framework.permissions import AllowAny

weather_api = settings.WEATHER_API_KEY


def index(request):
    return render(request, 'index.html')

@permission_classes([AllowAny])
@api_view(['GET', 'POST'])
def city_create_view(request):
    # 13417a3f4de1d1d1f86ccf8e6fd1277f
    #url = 'api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=13417a3f4de1d1d1f86ccf8e6fd1277f'
    if request.method == 'GET':
        city = City.objects.all()
        serializer = CitySerializer(city, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([AllowAny])
@api_view(['GET', 'POST'])
def list_create_city_view(request):
    if request.method == 'GET':
        weathers = Weather.objects.all().order_by('-created_at')
        serializer = WeatherSerializer(weathers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WeatherSerializer(data=request.data)
        if serializer.is_valid():
            #serializer.temperature = (serializer.temperature - 32) / 1.8000
            print(serializer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([AllowAny])
@api_view(['GET', 'POST'])
def add_coordinates(request):
    if request.method == 'GET':
        coordinates = Coordinates.objects.all()
        serializer = CoordinatesSerializer(coordinates, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CoordinatesSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)