from django.db import models
from django.urls import reverse

# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=40)
    brand = models.CharField(max_length=40)
    color = models.CharField(max_length=40)    
    description = models.TextField(max_length=100)    
    category = models.CharField(max_length=40)    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'shoe_id': self.id})

class Wearings(models.Model):
    date = models.DateField()
    activity = models.CharField(max_length=30)