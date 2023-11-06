from django.shortcuts import render
from rest_framework.views import APIView
from .models import City
from .serializer import CitySerializer
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
