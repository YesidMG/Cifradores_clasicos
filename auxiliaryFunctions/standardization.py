# Matriz del alfabeto
alphabetMatrix = [
    [' ', '.', ':', ',', 'm', 'n', 'b', 'v', 'c'],
    ['x', 'z', 'ñ', 'l', 'k', 'j', 'h', 'g', 'f'],
    ['d', 's', 'a', 'p', 'o', 'i', 'u', 'y', 't'],
    ['r', 'e', 'w', 'q', '0', '9', '8', '7', '6'],
    ['5', '4', '3', '2', '1', 'Q', 'W', 'E', 'R'],
    ['T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D'],
    ['F', 'G', 'H', 'J', 'K', 'L', 'Ñ', 'Z', 'X'],
    ['C', 'V', 'B', 'N', 'M', '¡', '!', '¿', '?'],
]

# ---------------- Normalización ----------------

def remove_accents(text):
    """Elimina las tildes de las vocales reemplazándolas por su equivalente sin tilde."""
    accents = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'
    }
    return ''.join(accents[char] if char in accents else char for char in text)

def normalize_strict(text):
    """Aplica normalización strict: elimina caracteres no alfabéticos y espacios, convierte a minúsculas, y elimina tildes."""
    text = remove_accents(text)  # Eliminar tildes
    return ''.join(char.lower() for char in text if char.isalpha())

def normalize_lax(text):
    """Aplica normalización lax: conserva solo los caracteres que están en la alphabetMatrix, y elimina tildes."""
    text = remove_accents(text)  # Eliminar tildes
    valid_chars = {char for row in alphabetMatrix for char in row}  # Conjunto de caracteres válidos en la matriz
    return ''.join(char for char in text if char in valid_chars)

def normalize(text, mode):
    """Normaliza el texto según el modo especificado (strict o lax)."""
    if mode == 'strict':
        return normalize_strict(text)
    elif mode == 'lax':
        return normalize_lax(text)
    else:
        raise ValueError("Modo de normalización no válido. Use 'strict' o 'lax'.")
    
def prepare_key(message, key):
    """Prepara la clave para el método de cesar, asegurando que sea un número válido basado en el mensaje.
    Si la llave es de longitud menor al mensaje normalizado, se repite hasta alcanzar la longitud del mensaje.
    Si la llave es de longitud mayor al mensaje normalizado, se recorta para que coincida con la longitud del mensaje."""

    nKey = normalize(key, 'lax')
    
    if len(nKey) == len(message):
        return nKey

    elif len(nKey) < len(message):
        # repetir y luego recortar
        return (nKey * (len(message) // len(nKey) + 1))[:len(message)]

    else:
        # recortar
        return nKey[:len(message)]