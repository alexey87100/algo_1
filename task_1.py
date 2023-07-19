def get_input():
    data = list(map(int, input().split()))
    k = int(input())
    return data, k


def solution_1(data, k):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i]+data[j] == k:
                return True
    return False


def solution_2(data, k):
    s = set()
    for elem in data:
        if elem in s:
            return True
        s.add(k-elem)
    return False


def solution_3(data, k):
    i = 0
    j = len(data) - 1
    while i != j:
        result = data[i]+data[j]
        if result == k:
            return True
        if result > k:
            j -= 1
        else:
            i += 1
    return False


if __name__ == '__main__':
    print(solution_2([-10, -5, -3, -1, 0, 2, 3, 54, 656], 44))
    # print(solution_3(*get_input()))