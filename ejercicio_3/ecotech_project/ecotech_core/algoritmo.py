def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    if consumo_kwh < 0:
        raise ValueError("El consumo en kWh no puede ser negativo.")
    return consumo_kwh * factor_emision


def obtener_metricas_consumo(registros):
    if not registros:
        return {
            "total_emisiones": 0.0,
            "planta_mayor_consumo": "Ninguna",
            "max_consumo": 0.0
        }

    total_emisiones = 0.0
    mayor_consumo = -1.0
    planta_mayor_consumo = ""

    for reg in registros:
        planta = reg.get("planta", "Desconocida")
        consumo = reg.get("consumo_kwh", 0.0)
        
        emision = calcular_emisiones_carbono(consumo)
        total_emisiones += emision

        if consumo > mayor_consumo:
            mayor_consumo = consumo
            planta_mayor_consumo = planta

    return {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo,
        "max_consumo": mayor_consumo
    }