from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Recipe, BrewingMethod, Category
from .forms import RecipeForm
from django.shortcuts import get_object_or_404



def home(request):
    methods = BrewingMethod.objects.all()
    categories = Category.objects.all()
    return render(request, 'main_app/home.html', {
        'methods': methods,
        'categories': categories
    })


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'main_app/recipe_list.html', {'recipes': recipes})



@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'main_app/add_recipe.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print("User logged in:", user.username)
            return redirect('home')
        else:
            print("Form errors:", form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'main_app/register.html', {'form': form})



def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'main_app/category_detail.html', {'category': category})


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("home")
    return render(request, "login.html", {"form": form})


def profile_view(request):
    return render(request, 'main_app/profile.html', {'user': request.user})

def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'main_app/confirm_delete.html', {'recipe': recipe})