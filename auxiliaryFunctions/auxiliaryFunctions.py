from auxiliaryFunctions.standardization import alphabetMatrix

def find_in_matrix(char):
    """Encuentra la posición (fila, columna) de un carácter en la matriz."""
    for row_idx, row in enumerate(alphabetMatrix):
        if char in row:
            return row_idx, row.index(char)
    return None

def char_to_linear_position(char):
    """Convierte un carácter a su posición lineal en la matriz (0-71)."""
    position = find_in_matrix(char)
    if position:
        row, col = position
        cols = len(alphabetMatrix[0])
        return row * cols + col
    return None

def linear_position_to_char(position):
    """Convierte una posición lineal (0-71) a su carácter en la matriz."""
    cols = len(alphabetMatrix[0])
    total = len(alphabetMatrix) * cols
    position = position % total
    row = position // cols
    col = position % cols
    return alphabetMatrix[row][col]