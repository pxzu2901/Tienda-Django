from django.urls import path, include
from ProyectoWebApp import views
from .views import VRegistro
urlpatterns = [
    
    path('',VRegistro.as_view(), name="autenticacion"),
    
]

