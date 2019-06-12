from django.db import models

# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=40)
    brand = models.CharField(max_length=40)
    color = models.CharField(max_length=40)    
    description = models.TextField(max_length=100)    
    category = models.CharField(max_length=40)    

    def __str__(self):
        return self.name