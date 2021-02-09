from .models import User, ContactsInfo
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id' , 'user_name', 'password']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactsInfo
        fields = ['full_name', 'phone', 'dob', 'gmail']