from django.shortcuts import render
from django.shortcuts import redirect
from .models import BrewingMethod, Category 

def home(request):
    methods = BrewingMethod.objects.all()
    categories = Category.objects.all()  
    return render(request, 'main_app/home.html', {
        'methods': methods,
        'categories': categories  
    })

def add_recipe(request):
    return render(request, 'main_app/add_recipe.html')
