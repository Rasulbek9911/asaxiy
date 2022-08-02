from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from helpers.pagination import CustomPagination


# Create your views here.

# bosh menu
class ProductIsTopView(generics.ListAPIView):
    queryset = Product.objects.is_top()
    serializer_class = ProductSerializer


class ProductIsWeekView(generics.ListAPIView):
    queryset = Product.objects.is_week()
    serializer_class = ProductSerializer


class ProductIsDiscountView(generics.ListAPIView):
    queryset = Product.objects.is_discount()
    serializer_class = ProductSerializer


class ProductIsSummerView(generics.ListAPIView):
    queryset = Product.objects.is_summer()
    serializer_class = ProductSerializer


class ProductIsPopularView(generics.ListAPIView):
    queryset = Product.objects.is_popular()
    serializer_class = ProductSerializer


class ProductBookCategory(generics.ListAPIView):
    queryset = Product.objects.filter(category__title='book')
    serializer_class = ProductSerializer


# Base categories
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
