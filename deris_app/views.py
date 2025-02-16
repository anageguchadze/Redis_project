from rest_framework import generics
from .models import Category, Animal
from .serializers import CategorySerializer, AnimalSerializer
from .filters import AnimalFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AnimalList(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = AnimalFilter
    search_fields = ['name', 'category__name', 'scientific_name', 'habitat', 'diet', 'status']


class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
   