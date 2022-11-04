import re
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import  Credenciales, form_pedido
from django.contrib.auth import authenticate,logout,login
from  django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Informacion,Mesa,Pedido, Producto, Tipo_producto, Producto_pedido
from datetime import datetime


# Create your views here.

def inicioSesion(request):
    if request.method=="POST":
        form = Credenciales(request.POST)
        if form.is_valid():
            usuario = authenticate(username=form.cleaned_data['usuario'], password=form.cleaned_data['secreta'])
            if usuario is not None:
                login(request,usuario)
                #request.session.set_expiry(1200)
                return HttpResponseRedirect('/panel/')
            else:
                messages.error(request,'Usuario o contraseña incorrecto.')
    else:
        form = Credenciales()
    info = Informacion.objects.get()
    return render(request,'pedidos/inicioSesion.html',{'form':form,'restaurante':info})

@login_required(login_url='/salir/')
@never_cache
def panel(request):
    mesas = Mesa.objects.all().order_by('numero')
    for mesa in mesas:
        print(mesa.estado)
    pedidos = Pedido.objects.all()
    return render(request,'pedidos/panel.html',{'mesas':mesas,'pedidos':pedidos})


@login_required(login_url='/salir/')
@never_cache
def pedidos(request,id):
    mesa = Mesa.objects.get(pk=id)
    if request.method == "POST":
        formpedido = form_pedido(request.POST)
        if formpedido.is_valid():
            if mesa.estado == False:
                ped = Pedido()
                ped.mesa = Mesa.objects.get(pk=id)
                ped.mesero = request.user
                ped.fecha = datetime.today().strftime('%Y-%m-%d')
                ped.hora = datetime.now().strftime('%H:%M:%S')
                ped.estado = False
                ped.save()

                estadomesa = Mesa.objects.get(pk=id)
                estadomesa.estado = True
                estadomesa.save()

            prod_ped = Producto_pedido()
            prod_ped.pedido = Pedido.objects.get(mesa=id, estado=False)
            prod_ped.producto = formpedido.cleaned_data['producto']
            prod_ped.cantidad = formpedido.cleaned_data['cantidad']
            prod_ped.observacion = formpedido.cleaned_data['observacion']
            prod_ped.save()
            
            messages.info(request, "Producto agregado correctamente")
        else:
            messages.error(request, "Informacion Invalida")
            print("informacion invalida")
    categorias = Tipo_producto.objects.all()
    formpedido = form_pedido()
    return render(request, 'pedidos/pedido.html', {'categorias':categorias,'formpedido':formpedido})

# hay que buscar el pedido  de la mesa que este en false, ya que una sola mesa puede tener un solo pedido. al momento de cancelar o pagar el pedido este pasa a ser true y se libera la mesa. entonces varios productos pueden pertenecer a un pedido.

@login_required(login_url='/salir/')
@never_cache
def verpedido(request,id):
    verped = Producto_pedido.objects.filter(pedido_id=id)
    return render (request, 'pedidos/verpedido.html', {'verped':verped})


@login_required(login_url='/salir/')
@never_cache
def mesas(request):
    pass

@login_required(login_url='/salir/')
@never_cache
def menu(request):
    pass


@login_required(login_url='/salir/')
@never_cache
def facturar(request):
    pass


def salir(request):
    logout(request)
    return HttpResponseRedirect('/')