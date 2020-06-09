from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    weight = models.FloatField()
    price = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
