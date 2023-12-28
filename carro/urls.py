from django.urls import path, include
from . import views

app_name="carro"

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('',views.home, name="Home"),
    path('agregar/<int:producto_id>/', views.agregar_producto, name="agregar"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="eliminar"),
    path('restar/<int:producto_id>/', views.restar_producto, name="restar"),
    path('limpiar/', views.limpiar_Carro, name="limpiar"),
    
]

