from django.contrib import admin
from .models import Category, Animal, Pet

# Register your models here.
admin.site.register(Category)
admin.site.register(Animal)
admin.site.register(Pet)