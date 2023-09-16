import sys


def ingestaDeDatos(nombreArchivo):
    try:
        with open(nombreArchivo, 'r') as data_file:
            while True:
                line = data_file.readline().strip()
                if not line:
                    break

                n = int(line)

                # Skipping the blank line before the flow matrix
                data_file.readline()

                # Reading the flow matrix
                flujo = [list(map(int, data_file.readline().split())) for _ in range(n)]

                # Skipping the blank line before the distance matrix
                data_file.readline()

                # Reading the distance matrix
                distancias = [list(map(int, data_file.readline().split())) for _ in range(n)]

                print("Tamanno:", n)
                print("Matriz de flujo:")
                for fila in flujo:
                    print(" ".join(map(str, fila)))
                print("\nMatriz de distancias:")
                for fila in distancias:
                    print(" ".join(map(str, fila)))
                print("----------------------------------")

                # Skipping the blank line after the distance matrix to get ready for the next data set
                data_file.readline()

    except FileNotFoundError:
        print(f"No se pudo abrir el archivo {nombreArchivo}.")
        return 1

    return 0


def main():
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} <nombre del archivo de parametros>")
        return 1

    try:
        with open(sys.argv[1], 'r') as param_file:
            params = {}
            for line in param_file:
                key, value = [s.strip() for s in line.split('=')]
                params[key] = value

            if params.get("otros_parametros") == "ingesta":
                result = ingestaDeDatos(params.get("nombre_del_archivo"))
                if result != 0:
                    return result

    except FileNotFoundError:
        print(f"No se pudo abrir el archivo {sys.argv[1]}.")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
