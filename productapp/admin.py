from django.contrib import admin
from productapp.models import Product

# Register your models here.
class AdminProduct(admin.ModelAdmin):
       list_display = ['name','price','description','quantity']

admin.site.register(Product,AdminProduct)