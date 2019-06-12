from django.shortcuts import render
from django.http import HttpResponse
from .models import Shoe
# Create your views here.


def home(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def shoes_index(request):
    shoes = Shoe.objects.all()
    return render(request, 'shoes/index.html', {'shoes': shoes})