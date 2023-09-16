import sys


# Función para ingerir datos de un archivo dado
def ingestaDeDatos(nombreArchivo):
    # Intentando abrir y leer el archivo de datos
    try:
        with open(nombreArchivo, 'r') as data_file:
            while True:
                # Leyendo una línea del archivo y eliminando espacios en blanco al principio/final
                line = data_file.readline().strip()

                # Salir del bucle si la línea está vacía
                if not line:
                    break

                # Convirtiendo la línea a un entero
                n = int(line)

                # Leyendo y descartando la siguiente línea vacía
                data_file.readline()

                # Leyendo 'n' líneas para poblar la matriz 'flujo'
                flujo = [list(map(int, data_file.readline().split())) for _ in range(n)]

                # Leyendo y descartando la siguiente línea
                data_file.readline()

                # Leyendo 'n' líneas para poblar la matriz 'distancias'
                distancias = [list(map(int, data_file.readline().split())) for _ in range(n)]

                # Imprimiendo el tamaño y las matrices
                print("Tamaño:", n)
                print("Matriz de flujo:")
                for fila in flujo:
                    print(" ".join(map(str, fila)))
                print("\nMatriz de distancias:")
                for fila in distancias:
                    print(" ".join(map(str, fila)))
                print("----------------------------------")

                # Leyendo y descartando la siguiente línea
                data_file.readline()

    # Manejando el caso donde el archivo podría no encontrarse
    except FileNotFoundError:
        print(f"No se pudo abrir el archivo {nombreArchivo}")


# Verificando si este script se está ejecutando como el módulo principal
if __name__ == "__main__":
    # Verificando si el script recibió el número requerido de argumentos de línea de comando
    if len(sys.argv) != 2:
        print("Uso: python main.py <nombre del archivo>")
    else:
        # Llamando a la función ingestaDeDatos con el nombre de archivo proporcionado
        ingestaDeDatos(sys.argv[1])
