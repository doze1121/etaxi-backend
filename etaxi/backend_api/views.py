from django.shortcuts import render
from rest_framework.views import APIView
from .models import City, Car
from .serializer import CitySerializer, CarSerializer
from rest_framework.response import Response

class CityView(APIView):
    def get(self, requset):
        output = [
            {
                'city': output.city,
                'phone': output.phone,
            } for output in City.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class CarView(APIView):
    def get(self, request):
        output = [
            {
                'model': car.model,
                'kpp': car.kpp,
                'engin': car.engin,
            } for car in Car.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            city_id = request.data.get('city')
            serializer.save(city_id=city_id)
            return Response(serializer.data)
