from django import forms
from django.forms import Textarea

from .models import Producto


class Credenciales(forms.Form):
    usuario = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Usuario','aria-label':'Usuario'}))
    secreta = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña'}))

class form_pedido(forms.Form):
    producto = forms.ModelChoiceField(queryset=Producto.objects.all())
    cantidad = forms.IntegerField()
    observacion = forms.CharField()