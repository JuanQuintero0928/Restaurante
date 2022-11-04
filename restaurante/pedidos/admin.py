from django.contrib import admin
from .models import Informacion,Mesa,Pedido,Tipo_producto,Producto,Producto_pedido,Factura

# Register your models here.
admin.site.register(Informacion)
admin.site.register(Mesa)
admin.site.register(Pedido)
admin.site.register(Tipo_producto)
admin.site.register(Producto)
admin.site.register(Producto_pedido)
admin.site.register(Factura)
