# Definir el tamaño de la cuadrícula por input
N = int(input("Tamaño de la cuadrícula: "))

# Posición de la reina
fila_reina = int(input("Fila de la reina (0 a {}): ".format(N - 1)))
columna_reina = int(input("Columna de la reina (0 a {}): ".format(N - 1)))

# Bloqueos
fila_bloqueo1 = int(input("Fila del primer bloqueo (0 a {}): ".format(N - 1)))
columna_bloqueo1 = int(input("Columna del primer bloqueo (0 a {}): ".format(N - 1)))

fila_bloqueo2 = int(input("Fila del segundo bloqueo (0 a {}): ".format(N - 1)))
columna_bloqueo2 = int(input("Columna del segundo bloqueo (0 a {}): ".format(N - 1)))

fila_bloqueo3 = int(input("Fila del tercer bloqueo (0 a {}): ".format(N - 1)))
columna_bloqueo3 = int(input("Columna del tercer bloqueo (0 a {}): ".format(N - 1)))

# Guardar posiciones
reina = (fila_reina, columna_reina)
bloqueos = {
    (fila_bloqueo1, columna_bloqueo1),
    (fila_bloqueo2, columna_bloqueo2),
    (fila_bloqueo3, columna_bloqueo3)
}

# Direcciones de movimiento de la reina (8 direcciones)
direcciones = [
    (-1, 0), (1, 0),    # arriba, abajo
    (0, -1), (0, 1),    # izquierda, derecha
    (-1, -1), (-1, 1),  # diagonales arriba
    (1, -1), (1, 1)     # diagonales abajo
]

# Calcular posiciones válidas
posiciones_validas = []
for dx, dy in direcciones:
    x, y = reina
    while True:
        x += dx
        y += dy
        if not (0 <= x < N and 0 <= y < N):
            break  # Fuera de la cuadrícula
        if (x, y) in bloqueos:
            break  # Alguno de los bloqueos
        posiciones_validas.append((x, y))

# Mostrar resultados
print(f"La reina puede moverse a {len(posiciones_validas)} posiciones:")
print(posiciones_validas)
