from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Message(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    category = models.CharField(
        max_length=10,
        choices=[
        ("", "---------"),
        ('question', "Pytanie"),
        ('other', "Inne")
        ]
    )
    subject = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f"{self.subject} od {self.email}"

    def get_absolute_url(self):
        return reverse('crud:message-list')