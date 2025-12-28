from typing import List, TypeVar, Union

MatrixData = List[List[float]]
Scalar = Union[int, float]

def create_matrix(data: MatrixData) -> MatrixData:
    """Создание матрицы из двумерного списка."""
    if not data:
        raise ValueError("Матрица не может быть пустой")
    
    rows = len(data)
    cols = len(data[0]) if rows > 0 else 0
    
    for row in data:
        if len(row) != cols:
            raise ValueError("Все строки матрицы должны иметь одинаковую длину")
    
    return [row[:] for row in data]  # Возвращаем копию

def get_dimensions(matrix: MatrixData) -> tuple[int, int]:
    """Получение размеров матрицы."""
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    return rows, cols

def add_matrices(m1: MatrixData, m2: MatrixData) -> MatrixData:
    """Сложение двух матриц."""
    rows1, cols1 = get_dimensions(m1)
    rows2, cols2 = get_dimensions(m2)
    
    if rows1 != rows2 or cols1 != cols2:
        raise ValueError("Матрицы должны иметь одинаковые размеры для сложения")
    
    result = []
    for i in range(rows1):
        row = []
        for j in range(cols1):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)
    
    return result

def multiply_matrices(m1: MatrixData, m2: MatrixData) -> MatrixData:
    """Умножение двух матриц."""
    rows1, cols1 = get_dimensions(m1)
    rows2, cols2 = get_dimensions(m2)
    
    if cols1 != rows2:
        raise ValueError("Количество столбцов первой матрицы должно совпадать с количеством строк второй")
    
    result = [[0.0] * cols2 for _ in range(rows1)]
    
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += m1[i][k] * m2[k][j]
    
    return result

def multiply_by_scalar(matrix: MatrixData, scalar: Scalar) -> MatrixData:
    """Умножение матрицы на скаляр."""
    rows, cols = get_dimensions(matrix)
    
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix[i][j] * scalar)
        result.append(row)
    
    return result

def transpose_matrix(matrix: MatrixData) -> MatrixData:
    """Транспонирование матрицы."""
    rows, cols = get_dimensions(matrix)
    
    result = [[0.0] * rows for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    
    return result

def matrix_to_string(matrix: MatrixData) -> str:
    """Преобразование матрицы в строку для вывода."""
    if not matrix:
        return "[]"
    
    rows, cols = get_dimensions(matrix)
    max_len = 0
    for row in matrix:
        for val in row:
            max_len = max(max_len, len(f"{val:.2f}"))
    
    result = []
    for i, row in enumerate(matrix):
        if i == 0:
            prefix = "⎡"
            suffix = "⎤"
        elif i == rows - 1:
            prefix = "⎣"
            suffix = "⎦"
        else:
            prefix = "⎢"
            suffix = "⎥"
        
        formatted = [f"{val:>{max_len}.2f}" for val in row]
        result.append(f"{prefix} {' '.join(formatted)} {suffix}")
    
    return "\n".join(result)