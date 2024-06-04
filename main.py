import os

# Ejercicio 1
def guardar_tabla_multiplicar():
    numero = int(input("Introduce un número entero entre 1 y 10: "))
    if 1 <= numero <= 10:
        with open(f'tabla-{numero}.txt', 'w') as archivo:
            for i in range(1, 11):
                archivo.write(f'{numero} x {i} = {numero * i}\n')
        print(f'Tabla del {numero} guardada en tabla-{numero}.txt')
    else:
        print("El número debe estar entre 1 y 10.")

# Ejercicio 2
def leer_tabla_multiplicar():
    numero = int(input("Introduce un número entero entre 1 y 10: "))
    if 1 <= numero <= 10:
        try:
            with open(f'tabla-{numero}.txt', 'r') as archivo:
                print(archivo.read())
        except FileNotFoundError:
            print(f'El archivo tabla-{numero}.txt no existe.')
    else:
        print("El número debe estar entre 1 y 10.")

# Ejercicio 3
def leer_linea_tabla_multiplicar():
    n = int(input("Introduce el primer número (n) entre 1 y 10: "))
    m = int(input("Introduce el segundo número (m) entre 1 y 10: "))
    if 1 <= n <= 10 and 1 <= m <= 10:
        try:
            with open(f'tabla-{n}.txt', 'r') as archivo:
                lineas = archivo.readlines()
                if 1 <= m <= len(lineas):
                    print(lineas[m-1].strip())
                else:
                    print(f'El archivo tabla-{n}.txt no tiene {m} líneas.')
        except FileNotFoundError:
            print(f'El archivo tabla-{n}.txt no existe.')
    else:
        print("Ambos números deben estar entre 1 y 10.")

# Ejercicio 4
def crear_listin():
    if not os.path.exists('listin.txt'):
        with open('listin.txt', 'w') as archivo:
            print('Archivo listin.txt creado.')
    else:
        print('El archivo listin.txt ya existe.')

def consultar_telefono():
    nombre = input("Introduce el nombre del cliente: ")
    try:
        with open('listin.txt', 'r') as archivo:
            for linea in archivo:
                if linea.startswith(nombre + ','):
                    print(f'Teléfono de {nombre}: {linea.split(",")[1].strip()}')
                    return
            print(f'Cliente {nombre} no encontrado.')
    except FileNotFoundError:
        print('El archivo listin.txt no existe.')

def anadir_cliente():
    nombre = input("Introduce el nombre del nuevo cliente: ")
    telefono = input("Introduce el teléfono del nuevo cliente: ")
    with open('listin.txt', 'a') as archivo:
        archivo.write(f'{nombre},{telefono}\n')
    print(f'Cliente {nombre} añadido con teléfono {telefono}.')

def eliminar_cliente():
    nombre = input("Introduce el nombre del cliente a eliminar: ")
    try:
        with open('listin.txt', 'r') as archivo:
            lineas = archivo.readlines()
        with open('listin.txt', 'w') as archivo:
            encontrado = False
            for linea in lineas:
                if not linea.startswith(nombre + ','):
                    archivo.write(linea)
                else:
                    encontrado = True
            if encontrado:
                print(f'Cliente {nombre} eliminado.')
            else:
                print(f'Cliente {nombre} no encontrado.')
    except FileNotFoundError:
        print('El archivo listin.txt no existe.')

# Programa principal para gestionar los ejercicios
def main():
    while True:
        print("\nMenu:")
        print("1. Guardar tabla de multiplicar")
        print("2. Leer tabla de multiplicar")
        print("3. Leer línea específica de tabla de multiplicar")
        print("4. Crear/gestionar listín telefónico")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            guardar_tabla_multiplicar()
        elif opcion == '2':
            leer_tabla_multiplicar()
        elif opcion == '3':
            leer_linea_tabla_multiplicar()
        elif opcion == '4':
            while True:
                print("\nSubmenu Listín Telefónico:")
                print("1. Crear listín")
                print("2. Consultar teléfono")
                print("3. Añadir cliente")
                print("4. Eliminar cliente")
                print("5. Volver al menú principal")
                subopcion = input("Elige una opción: ")

                if subopcion == '1':
                    crear_listin()
                elif subopcion == '2':
                    consultar_telefono()
                elif subopcion == '3':
                    anadir_cliente()
                elif subopcion == '4':
                    eliminar_cliente()
                elif subopcion == '5':
                    break
                else:
                    print("Opción no válida. Inténtalo de nuevo.")
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
