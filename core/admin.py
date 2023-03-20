from django.contrib import admin
from .models import City, Weather, Coordinates

class WeatherAdmin(admin.ModelAdmin):
    list_display = ('city_name','country','description','temperature','icon',
        'lat','lon','created_at',)

admin.site.register(Coordinates)
admin.site.register(Weather,WeatherAdmin)
admin.site.register(City)