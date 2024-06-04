# Gestión de Tablas de Multiplicar y Listín Telefónico

Este proyecto en Python incluye varias funcionalidades que permiten trabajar con tablas de multiplicar y gestionar un listín telefónico. A continuación, se describen los diferentes ejercicios implementados y cómo utilizar el programa.

## Ejercicios

### Ejercicio 1: Guardar tabla de multiplicar

Escribir una función que pida un número entero entre 1 y 10 y guarde en un archivo con el nombre `tabla-n.txt` la tabla de multiplicar de ese número, donde `n` es el número introducido.

### Ejercicio 2: Leer tabla de multiplicar

Escribir una función que pida un número entero entre 1 y 10, lea el archivo `tabla-n.txt` con la tabla de multiplicar de ese número, donde `n` es el número introducido, y la muestre por pantalla. Si el archivo no existe, debe mostrar un mensaje por pantalla informando de ello.

### Ejercicio 3: Leer línea específica de la tabla de multiplicar

Escribir una función que pida dos números `n` y `m` entre 1 y 10, lea el archivo `tabla-n.txt` con la tabla de multiplicar de ese número, y muestre por pantalla la línea `m` del archivo. Si el archivo no existe, debe mostrar un mensaje por pantalla informando de ello.

### Ejercicio 4: Gestión de Listín Telefónico

Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa. El programa incorpora funciones para:
- Crear el archivo con el listín si no existe.
- Consultar el teléfono de un cliente.
- Añadir el teléfono de un nuevo cliente.
- Eliminar el teléfono de un cliente.

El listín debe estar guardado en el archivo de texto `listin.txt`, donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.

## Instrucciones de Uso

1. **Clonar el repositorio** (si aplica) o copiar el código en un archivo Python (`main.py`).
2. **Ejecutar el programa** desde la consola con el siguiente comando:
    ```sh
    python main.py
    ```
3. **Menú Principal**:
    - `1`: Guardar tabla de multiplicar.
    - `2`: Leer tabla de multiplicar.
    - `3`: Leer línea específica de tabla de multiplicar.
    - `4`: Crear/gestionar listín telefónico.
    - `5`: Salir.

4. **Submenú Listín Telefónico**:
    - `1`: Crear listín (si no existe).
    - `2`: Consultar teléfono de un cliente.
    - `3`: Añadir cliente.
    - `4`: Eliminar cliente.
    - `5`: Volver al menú principal.

## Ejemplos de Uso

### Ejercicio 1
Introduce un número entre 1 y 10. La tabla de multiplicar de ese número se guardará en un archivo `tabla-n.txt`.

### Ejercicio 2
Introduce un número entre 1 y 10. El programa leerá y mostrará la tabla de multiplicar desde el archivo `tabla-n.txt`. Si el archivo no existe, se mostrará un mensaje de error.

### Ejercicio 3
Introduce dos números `n` y `m` entre 1 y 10. El programa leerá la línea `m` de la tabla de multiplicar del archivo `tabla-n.txt`. Si el archivo no existe o la línea no está disponible, se mostrará un mensaje de error.

### Ejercicio 4
Gestiona un listín telefónico:
- Crear el archivo `listin.txt` si no existe.
- Consultar el teléfono de un cliente.
- Añadir un nuevo cliente al listín.
- Eliminar un cliente del listín.

## Requisitos

- Python 3.x

## Autor

Creado por [Tu Nombre]

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
