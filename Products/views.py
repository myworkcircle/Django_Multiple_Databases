from django.shortcuts import render


from django.shortcuts import render
from .forms import ProductForm
from django.conf import settings

def product_details(request):
    if request.method=="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            form.save()
    form1 = ProductForm()
    return render(request,'product.html',{'form':form1})


