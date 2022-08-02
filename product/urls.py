from django.urls import path
from .views import *

urlpatterns = [
    path('product-istop/', ProductIsTopView.as_view()),
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>/', CategoryRetrieveView.as_view()),
    path('product-category-book/', ProductBookCategory.as_view()),
]
