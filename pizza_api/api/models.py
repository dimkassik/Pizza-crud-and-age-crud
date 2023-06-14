from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Pizza(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sir = models.CharField(max_length=100)
    tolchina = models.CharField(max_length=100)
    secretnii_ingridient = models.CharField(max_length=100)
    def __str__(self):
        return self.name
