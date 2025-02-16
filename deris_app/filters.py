import django_filters
from .models import Animal


class AnimalFilter(django_filters.FilterSet):
    class Meta:
        model = Animal
        fields = ['name', 'category', 'scientific_name', 'habitat', 'diet', 'status']