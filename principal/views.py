#encoding:utf-8
# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from principal.forms import BuscarForm
from principal.models import Juego


def index(request):
    form = ""
    titulo = request.GET.get('titulo','')
    if(titulo==''):
        form = BuscarForm()
        form.titulo = titulo
        return render_to_response('index.html', {'formulario':form,'request':request,'mostrarForm':True},context_instance=RequestContext(request))
    else:
        juegos = Juego.objects.filter(nombre__contains=str(titulo))
        return render_to_response('index.html', {'juegos':juegos,'mostrarForm':False},context_instance=RequestContext(request))