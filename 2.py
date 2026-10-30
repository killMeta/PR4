import math
x = float(input("x (|x|<1): "))
eps = float(input("eps: "))
left = math.pi**2/8 - math.pi/4*abs(x)
right, n = 0.0, 0
while True:
    k = 2*n + 1
    term = math.cos(k*x) / k**2
    right += term
    if abs(term) < eps:
        break
    n += 1
print(f"Левая:  {left:.8f}")
print(f"Правая: {right:.8f}")
print(f"Итераций: {n+1}")