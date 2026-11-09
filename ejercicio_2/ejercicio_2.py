import json

class StockInvalidoError(Exception):
    pass

class DispositivoEcológico:
    def __init__(self, dispositivo_id, nombre, stock):
        self.dispositivo_id = dispositivo_id
        self.nombre = nombre
        self.stock = stock

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise StockInvalidoError("El stock no puede ser un valor negativo.")
        self._stock = valor

    def ficha_tecnica(self):
        return f"ID: {self.dispositivo_id} | Nombre: {self.nombre} | Stock: {self.stock}"

class PanelSolar(DispositivoEcológico):
    def __init__(self, dispositivo_id, nombre, stock, potencia_w, tipo_celda):
        super().__init__(dispositivo_id, nombre, stock)
        self.potencia_w = potencia_w
        self.tipo_celda = tipo_celda

    def ficha_tecnica(self):
        base = super().ficha_tecnica()
        return f"{base} | Potencia: {self.potencia_w}W | Tipo de Celda: {self.tipo_celda}"

class GestorInventario:
    @staticmethod
    def guardar_catalogo_json(lista_dispositivos, ruta_archivo):
        datos = []
        for disp in lista_dispositivos:
            item = {
                "clase": type(disp).__name__,
                "dispositivo_id": disp.dispositivo_id,
                "nombre": disp.nombre,
                "stock": disp.stock
            }
            if isinstance(disp, PanelSolar):
                item["potencia_w"] = disp.potencia_w
                item["tipo_celda"] = disp.tipo_celda
            datos.append(item)
        
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    print("--- PRUEBA DE CAPTURA DE EXCEPCIÓN DE STOCK INVÁLIDO ---")
    try:
        dispositivo_fallido = DispositivoEcológico("DEV-999", "Batería Experimental", -5)
    except StockInvalidoError as e:
        print(f"Excepción capturada exitosamente: {e}")

    print("\n--- CREACIÓN DE PRODUCTOS VÁLIDOS ---")
    p1 = PanelSolar("SOL-001", "Panel Monocristalino High-Power", 15, 450, "Monocristalino")
    p2 = PanelSolar("SOL-002", "Panel Policristalino Estándar", 30, 300, "Policristalino")
    d1 = DispositivoEcológico("GEN-001", "Inversor Solar Híbrido", 8)

    dispositivos = [p1, p2, d1]

    for disp in dispositivos:
        print(disp.ficha_tecnica())

    print("\n--- EXPORTACIÓN DE CATÁLOGO A JSON ---")
    archivo_salida = "catalogo_ecotech.json"
    GestorInventario.guardar_catalogo_json(dispositivos, archivo_salida)
    print(f"Catálogo exportado exitosamente al archivo: {archivo_salida}")