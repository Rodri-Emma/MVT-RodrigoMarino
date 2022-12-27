from django.db import models
from django.shortcuts import render


class integrantes(models.Model):
    name = models.CharField(max_length=50)
    age = models.FloatField()
    nationality = models.BooleanField()
    



# Create your models here.
