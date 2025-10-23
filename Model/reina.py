class Reina:
    """Clase que representa la posición de una reina en el tablero"""
    
    def __init__(self, fila, columna):
        self._fila = fila
        self._columna = columna
    
    def obtener_fila(self):
        return self._fila
    
    def obtener_columna(self):
        return self._columna
    
    def __repr__(self):
        return f"Reina(fila={self._fila}, col={self._columna})"
    
