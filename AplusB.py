T = int(input())
C = []

for i in range(T):
    A, B = input().split()
    A = int(A)
    B = int(B)
    if 1 <= A <= 9 and 1 <= B <= 9:
        C.append(A + B)
    else:
        ValueError

for j in range(T):
    print('Case #{}: {}'.format(j+1, C[j]))