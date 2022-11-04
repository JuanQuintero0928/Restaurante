from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('', views.inicioSesion,name='inicioSesion'),
    path('panel/', views.panel,name='panel'),
    path('pedidos/<int:id>', views.pedidos,name='pedidos'),
    path('menu/', views.menu,name='menu'),
    path('facturar/', views.facturar,name='facturar'),
    path('salir/', views.salir,name='salir'),
    path('verpedido/<int:id>', views.verpedido ,name='verpedido'),
]
