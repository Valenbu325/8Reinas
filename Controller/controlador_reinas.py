
class ControladorReinas:
    """Controlador que maneja la lógica entre modelo y vista"""
    
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
    
    def ejecutar(self, fila, columna):
        self.modelo.resolver_desde(fila, columna)
        self.vista.mostrar_todas(self.modelo.obtener_soluciones())
