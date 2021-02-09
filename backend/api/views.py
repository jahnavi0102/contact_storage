from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User, ContactsInfo
from .Serializers import ContactSerializer, UserSerializer, ContactNameSerializer



@api_view(['GET'])
def contact_list(request):

        contacts = ContactsInfo.objects.all()
        serializer = ContactNameSerializer(contacts, many= True)

        return Response(serializer.data, status=200)

@api_view(['POST'])
def add_contact(request):
    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save() 

    return Response(serializer.data)    

@api_view(['GET'])
def contact_detail(request, pk):

        contacts = ContactsInfo.objects.get(id= pk)
        serializer = ContactSerializer(contacts, many= False)
        return Response(serializer.data, status=200)

@api_view(['GET'])
def delete_contact(request, pk):

        contacts = ContactsInfo.objects.delete(id=pk)
        serializer = ContactSerializer(contacts, many = False)
        return Response(serializer.data, status=200)

@api_view(['GET'])
def update_contact(request, pk):

        contacts = ContactsInfo.objects.update(id=pk)
        serializer = ContactSerializer(contacts, many = True)
        return Response(serializer.data, status=200)