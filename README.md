# 🏰 Problema de las 8 Reinas - Python MVC

Solución al clásico problema de las 8 reinas del ajedrez utilizando el patrón de diseño **Modelo-Vista-Controlador (MVC)** en Python.

## 📋 Descripción

El problema de las 8 reinas consiste en colocar 8 reinas en un tablero de ajedrez 8×8 de manera que ninguna reina amenace a otra. Esto significa que no puede haber dos reinas en:
- La misma fila
- La misma columna
- La misma diagonal

Este proyecto permite al usuario especificar la posición inicial de la primera reina y encuentra todas las soluciones posibles que incluyan esa reina en esa posición.

## 🏗️ Arquitectura MVC

El proyecto está organizado siguiendo el patrón MVC:

```
Problema8Reinas/
│
├── modelo/
│   ├── __init__.py
│   ├── reina.py          # Clase Reina (representa una posición)
│   └── tablero.py        # Clase Tablero (lógica del problema)
│
├── vista/
│   ├── __init__.py
│   └── vista_tablero.py  # Muestra las soluciones en consola
│
├── controlador/
│   ├── __init__.py
│   └── controlador_reinas.py  # Coordina modelo y vista
│
├── main.py               # Punto de entrada de la aplicación
└── README.md
```

### Componentes

- **Modelo (`modelo/`)**: Contiene la lógica del negocio
  - `Reina`: Representa la posición de una reina (fila, columna)
  - `Tablero`: Implementa el algoritmo de backtracking para encontrar soluciones

- **Vista (`vista/`)**: Maneja la presentación
  - `VistaTablero`: Muestra las soluciones en consola con formato visual

- **Controlador (`controlador/`)**: Coordina modelo y vista
  - `ControladorReinas`: Conecta las operaciones del modelo con la vista

## 🚀 Instalación

### Requisitos
- Python 3.7 o superior

### Clonar el repositorio
```bash
git clone https://github.com/Valenbu/Problema8Reinas.git
cd Problema8Reinas
```

No se requieren dependencias externas, solo Python estándar.

## 💻 Uso

### Ejecutar el programa
```bash
python main.py
```

### Ejemplo de uso
```
Problema de las 8 reinas - Proyecto MVC

Ingrese fila inicial (0-7): 0
Ingrese columna inicial (0-7): 0

Total de soluciones encontradas: 1

Solución #1
 ♛  .  .  .  .  .  .  . 
 .  .  .  .  ♛  .  .  . 
 .  .  .  .  .  .  .  ♛ 
 .  .  .  .  .  ♛  .  . 
 .  .  ♛  .  .  .  .  . 
 .  .  .  .  .  .  ♛  . 
 .  ♛  .  .  .  .  .  . 
 .  .  .  ♛  .  .  .  . 
```

## 🧠 Algoritmo

El proyecto utiliza **backtracking** para encontrar todas las soluciones posibles:

1. El usuario especifica una posición inicial (fila, columna)
2. Se coloca la primera reina en esa posición (fija)
3. Se intenta colocar las 7 reinas restantes en las demás filas
4. Para cada fila, se prueban todas las columnas posibles
5. Se verifica que la nueva posición sea segura (no amenace a otras reinas)
6. Si se encuentra una solución válida, se guarda
7. Se retrocede (backtrack) para encontrar más soluciones

### Complejidad
- **Tiempo**: O(n!) en el peor caso
- **Espacio**: O(n) para la recursión

## 📊 Estructuras de Datos Utilizadas

### 1. **Listas (Lists)**
Las listas son la estructura principal usada en Python:

```python
# Lista de soluciones (lista de listas)
soluciones = []

# Lista de reinas en una solución
reinas_actuales = [Reina(0,0), Reina(1,3), ...]

# Lista de filas disponibles
filas_para_colocar = [1, 2, 3, 4, 5, 6, 7]
```

**¿Por qué listas?**
- Orden secuencial (importante para el algoritmo)
- Acceso rápido por índice: O(1)
- Fácil agregar/quitar elementos: `append()`, `pop()`
- Ideal para backtracking

### 2. **No se usan colas ni pilas explícitas**
El proyecto **NO** utiliza estructuras de cola (Queue) o pila (Stack) explícitas, aunque:
- La **recursión** del backtracking usa implícitamente la pila de llamadas
- Las listas con `append()` y `pop()` simulan comportamiento de pila

### 3. **Objetos (Reina)**
```python
class Reina:
    def __init__(self, fila, columna):
        self._fila = fila
        self._columna = columna
```
Encapsulan datos relacionados (fila y columna).

## 🔍 ¿Cómo funciona el backtracking?

```python
def _backtrack_filas(filas, indice, reinas):
    # Caso base: solución completa
    if len(reinas) == 8:
        guardar_solucion()
        return
    
    # Probar cada columna en la fila actual
    for col in range(8):
        if es_seguro(fila, col, reinas):
            reinas.append(nueva_reina)  # Probar
            backtrack(indice + 1)       # Recursión
            reinas.pop()                # Retroceder
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Haz un fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👤 Autor

**Valenbu**
- GitHub: [@Valenbu](https://github.com/Valenbu)

## 🙏 Agradecimientos

- Basado en el clásico problema de las N reinas
- Implementado como proyecto educativo para aprender MVC y algoritmos de backtracking

---

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub!

👤 Autor
Valentina Burgos//Andres Moreno

🙏 Agradecimientos

Basado en el clásico problema de las N reinas
Implementado como proyecto educativo para aprender MVC y algoritmos de backtracking
