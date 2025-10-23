class VistaTablero:
    """Vista que muestra el tablero en consola con las soluciones"""
    
    def __init__(self, tamano_tablero):
        self.tamano_tablero = tamano_tablero
    
    def mostrar_solucion(self, reinas, indice):
        print(f"Solución #{indice + 1}")
        
        for fila in range(self.tamano_tablero):
            for col in range(self.tamano_tablero):
                hay_reina = False
                for reina in reinas:
                    if reina.obtener_fila() == fila and reina.obtener_columna() == col:
                        hay_reina = True
                        break
                print(" ♛ " if hay_reina else " . ", end="")
            print()
        print()
    
    def mostrar_todas(self, soluciones):
        print(f"Total de soluciones encontradas: {len(soluciones)}")
        for i, solucion in enumerate(soluciones):
            self.mostrar_solucion(solucion, i)
