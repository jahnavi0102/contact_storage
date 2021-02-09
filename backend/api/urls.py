from django.urls import path
from . import  views


urlpatterns = [
    path('list/', views.contact_list),
    path('add/', views.add_contact),
    path('detail/<str:pk>', views.contact_detail),
    path('delete/<str:pk>',views.delete_contact),
    path('update/<str:pk>',views.update_contact.as_view()),
]