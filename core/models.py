from django.db import models

class City(models.Model):
    name                = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'

class Weather(models.Model):
    country = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    temperature  = models.FloatField()
    icon = models.CharField(max_length=255)
    lat= models.FloatField(default=321.33)
    lon= models.FloatField(default=321.33)
    #coordinates = models.ForeignKey('Coordinates', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city_name

    def get_celsius(self):
        fahrenheit = self.temperature
        celsius = (fahrenheit-32) / 1.8000
        return celsius

    def save(self, *args, **kwargs): 
        self.temperature = round((self.temperature - 32)/1.8000,2)
        super(Weather, self).save(*args, **kwargs) 

class Coordinates(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return "Latitude:{} - Longitude :{}".format(self.lat, self.lon)

    class Meta:
        verbose_name_plural = "Coordinates"