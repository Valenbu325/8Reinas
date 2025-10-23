from Model.reina import Reina

class Tablero:
    """Modelo que contiene la lógica para resolver el problema de las 8 reinas"""
    
    def __init__(self, tamano=8):
        self.tamano = tamano
        self.soluciones = []
    
    def resolver_desde(self, fila_inicial, columna_inicial):
        self.soluciones = []
        reinas = [Reina(fila_inicial, columna_inicial)]
        filas_para_colocar = [i for i in range(self.tamano) if i != fila_inicial]
        self._backtrack_filas(filas_para_colocar, 0, reinas)
    
    def _backtrack_filas(self, filas_para_colocar, indice_fila, reinas_actuales):
        if len(reinas_actuales) == self.tamano:
            self.soluciones.append(reinas_actuales.copy())
            return
        
        if indice_fila >= len(filas_para_colocar):
            return
        
        fila = filas_para_colocar[indice_fila]
        
        for col in range(self.tamano):
            if self._es_seguro(fila, col, reinas_actuales):
                reinas_actuales.append(Reina(fila, col))
                self._backtrack_filas(filas_para_colocar, indice_fila + 1, reinas_actuales)
                reinas_actuales.pop()
    
    def _es_seguro(self, fila, col, reinas):
        for reina in reinas:
            rf = reina.obtener_fila()
            rc = reina.obtener_columna()
            if rc == col or abs(rf - fila) == abs(rc - col):
                return False
        return True
    
    def obtener_soluciones(self):
        return self.soluciones
    
    def obtener_tamano(self):
        return self.tamano
