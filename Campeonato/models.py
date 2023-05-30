from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre_equipo = models.CharField(max_length=45)

class Partido(models.Model):
    numero_de_partido = models.IntegerField()
    equipo_ganador=models.ForeignKey(Equipo,on_delete=models.CASCADE, null=True, blank=True)

class partido_x_equipo(models.Model):
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    goles_TR = models.IntegerField()
    tarjetas_amarillas = models.IntegerField(null=True, blank=True)
    tarjetas_rojas = models.IntegerField(null=True, blank=True)
    penales = models.IntegerField(null=True, blank=True)