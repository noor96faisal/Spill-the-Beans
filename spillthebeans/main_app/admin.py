from django.contrib import admin
from .models import BrewingMethod, Recipe, Category, Reaction
# Register your models here.
admin.site.register(BrewingMethod)
admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Reaction)