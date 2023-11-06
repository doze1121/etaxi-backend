from django.db import models

class City(models.Model):
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Car(models.Model):
    city = models.ForeignKey(City, related_name='cars', on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    kpp = models.CharField(max_length=16)
    engin = models.CharField(max_length=100)

    def __str__(self):
        return self.model
