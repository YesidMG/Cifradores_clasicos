from auxiliaryFunctions.auxiliaryFunctions import find_in_matrix
from auxiliaryFunctions.standardization import alphabetMatrix, normalize, prepare_key

# ---------------- Método César ----------------

def cesar(message, mode, key):
    """Cifra el mensaje usando el método César con normalización strict o lax.
    El desplazamiento n se calcula en función de la cantidad de caracteres del mensaje."""
    
    nMessage = normalize(message, mode)  # Normalizar el mensaje según el modo
    nKey = prepare_key(nMessage, key)  # Preparar la clave para que coincida con la longitud del mensaje
    resultado = ""

    cols = len(alphabetMatrix[0])
    total = len(alphabetMatrix) * cols

    for i, char in enumerate(nMessage):
        pos_m = find_in_matrix(char)
        pos_k = find_in_matrix(nKey[i])

        row_m, col_m = pos_m
        row_k, col_k = pos_k

        new_col = (((row_m * cols + col_m) + (row_k * cols + col_k)) % total) % cols
        new_row = (((row_m * cols + col_m) + (row_k * cols + col_k)) % total) // cols

        resultado += alphabetMatrix[new_row][new_col]

    return resultado

# ---------------- Método Polibio ----------------

def polibio(message, mode):
    """Cifra el mensaje usando el método Polibio con normalización strict o lax."""
    nMessage = normalize(message, mode)  # Normalizar el mensaje según el modo

    resultado = ""
    for char in nMessage:
        position = find_in_matrix(char)
        if position:  # Si el carácter está en la matriz
            row, col = position
            resultado += f"{row}{col}"  # Codifica como fila y columna
        else:
            resultado += char  # Si no está en la matriz, se deja igual

    return resultado

# ---------------- Método de Transposición ----------------

def transposicion(message, mode, key):
    """Cifra el mensaje usando el método de transposición con normalización strict o lax.
    Si la llave normalizada tiene largo par, lleva los caracteres en posición par al final.
    Si la llave normalizada tiene largo impar, lleva los caracteres en posición impar al final."""
    
    nMessage = normalize(message, mode)  # Normalizar el mensaje según el modo
    
    pares = ""
    impares = ""

    for idx, char in enumerate(nMessage):
        if idx % 2 == 0:  # Índices pares
            pares += char
        else:  # Índices impares
            impares += char

    # Si el largo de la llave es par, pares van al final
    # Si el largo de la llave es impar, impares van al final
    if len(key) % 2 == 0:
        return impares + pares  # Pares al final
    else:
        return pares + impares  # Impares al final

