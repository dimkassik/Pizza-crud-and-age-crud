from django.shortcuts import render

from rest_framework import viewsets
from .models import Restaurant, Pizza
from .serializers import RestaurantSerializer, PizzaSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer