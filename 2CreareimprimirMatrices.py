def imprimirMatriz(titulo, matriz):
    
    ancho = 1
    for fila in matriz:
        for valor in fila:
            if len(str(valor)) > ancho:
                ancho = len(str(valor))

    print(titulo)
    for fila in matriz:
        textos = []
        for valor in fila:
            textos.append(str(valor).rjust(ancho))
        print(" ".join(textos))
    print()



def matConsecutiva(n):
    matriz = []
    for f in range(n):
        fila = []
        for c in range(n):
            fila.append(f * n + c + 1)
        matriz.append(fila)
    return matriz


def matSubeBaja(n):
    matriz = []
    for f in range(n):
        fila = []
        for c in range(n):
            if f % 2 == 0:
                fila.append(c + 1)
            else:
                fila.append(n - c)
        matriz.append(fila)
    return matriz


def matDiagonalPrincipal(n):
    matriz = []
    for f in range(n):
        fila = []
        for c in range(n):
            if f == c:
                fila.append(1)
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz


def matDiagonalSecundaria(n):
    matriz = []
    for f in range(n):
        fila = []
        for c in range(n):
            if c == n - 1 - f:
                fila.append(1)
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz


def matTrianguloInferior(n):
    matriz = []
    for f in range(n):
        fila = []
        for c in range(n):
            if c <= f:
                fila.append(1)
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz


def matTrianguloSuperior(n):
    matriz = []
    for f in range(n):
        fila = []
        for c in range(n):
            if c >= f:
                fila.append(1)
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz


def matPorColumnas(n):
    matriz = []
    for f in range(n):
        fila = []
        for c in range(n):
            fila.append(c * n + f + 1)
        matriz.append(fila)
    return matriz

def matLetras(n):
    matriz = []
    for f in range(n):
        fila = []
        for c in range(n):
            if c <= f:
                if c % 2 == 0:
                    fila.append("A")
                else:
                    fila.append("B")
            else:
                fila.append("")
        matriz.append(fila)
    return matriz



n = int(input("Tamaño de las matrices cuadradas (n): "))
while n < 1:
    n = int(input("El tamaño debe ser mayor que 0. Intenta de nuevo: "))

print()
imprimirMatriz("Matriz 1 (consecutiva por filas):", matConsecutiva(n))
imprimirMatriz("Matriz 2 (filas que suben y bajan):", matSubeBaja(n))
imprimirMatriz("Matriz 3 (diagonal principal):", matDiagonalPrincipal(n))
imprimirMatriz("Matriz 4 (diagonal secundaria):", matDiagonalSecundaria(n))
imprimirMatriz("Matriz 5 (triángulo inferior):", matTrianguloInferior(n))
imprimirMatriz("Matriz 6 (triángulo superior):", matTrianguloSuperior(n))
imprimirMatriz("Matriz 7 (consecutiva por columnas):", matPorColumnas(n))
imprimirMatriz("Matriz 8 (letras A y B):", matLetras(n))
