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

class Person(models.Model):
    city = models.ForeignKey(City, related_name='pers', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    comment_person = models.CharField(max_length=500)
    photo_person = models.ImageField(upload_to='person_photos/', blank=True, null=True)

    def __str__(self):
        return self.name
