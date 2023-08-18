from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('registro/',views.registro_usuario, name= 'registro'),
    path('bienvenida/', views.bienvenida, name= 'bienvenida'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('sesion_iniciada/', views.sesion_iniciada, name='sesion_iniciada'),
    path('exit/', views.exit, name = 'exit'),
    
]
