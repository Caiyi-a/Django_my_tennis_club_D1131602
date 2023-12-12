from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('courts/', views.courts, name='courts'),
    path('courts/courts_details/<int:id>', views.courts_details, name='courts_details'),
]