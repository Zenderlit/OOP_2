from matrix_oop import Matrix
from functional_matrix import (
    create_matrix, add_matrices, multiply_matrices,
    multiply_by_scalar, transpose_matrix, matrix_to_string
)

def demo_oop_style() -> None:
    """Демонстрация ООП стиля."""
    print("=" * 50)
    print("ООП СТИЛЬ")
    print("=" * 50)
    
    # Создание матриц
    m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    m3 = Matrix([[1, 2], [3, 4]])
    
    print(f"Матрица m1:\n{m1}")
    print(f"\nМатрица m2:\n{m2}")
    
    # Сложение матриц
    m_sum = m1 + m2
    print(f"\nm1 + m2:\n{m_sum}")
    
    # Умножение матриц
    m4 = Matrix([[1, 2], [3, 4], [5, 6]])
    m5 = Matrix([[7, 8], [9, 10]])
    m_mul = m4 * m5
    print(f"\nm4 * m5:\n{m_mul}")
    
    # Умножение на скаляр
    m_scaled = m1 * 2
    print(f"\nm1 * 2:\n{m_scaled}")
    
    # Транспонирование
    m_transposed = m1.transpose()
    print(f"\nТранспонированная m1:\n{m_transposed}")
    
    # Определитель
    det = m3.determinant()
    print(f"\nОпределитель m3: {det:.2f}")

def demo_functional_style() -> None:
    """Демонстрация функционального стиля."""
    print("\n" + "=" * 50)
    print("ФУНКЦИОНАЛЬНЫЙ СТИЛЬ")
    print("=" * 50)
    
    # Создание матриц
    m1 = create_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m2 = create_matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    
    print(f"Матрица m1:\n{matrix_to_string(m1)}")
    print(f"\nМатрица m2:\n{matrix_to_string(m2)}")
    
    # Сложение матриц
    m_sum = add_matrices(m1, m2)
    print(f"\nm1 + m2:\n{matrix_to_string(m_sum)}")
    
    # Умножение матриц
    m3 = create_matrix([[1, 2], [3, 4], [5, 6]])
    m4 = create_matrix([[7, 8], [9, 10]])
    m_mul = multiply_matrices(m3, m4)
    print(f"\nm3 * m4:\n{matrix_to_string(m_mul)}")
    
    # Умножение на скаляр
    m_scaled = multiply_by_scalar(m1, 2)
    print(f"\nm1 * 2:\n{matrix_to_string(m_scaled)}")
    
    # Транспонирование
    m_transposed = transpose_matrix(m1)
    print(f"\nТранспонированная m1:\n{matrix_to_string(m_transposed)}")

def main() -> None:
    """Основная функция демонстрации."""
    print("Лабораторная работа 2: Матрицы")
    print("Реализация в двух парадигмах: ООП и функциональной\n")
    
    demo_oop_style()
    demo_functional_style()

if __name__ == "__main__":
    main()