from django.db import models
from django.urls import reverse

FLY = (
    ('Y', 'Yeah, it was fly'),
    ('N', 'Not my flyest, but still fy')
)
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
    date = models.DateField('worn on date')
    fly = models.CharField(
        max_length=1,
        choices=FLY,
        default=FLY[0][0]
    )

    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)    

    def __str__(self):
        return f"{self.get_fly_display()} on {self.date}"