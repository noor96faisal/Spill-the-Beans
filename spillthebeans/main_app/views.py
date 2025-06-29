from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
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

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == 'POST':
        print("POST received")
        if form.is_valid():
            print("Form is valid")
            user = form.save()
            login(request, user)
            print("User logged in:", user.username)
            return redirect('home')
        else:
            print("Form errors:", form.errors)
    else:
        print("GET request")

    return render(request, 'main_app/register.html', {'form': form})


