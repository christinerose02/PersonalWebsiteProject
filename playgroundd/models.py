from django.db import models
from django.contrib import admin    


# Create your models here.
class Scheduler(models.Model):
    cellnumber = models.CharField(max_length=20)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=50)
    pettype = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()

def __str__(self):
    return self.name