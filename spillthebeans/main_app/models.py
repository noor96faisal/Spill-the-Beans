from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='category_icons/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class BrewingMethod(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='method_icons/', blank=True, null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    instructions = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    method = models.ForeignKey(BrewingMethod, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  

    def __str__(self):
        return self.title


class Reaction(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    like = models.BooleanField()

    def __str__(self):
        return f"{'Like' if self.like else 'Dislike'} by {self.profile}"
