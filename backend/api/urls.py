from django.urls import path
from .views import getProducts, getProduct

urlpatterns = [
    path("product-list/", getProducts, name='product-list'),
    path("product/<str:pk>/", getProduct, name='product'),
]
