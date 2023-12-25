from django.urls import path, include
from ProyectoWebApp import views
from . import views
urlpatterns = [
    
    path('',views.contacto, name="Contacto"),
    
]

