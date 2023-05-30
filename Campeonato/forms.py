from django.forms import ModelForm
from Campeonato.models import *

class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = ("nombre_equipo",)
