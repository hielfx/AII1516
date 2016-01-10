#encoding: utf-8
from django.db import models

# Create your models here.

class Juego(models.Model):
    url = models.URLField()
    nombre = models.CharField(max_length=255)
    precio = models.FloatField()
    web = models.CharField(max_length=255)#Página web de la que procede
    
    def __str__(self):
        return str(self.nombre)+" - "+str(self.precio)