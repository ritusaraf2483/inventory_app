from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from productapp.forms import ProductForm
from productapp.models import Product

def home(request):
    return render(request,'home.html')

#def get_product(request):
#    prods=Product.objects.all()
#    return render(request,'productapp/product.html',{'Products':prods})

def product_detail(request,product_id):
     #prod=Product.objects.filter(id=product_id)
     prod=get_object_or_404(Product,id=product_id)
     return render(request,'productapp/product_detail.html',{'object':prod})


class get_product(ListView):
     model = Product
     template_name = 'productapp/product.html'

#class product_detail(DetailView):
#     template_name = 'productapp/product_detail.html'
#     model = Product

class ProductCreate(CreateView):
     model = Product
     form_class = ProductForm
     template_name = 'productapp/product_new.html'
     success_url = reverse_lazy('Product:product_list')

def product_new(request):
     if request.method=='GET':
          return render(request, 'productapp/product_new.html', {'form': ProductForm})
     else:
          form=ProductForm(request.POST)
          if form.is_valid():
                form.save(commit=True)
                return HttpResponseRedirect(reverse('Product:product_list'))
          else:
               return render(request, 'productapp/product_new.html', {'form': ProductForm})

def product_update(request,product_id):
     prod=get_object_or_404(Product,id=product_id)
     form=ProductForm(request.POST or None,instance=prod)
     if request.method=='POST':
          if form.is_valid():
               form.save()
               return HttpResponseRedirect(reverse('Product:product_list'))
     else:
         return render(request,'productapp/product_update.html',{'form':form})