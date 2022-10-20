from django.db import models
from datetime import datetime
# Create your models here.
class Family(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    nacimiento = models.DateField(auto_now=False, auto_now_add=False)