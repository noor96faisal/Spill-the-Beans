from django.shortcuts import render
from .models import BrewingMethod

# Create your views here.
def home(request):
    methods = BrewingMethod.objects.all()
    return render(request, 'main_app/home.html', {'methods': methods})

def add_recipe(request):
    return render(request, 'main_app/add_recipe.html')