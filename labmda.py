print((lambda a, b, c: "WIN" if a%2 == b%2 == c%2 else "FAIL")(*map(int, input().split())))