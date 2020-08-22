from django.db import models


# Create your models here.
class Person(models.Model):
    full_name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.full_name} z {self.city} ({self.age})"