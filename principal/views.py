#encoding:utf-8
# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from principal.forms import BuscarForm
from principal.models import Juego
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import gettingData

def index(request):
    form = ""
    titulo = request.GET.get('titulo','')
    page = request.GET.get('page','')
    if(titulo=='' and page==''):
        form = BuscarForm()
        form.titulo = titulo
        return render_to_response('index.html', {'formulario':form,'request':request,'mostrarForm':True},context_instance=RequestContext(request))
    else:
        if titulo!='' and page=='':
            Juego.objects.all().delete()#Borramos el contenido de la tabla
            gettingData.buscar_nombre(titulo)#Obtenemos los nuevos juegos
            
        juegos_list = Juego.objects.filter(nombre__contains=str(titulo)).order_by('precio')#ordenamos por precio para mostrar los baratos
        paginator = Paginator(juegos_list,6)#muestra 6 juegos por pagina
        try:
            juegos = paginator.page(page)
        except PageNotAnInteger:
            #Si page no es un entero mostramos la primera pagina
            juegos = paginator.page(1)
        except EmptyPage:
            #Si page esta fuera de rango, mostramos la ultima pagina
            juegos = paginator.page(paginator.num_pages)
        return render_to_response('index.html', {'juegos':juegos,'mostrarForm':False},context_instance=RequestContext(request))