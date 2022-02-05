from django.urls import path
from productapp import views

urlpatterns=[
    path('showproducts', views.get_product),
]