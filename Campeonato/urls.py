from django.urls import path

from Campeonato import views

urlpatterns = [
    path("inicio/", views.index, name="inicio"),
    path("registroEquipo/", views.RegistrarEquipo.as_view(), name="registrar_equipo"),
    path('generar_match', views.asignar_partidos, name="match"),
    path('generar_resultados', views.generar_resultados, name="resultados"),

]