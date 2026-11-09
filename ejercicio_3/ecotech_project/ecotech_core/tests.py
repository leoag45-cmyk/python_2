import unittest
from .algoritmo import calcular_emisiones_carbono, obtener_metricas_consumo

class TestCalculoEmisiones(unittest.TestCase):
    
    def test_calculo_nominal(self):
        resultado = calcular_emisiones_carbono(100.0, 0.4)
        self.assertEqual(resultado, 40.0)

    def test_calculo_factor_personalizado(self):
        resultado = calcular_emisiones_carbono(200.0, 0.5)
        self.assertEqual(resultado, 100.0)

    def test_consumo_negativo_excepcion(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-10.0)

    def test_obtener_metricas_consumo(self):
        registros = [
            {"planta": "Planta Norte", "consumo_kwh": 150.0},
            {"planta": "Planta Sur", "consumo_kwh": 300.0}
        ]
        metricas = obtener_metricas_consumo(registros)
        self.assertEqual(metricas["total_emisiones"], 180.0)
        self.assertEqual(metricas["planta_mayor_consumo"], "Planta Sur")