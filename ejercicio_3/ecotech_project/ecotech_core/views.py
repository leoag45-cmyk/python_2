from django.shortcuts import render
from .algoritmo import obtener_metricas_consumo

def vista_panel_sustentabilidad(request):
    registros_mock = [
        {"planta": "Planta Norte", "consumo_kwh": 450.0},
        {"planta": "Planta Sur", "consumo_kwh": 780.0},
        {"planta": "Planta Este", "consumo_kwh": 320.0}
    ]
    
    metricas = obtener_metricas_consumo(registros_mock)
    
    contexto = {
        "metricas": metricas,
        "registros": registros_mock
    }
    
    return render(request, "sustentabilidad/panel.html", contexto)