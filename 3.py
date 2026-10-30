import random
for n in [10, 100, 1000, 10000]:
    counts = [0, 0, 0, 0]
    for _ in range(n):
        x = random.random()  
        counts[int(x * 4)] += 1 
    print(f"N = {n:>5}: {counts}  (доли: {[round(c/n, 3) for c in counts]})")