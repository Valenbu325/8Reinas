from Model.tablero import Tablero
from View.vista_tablero import VistaTablero
from Controller.controlador_reinas import ControladorReinas

def main():
    print("Problema de las 8 reinas - Proyecto MVC")
    print()
    
    # Solicitar fila y columna inicial al usuario
    try:
        fila = int(input("Ingrese fila inicial (0-7): "))
        columna = int(input("Ingrese columna inicial (0-7): "))
        
        # Validación de límites
        if fila < 0 or fila > 7 or columna < 0 or columna > 7:
            print("Posición inválida. Debe estar entre 0 y 7.")
            return
        
        # Crear componentes MVC
        modelo = Tablero()
        vista = VistaTablero(8)  # Tamaño del tablero
        controlador = ControladorReinas(modelo, vista)
        
        # Ejecutar la lógica con la posición inicial
        print()
        controlador.ejecutar(fila, columna)
        
    except ValueError:
        print("Error: Debe ingresar números enteros.")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")

if __name__ == "__main__":
    main()