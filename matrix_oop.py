from typing import List, Union, overload
import copy

Scalar = Union[int, float]

class Matrix:
    """Класс матрицы с поддержкой основных операций."""
    
    def __init__(self, data: List[List[Scalar]]) -> None:
        """Инициализация матрицы."""
        if not data:
            raise ValueError("Матрица не может быть пустой")
        
        self._rows = len(data)
        self._cols = len(data[0]) if self._rows > 0 else 0
        
        # Проверяем, что все строки имеют одинаковую длину
        for row in data:
            if len(row) != self._cols:
                raise ValueError("Все строки матрицы должны иметь одинаковую длину")
        
        self._data = [list(row) for row in data]
    
    @property
    def rows(self) -> int:
        """Количество строк."""
        return self._rows
    
    @property
    def cols(self) -> int:
        """Количество столбцов."""
        return self._cols
    
    @property
    def shape(self) -> tuple[int, int]:
        """Размерность матрицы (строки, столбцы)."""
        return (self._rows, self._cols)
    
    def __getitem__(self, index: int) -> List[Scalar]:
        """Получение строки матрицы."""
        return self._data[index]
    
    def __setitem__(self, index: int, value: List[Scalar]) -> None:
        """Установка строки матрицы."""
        if len(value) != self._cols:
            raise ValueError(f"Строка должна содержать {self._cols} элементов")
        self._data[index] = list(value)
    
    def __repr__(self) -> str:
        """Строковое представление матрицы."""
        return f"Matrix({self._data})"
    
    def __str__(self) -> str:
        """Красивый вывод матрицы."""
        if not self._data:
            return "[]"
        
        # Находим максимальную длину элемента для форматирования
        max_len = 0
        for row in self._data:
            for val in row:
                max_len = max(max_len, len(f"{val:.2f}"))
        
        result = []
        for i, row in enumerate(self._data):
            if i == 0:
                prefix = "⎡"
                suffix = "⎤"
            elif i == self._rows - 1:
                prefix = "⎣"
                suffix = "⎦"
            else:
                prefix = "⎢"
                suffix = "⎥"
            
            formatted = [f"{val:>{max_len}.2f}" for val in row]
            result.append(f"{prefix} {' '.join(formatted)} {suffix}")
        
        return "\n".join(result)
    
    def __eq__(self, other: object) -> bool:
        """Проверка на равенство матриц."""
        if not isinstance(other, Matrix):
            return False
        
        if self.shape != other.shape:
            return False
        
        for i in range(self._rows):
            for j in range(self._cols):
                if self._data[i][j] != other._data[i][j]:
                    return False
        
        return True
    
    def __add__(self, other: 'Matrix') -> 'Matrix':
        """Сложение матриц."""
        if not isinstance(other, Matrix):
            raise TypeError("Можно складывать только матрицы")
        
        if self.shape != other.shape:
            raise ValueError("Матрицы должны иметь одинаковые размеры для сложения")
        
        result_data = []
        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                row.append(self._data[i][j] + other._data[i][j])
            result_data.append(row)
        
        return Matrix(result_data)
    
    def __mul__(self, other: Union['Matrix', Scalar]) -> 'Matrix':
        """Умножение матрицы на матрицу или скаляр."""
        if isinstance(other, (int, float)):
            # Умножение на скаляр
            result_data = []
            for i in range(self._rows):
                row = []
                for j in range(self._cols):
                    row.append(self._data[i][j] * other)
                result_data.append(row)
            return Matrix(result_data)
        
        elif isinstance(other, Matrix):
            # Умножение матриц
            if self._cols != other._rows:
                raise ValueError("Количество столбцов первой матрицы должно совпадать с количеством строк второй")
            
            result_data = [[0.0] * other._cols for _ in range(self._rows)]
            
            for i in range(self._rows):
                for j in range(other._cols):
                    for k in range(self._cols):
                        result_data[i][j] += self._data[i][k] * other._data[k][j]
            
            return Matrix(result_data)
        else:
            raise TypeError(f"Неподдерживаемый тип для умножения: {type(other)}")
    
    def __rmul__(self, other: Scalar) -> 'Matrix':
        """Умножение скаляра на матрицу (справа)."""
        if isinstance(other, (int, float)):
            return self * other
        raise TypeError(f"Неподдерживаемый тип для умножения: {type(other)}")
    
    def transpose(self) -> 'Matrix':
        """Транспонирование матрицы."""
        result_data = [[0.0] * self._rows for _ in range(self._cols)]
        
        for i in range(self._rows):
            for j in range(self._cols):
                result_data[j][i] = self._data[i][j]
        
        return Matrix(result_data)
    
    def determinant(self) -> float:
        """Вычисление определителя матрицы (только для квадратных матриц)."""
        if self._rows != self._cols:
            raise ValueError("Определитель можно вычислить только для квадратной матрицы")
        
        n = self._rows
        data = copy.deepcopy(self._data)
        
        # Приводим матрицу к треугольному виду методом Гаусса
        det = 1.0
        for i in range(n):
            # Ищем максимальный элемент в столбце
            max_row = i
            for k in range(i + 1, n):
                if abs(data[k][i]) > abs(data[max_row][i]):
                    max_row = k
            
            # Меняем строки местами
            if max_row != i:
                data[i], data[max_row] = data[max_row], data[i]
                det *= -1
            
            # Если диагональный элемент равен 0, определитель равен 0
            if abs(data[i][i]) < 1e-10:
                return 0.0
            
            det *= data[i][i]
            
            # Обнуляем элементы ниже диагонали
            for k in range(i + 1, n):
                factor = data[k][i] / data[i][i]
                for j in range(i + 1, n):
                    data[k][j] -= factor * data[i][j]
        
        return det