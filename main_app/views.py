from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Shoe:
    def __init__(self, name, brand, description, kind):
        self.name = name
        self.brand = brand
        self.description = description
        self.kind = kind

shoes = [
    Shoe('Indy 405', 'Alden', 'Indy shoes', 'work boot'),
    Shoe('Jordan 3', 'Nike', 'Black Jordan 3s', 'basketball'),
    Shoe('Cap toe brown boot', 'Allen Edmonds', 'Cap toe brown boot', 'boot')
]

def home(request):
    return HttpResponse('<h1>Test</h1>')

def about(request):
    return render(request, 'about.html')

def shoes_index(request):
    return render(request, 'shoes/index.html', {'shoes': shoes})