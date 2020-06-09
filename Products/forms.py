from django import forms
from django.contrib.auth.models import User
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    

