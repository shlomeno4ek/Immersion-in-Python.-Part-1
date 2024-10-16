# Напишите функцию для транспонирования матрицы

# матрица для транспонирования
MATRIX = [
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4],
]


def main():
    print("Исходная матрица:")
    print_matrix(MATRIX)
    print("Транспонированная:")
    print_matrix(transpose_matrix(MATRIX))


def print_matrix(matrix: list[list]):
    """Вывод матрицы на экран"""
    for row in matrix:
        print(row)


def transpose_matrix(matrix: list[list]) -> list[list]:
    """Транспонирование матрицы"""
    new_matrix = [[] for _ in range(0, len(matrix[0]))]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            new_matrix[col].append(matrix[row][col])
    return new_matrix


if __name__ == "__main__":
    main()