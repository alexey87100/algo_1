
def bin_search(data, k) -> bool:
    """Бинарный поиск."""
    left = 0
    right = len(data) - 1
    center = (left + right) // 2
    while data[center] != k:
        if k > data[center]:
            left = center + 1
        else:
            right = center - 1
        center = (left + right) // 2
        if left >= right:
            return False
    return True


def get_input() -> tuple:
    lines_num = int(input())
    data = []
    for _ in range(lines_num):
        data.append(list(map(int, input().split())))
    k = int(input())
    return data, k


def solution_1(data, k):
    """Решение №1
        Временная сложность O(len(data)**2)
        Пространственная сложность О(1)
    """
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == k:
                return True
    return False


def solution_2(data, k):
    """Решение №2
        Временная сложность O(len(data)*log(len(data)))
        Пространственная сложность О(1)
    """
    for i in range(len(data)):
        if bin_search(data[i], k):
            return True
    return False


def solution_3(data, k):
    """Решение №3
        Предлагается реализовать решение самостоятельно
        Основа реализации - диагональный поиск
        Временная сложность О(len(data))
        Пространственная О(1)
    """


if __name__ == '__main__':
    print(solution_2(*get_input()))
