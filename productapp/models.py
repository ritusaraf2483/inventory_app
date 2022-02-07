from django.db import models
from django.urls import reverse


class Product(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    price=models.FloatField()
    description=models.CharField(max_length=50)
    quantity=models.IntegerField()

    def get_absolute_url(self):
        return reverse('Product:product_list')