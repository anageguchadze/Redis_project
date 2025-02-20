from rest_framework import generics
from .models import Category, Animal, Pet
from .serializers import CategorySerializer, AnimalSerializer, PetSerializer
from .filters import AnimalFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AnimalList(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_backends = [DjangoFilterBackend]
    filter_class = AnimalFilter
    # search_fields = ['name', 'category__name', 'scientific_name', 'habitat', 'diet', 'status']
    def list(self, request, *args, **kwargs):
        query_params = request.query_params
        cache_key = f'animal_list_{query_params}'
        data = cache.get(cache_key)
        if not data:
            filtered_queryset = self.filter_queryset(self.get_queryset())
            data = AnimalSerializer(filtered_queryset, many=True).data
            cache_time = 60 * 5
            cache.set(cache_key, data, cache_time)
        return Response(data)

class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
   
class PetList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer