from django.db import models
from django.conf import settings
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
# User = settings.AUTH_USER_MODEL

# class User(AbstractUser):

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

