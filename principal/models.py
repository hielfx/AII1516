from django.db import models

# Create your models here.

class Juego(models.Model):
    url = models.URLField()
    nombre = models.CharField(max_lenght=255)
    precio = models.FloatField()

