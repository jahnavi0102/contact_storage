from django.urls import path
from . import  views


urlpatterns = [
    path('list/', views.contact_list),
    path('add/', views.add_contact),
    path('detail/<str:pk>', views.contact_detail),
]