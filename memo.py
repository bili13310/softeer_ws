S = [0, 1, 2, 3, 4]
A = int(2)
B = int(5)
F = 0

for i in range(B-A+1):
    T = S[A-1+i]
    F += T
    print(F)

print(F)