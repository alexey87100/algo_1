def dec_to_bin(n: int) -> str:
    """Перевод в двоичную систему исчисления из десятичной."""
    s = ''
    while n != 0:
        s += str(n % 2)
        n //= 2
    s = s[:]
    return s


def bin_to_dec(s: str) -> int:
    """Перевод из двоичной системы в десятичную."""
    n = 0
    for num, symbol in enumerate(s):
        n += int(symbol)*2**(len(s)-num - 1)
    return n


def solve_contest_task():
    """Решение задачи из контеста с применением операции XOR."""
    result = 0
    for elem in input():
        result = result ^ ord(elem)
    for elem in input():
        result = result ^ ord(elem)
    print(chr(result))
