from typing import List


def dfs(matrix: List[List[str]], row: int, col: int) -> None:
    """Выполняет поиск в глубину для поиска островов в матрице."""
    if (row < 0 or col < 0 or row >= len(matrix)
       or col >= len(matrix[0]) or matrix[row][col] != '1'):
        return
    matrix[row][col] = '2'
    dfs(matrix, row + 1, col)
    dfs(matrix, row - 1, col)
    dfs(matrix, row, col + 1)
    dfs(matrix, row, col - 1)


def get_input() -> List[List[str]]:
    """
    Запрашивает у пользователя ввод матрицы и возвращает его
    в виде списка списков символов.
    Количество символов в строках должны быть одной длины.
    """
    matrix = []
    while True:
        row = input()
        if not row:
            break
        matrix.append([item for item in row])
    return matrix


def main() -> None:
    """
    Основная функция программы, выполняет поиск островов в
    матрице и возвращает их количество.
    """
    matrix = get_input()
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == '1':
                dfs(matrix, row, col)
                count += 1
    return count


if __name__ == '__main__':
    print(main())
