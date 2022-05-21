from django.urls import path
from .import views

urlpatterns =[
    path('heli_engine/',views.index),
]