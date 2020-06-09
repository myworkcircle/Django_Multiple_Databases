from django import forms
from django.contrib.auth.models import User
from .models import Post
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email']
        extrakwargs = {
            'password' : {'write_only':True}
        }
    def save(self,*args,**kwargs):
        user_obj = User(
            username = self.cleaned_data['username'],
            email = self.cleaned_data['email'],
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name']
        )
        password = self.cleaned_data['password']
        user_obj.set_password(password)
        user_obj.save()
        return user_obj

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']