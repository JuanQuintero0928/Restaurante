from email.policy import default
from xml.etree.ElementInclude import default_loader
from django.db import models

# Create your models here.


from django.db import models
from django.conf import settings
#from django.contrib.auth.models import User

# Create your models here.

class Informacion(models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=70)
    telefono = models.CharField(max_length=7)
    celular = models.CharField(max_length=10)
    nit = models.CharField(max_length=15)
    representanteLegal = models.CharField(max_length=70)
    eslogan = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Información"
        verbose_name_plural = "Información"
    
    def __str__(self):
        return self.nombre

class Mesa(models.Model):
    numero = models.CharField(max_length=3)
    capacidad = models.IntegerField()
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Mesas"
        verbose_name_plural = "Mesas"
    
    def __str__(self):
        return f'Mesa {self.numero}'

class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa,on_delete=models.CASCADE)
    mesero = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.BooleanField(default=False)

class Tipo_producto(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    tipoProducto = models.ForeignKey(Tipo_producto, on_delete=models.CASCADE)
    precio = models.FloatField()
    numeroPersonas = models.IntegerField()
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Producto_pedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    observacion = models.TextField(default="")

class Factura(models.Model):
    opciones = (
        ("efectivo","Efectivo"),
        ("debito","Tarjeta debito"),
        ("credito","Tarjeta de Crédito"),
        ("transferencia","Transferencia bancaria"),
    )
    pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    valor = models.FloatField()
    medioPago = models.CharField(max_length=20,choices=opciones)
    estado = models.BooleanField()