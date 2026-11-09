import re

def limpiar_registro_sensor(registro_raw):
    sensor_id = registro_raw.get("sensor_id", "").strip()
    temp_raw = str(registro_raw.get("temperatura", "0"))
    temp_clean_str = re.sub(r'[^0-9.-]', '', temp_raw)
    
    try:
        temperatura = float(temp_clean_str) if temp_clean_str else 0.0
    except ValueError:
        temperatura = 0.0
        
    ubicacion = registro_raw.get("ubicacion")
    if not ubicacion or not str(ubicacion).strip():
        ubicacion = "Planta General"
    else:
        ubicacion = str(ubicacion).strip()
        
    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }


def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    if not lista_sensores_limpios:
        return [], 0.0
        
    lista_sensores_alerta = []
    suma_temperaturas = 0.0
    total_sensores = len(lista_sensores_limpios)
    
    for sensor in lista_sensores_limpios:
        temp = sensor.get("temperatura", 0.0)
        suma_temperaturas += temp
        
        if temp > umbral_temperatura:
            lista_sensores_alerta.append(sensor.get("sensor_id"))
            
    promedio_temperatura = suma_temperaturas / total_sensores
    
    return lista_sensores_alerta, promedio_temperatura


if __name__ == "__main__":
    registros_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002", "temperatura": "29.8°C", "ubicacion": ""},
        {"sensor_id": " SENSOR-003 ", "temperatura": "31.2 C", "ubicacion": "Planta Sur"},
        {"sensor_id": "SENSOR-004", "temperatura": "22.1", "ubicacion": None},
        {"sensor_id": " SENSOR-005", "temperatura": "28.5 °C", "ubicacion": "Planta Este"}
    ]
    
    print("--- 1. PROCESO DE LIMPIEZA Y NORMALIZACIÓN ---")
    sensores_limpios = []
    for reg in registros_crudos:
        limpio = limpiar_registro_sensor(reg)
        sensores_limpios.append(limpio)
        print(f"Crudo: {reg}  -->  Limpio: {limpio}")
        
    UMBRAL_ALERTA = 28.0
    
    sensores_alerta, promedio_global = generar_resumen_sensores(sensores_limpios, UMBRAL_ALERTA)
    
    print("\n--- 2. REPORTE CONSOLIDADO PARA TOMA DE DECISIONES ---")
    print(f"• Umbral de Temperatura Configurado : {UMBRAL_ALERTA} °C")
    print(f"• Temperatura Promedio Global de Planta: {promedio_global:.2f} °C")
    print(f"• Dispositivos que superan el umbral ({len(sensores_alerta)}): {', '.join(sensores_alerta) if sensores_alerta else 'Ninguno'}")