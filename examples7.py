from typing import Iterable, Any
from bisect import insort


def test_list():
    """Работа со списками."""
    a = []
    a.append(1)
    a.append(10)
    a.append(3)
    a.append(12)

    a.sort()

    insort(a, 2)
    max(a)
    print(1 in a)


def test_set():
    """Работа с множествами"""
    s = set()
    s.add('1')
    s.add('3')
    s.add('2')
    max(s)
    print('1' in s)


def find_max(data: Iterable) -> Any:
    """Поиск наибольшего элемента."""
    max_elem = float("-inf")
    for elem in data:
        max_elem = max(elem, max_elem)
    return max_elem


def find_extremum(data: Iterable, ext_func=max) -> Any:
    """Поиск наибольшего или наименьшего значения."""
    extremum = data[0] if len(data) > 0 else None
    for elem in data:
        extremum = ext_func(elem, extremum)
    return extremum


def swap(data: list, ind_1: int, ind_2: int) -> None:
    """Смена местами двух элементов списка."""
    buffer = data[ind_1]
    data[ind_1] = data[ind_2]
    data[ind_2] = buffer


def bubble_sort(data: list) -> None:
    """Сортировка пузырьком."""
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] > data[j]:
                swap(data, i, j)


def is_sequence_sorted(data: Iterable) -> bool:
    """Проверяет, отсортирована ли последовательность по возрастанию."""
    for i in range(len(data) - 1):
        if data[i + 1] < data[i]:
            return False
    return True


def god_sort(data: list) -> int:
    """Сортировка Бога."""
    from random import shuffle

    attempt_num = 0
    if is_sequence_sorted(data):
        return attempt_num
    while not is_sequence_sorted(data):
        shuffle(data)
        attempt_num += 1
    return attempt_num


if __name__ == '__main__':
    print(god_sort([1, 4, 2, 5, 23, 5, 38, 7, 10, 123]))