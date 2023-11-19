from rest_framework import serializers
from .models import City, Car, Person

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city', 'phone']

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['model', 'kpp', 'engin']

class PersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'position', 'comment_person', 'photo_person']
