from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

import random

from Campeonato.models import *
from Campeonato.forms import *
# Create your views here.

def index(request):
    equipos = Equipo.objects.all()
    partidos = partido_x_equipo.objects.all()
    return render(request, "index.html", {"equipos":equipos, "partidos":partidos})


class RegistrarEquipo(CreateView):
    model = Equipo
    template_name = "form1.html"
    form_class = EquipoForm

    def form_valid(self, form):
        form.save()
        return redirect('inicio')
    
def asignar_partidos(request):
    contador = 1
    
    equipos = Equipo.objects.all()
    eqs=[]
    cantidad_equipos = Equipo.objects.count()
    cant_partidos = cantidad_equipos/2
    for object in equipos:
        eqs.append(object.id)
        
    if cantidad_equipos %2 != 0:
        print("no es una cantidad par de equipos")
    else:
        if cantidad_equipos %4 !=0:
            print("no es una cantidad multiplo de 4 para formar equipos")
        
        else:
            while cant_partidos >0:
                patd= Partido.objects.create(numero_de_partido= contador)
                equip1 = random.randint(0, len(eqs)-1)
                a = eqs[equip1]
                equipo1 = Equipo.objects.get(id=a)
                check = partido_x_equipo.objects.get(equipo = equipo1)
                if check: 
                    equip1 = random.randint(0, len(eqs)-1)
                    a = eqs[equip1]
                eqs.pop(equip1)
                partido_x_equipo.objects.create(partido = patd, equipo = Equipo.objects.get(id=a), goles_TR=0)
                equip2 = random.randint(0, len(eqs)-1)
                b = eqs[equip2]
                partido_x_equipo.objects.create(partido = patd, equipo = Equipo.objects.get(id= b), goles_TR=0)    
                contador +=1
                cant_partidos -=1
    return redirect('inicio')

def generar_resultados(request):
    partidos = partido_x_equipo.objects.all()
    for partido in partidos:
        partido.goles_TR=random.randint(0, 10)
        partido.tarjetas_amarillas= random.randint(0, 10)
        partido.tarjetas_rojas = random.randint(0, 10)
        partido.save()
    return redirect('inicio')
