import sys


# Función para ingerir datos de un archivo dado
def ingestaDeDatos(nombreArchivo):
    try:
        with open(nombreArchivo, 'r') as data_file:
            lines = data_file.read().splitlines()  # Lee todas las líneas a la vez
            i = 0
            while i < len(lines):
                if not lines[i]:  # Ignorar líneas vacías
                    i += 1
                    continue

                n = int(lines[i])
                i += 1

                flujo = [list(map(int, lines[j].split())) for j in range(i, i + n)]
                i += n + 1  # Saltar una línea adicional para pasar a la matriz de distancias

                distancias = [list(map(int, lines[j].split())) for j in range(i, i + n)]
                i += n + 1  # Saltar una línea adicional para el siguiente conjunto o fin de archivo

                # Imprime el tamaño y las matrices
                print("Tamaño:", n)
                print("Matriz de flujo:")
                for fila in flujo:
                    print(" ".join(map(str, fila)))
                print("\nMatriz de distancias:")
                for fila in distancias:
                    print(" ".join(map(str, fila)))
                print("----------------------------------")
        return 1
    except Exception as e:
        print(f"Error al procesar el archivo {nombreArchivo}: {e}")
        return 0


def lecturaParametros(nombre_archivo: str) -> int:
    try:
        with open(nombre_archivo, 'r') as param_file:
            parametros = {}
            for line in param_file:
                if '=' in line:
                    key, value = line.split('=')
                    key = key.strip()
                    value = value.strip()
                    parametros[key] = value

        if parametros.get("otros_parametros") == "ingesta":
            result = ingestaDeDatos(parametros["nombre_del_archivo"])
            if result != 0:
                return result

        return 0

    except FileNotFoundError:
        print(f"No se pudo abrir el archivo {nombre_archivo}.")
        return 1


if __name__ == "__main__":
    # Verificando si el script recibió el número requerido de argumentos de línea de comando
    if len(sys.argv) != 2:
        print("Uso: python main.py <nombre del archivo>")

    archivoParametros = sys.argv[1]

    lecturaParametros(archivoParametros)
