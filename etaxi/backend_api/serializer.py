from rest_framework import serializers
from .models import City, Car

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city', 'phone']

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['model', 'kpp', 'engin']
