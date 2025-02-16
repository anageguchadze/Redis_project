from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryList, CategoryDetail, AnimalList, AnimalDetail

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),
    path('animals/', AnimalList.as_view()),
    path('animals/<int:pk>/', AnimalDetail.as_view()),
]