from django.urls import path, re_path
from django.views.generic import UpdateView

from productapp import views
from productapp.forms import ProductForm
from productapp.models import Product

app_name="Product"
urlpatterns=[
    path('showproducts', views.get_product.as_view(),name='product_list'),
    #path('<int:pk>',views.product_detail.as_view()),
    #re_path(r'^(?P<pk>[0-9]+)$',views.product_detail.as_view(),name='product_detail'),
    re_path(r'^(?P<product_id>[0-9]+)$',views.product_detail,name='product_detail'),
    #path('new',views.ProductCreate.as_view()),
    path('new', views.product_new),
    #path("<int:product_id>/update",views.product_update)
    path('<int:pk>/update',UpdateView.as_view(model=Product,template_name='productapp/product_update.html',form_class=ProductForm))
]