from django.shortcuts import render
from .forms import UserForm, PostForm
from django.conf import settings

def user_register(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            form.save()
    form1 = UserForm()
    return render(request,'register.html',{'form':form1})

def user_post(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
    form1 = PostForm()
    return render(request,'post.html',{'form':form1})
