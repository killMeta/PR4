n = int(input("Введите N (> 0): "))

total = 0.0
for i in range(1, n + 1):
    term = float(i) ** (n - i + 1)
    total += term
print(f"Сумма = {total}")