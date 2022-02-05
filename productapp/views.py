from django.shortcuts import render
from productapp.models import Product

def home(request):
    return render(request,'home.html')

def get_product(request):
    prods=Product.objects.all()
    return render(request,'productapp/product.html',{'Products':prods})