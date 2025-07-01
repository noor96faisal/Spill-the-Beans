from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('register/', views.register, name='signup'),  # ✅ changed name from 'register' to 'signup'
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(template_name='main_app/login.html'),
        name='login'
    ),
    path('profile/', views.profile_view, name='profile'),

]
