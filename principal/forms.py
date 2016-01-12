#encoding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import Juego

class BuscarForm(forms.Form):
    titulo = forms.CharField(label="Título del juego", max_length=255,widget=forms.TextInput(attrs={'class':"form-control"}))
