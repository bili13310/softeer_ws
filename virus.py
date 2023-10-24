import sys

K, P, N = input().split()

K = int(K)
P = int(P)
N = int(N)

for i in range(N):
    A = K * P
    K = A % 1000000007

print(K)