import sys, itertools
# 외부 라이브러리(numpy 사용불가)

# 3.5h

N, K = map(int,input().split())

S = []
F = []
f = 0
A = []
B = []
j = 0

S.append(input().split())
print(S)
S = list(itertools.chain(*S))
print(S)
S = list(map(int, S))
print(S)

if len(S) == N:
    for i in range(K):
        a, b = map(int, input().split())
        A.append(a), B.append(b)
        if A[i] > N or A[i] < 1 or B[i] > N or B[i] < 1:
            ValueError
        else:
            for j in range(B[i] - A[i] + 1):
                T = S[A[i]-1+j]
                f += T
            PG = f / (B[i] - A[i] + 1)
            F.append(PG)
            f = 0

else:
    print("잘못된 개수를 입력했습니다.")
    ValueError

for k in range(K):
    print('{:.2f}'.format(F[k]))