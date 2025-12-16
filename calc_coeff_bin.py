import math

n = int(input("n= "))
x = int(input("x= "))

if (n + x) % 2 == 0 and abs(x) <= n:
    k = (n + x) // 2
    probabilità = math.comb(n, k) * (2**-n)
    print(probabilità)
else:
    print(0)