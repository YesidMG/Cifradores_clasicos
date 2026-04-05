from auxiliaryFunctions.auxiliaryFunctions import find_in_matrix
from auxiliaryFunctions.standardization import alphabetMatrix, prepare_key

# ---------------- Método César (Desencriptación) ----------------

def cesar_decrypt(message, key):
    """Decifra el mensaje usando el método César."""
    
    nKey = prepare_key(message, key)  # Preparar la clave para que coincida con la longitud del mensaje
    resultado = ""

    cols = len(alphabetMatrix[0])
    total = len(alphabetMatrix) * cols

    for i, char in enumerate(message):
        pos_m = find_in_matrix(char)
        pos_k = find_in_matrix(nKey[i])

        row_m, col_m = pos_m
        row_k, col_k = pos_k

        new_col = (((row_m * cols + col_m) - (row_k * cols + col_k)) % total) % cols
        new_row = (((row_m * cols + col_m) - (row_k * cols + col_k)) % total) // cols

        resultado += alphabetMatrix[new_row][new_col]

    return resultado

# ---------------- Método Polibio (Desencriptación) ----------------

def polibio_decrypt(message, mode='strict'):
    """Desencripta el mensaje usando el método Polibio con normalización strict o lax."""
    resultado = ""
    i = 0

    while i < len(message):
        if i + 1 < len(message) and message[i].isdigit() and message[i + 1].isdigit():
            # Tomar dos dígitos consecutivos como fila y columna
            row = int(message[i])
            col = int(message[i + 1])
            resultado += alphabetMatrix[row][col]
            i += 2  # Avanzar dos posiciones
        else:
            # Si no es un par válido, agregar el carácter tal cual
            resultado += message[i]
            i += 1

    return resultado

# ---------------- Método de Transposición (Desencriptación) ----------------

def transposicion_decrypt(message, key):
    n = len(message)
    
    # Cantidad real de pares e impares
    pares_len = (n + 1) // 2   # incluye el índice 0
    impares_len = n // 2

    # Separar correctamente según la llave
    if len(key) % 2 == 0:
        # llave par → pares al final
        impares = message[:impares_len]
        pares = message[impares_len:]
    else:
        # llave impar → impares al final
        pares = message[:pares_len]
        impares = message[pares_len:]

    # Reconstrucción
    resultado = []
    par_idx = 0
    impar_idx = 0

    for i in range(n):
        if i % 2 == 0:
            resultado.append(pares[par_idx])
            par_idx += 1
        else:
            resultado.append(impares[impar_idx])
            impar_idx += 1

    return "".join(resultado)
