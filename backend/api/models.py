from django.db import models
import datetime

class User(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    user_name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ContactsInfo(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, unique=True)
    dob = models.DateField(max_length=8)
    gmail = models.EmailField(max_length = 254) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


