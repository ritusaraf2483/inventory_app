from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.FloatField()
    description=models.CharField(max_length=50)
    quantity=models.IntegerField()