def fib(n):
    if n == 0:
        return 1
    elif n < 2 and n != 0:
        return n
    n0 = 0
    n1 = 1
    fib = 0
    for i in range(n):
        fib = n0 + n1
        n0 = n1
        n1 = fib
    return fib

for c in range(43):
    print(f"第 {c} 階有 {fib(c)} 種可能")
