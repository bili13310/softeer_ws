import sys, itertools, numpy
# 외부 라이브러리(numpy 사용불가)

# 2h

N, K = map(int,input().split())

S = []
PG = []

S.append(input().split())
S = list(itertools.chain(*S))
S = list(map(int, S))

if len(S) == N:
    for i in range(K):
        A, B = map(int, input().split())
        if A > N or A < 1 or B > N or B < 1:
            ValueError
        else:
            PG.append(numpy.mean(S[A-1:B]))
            # type(S[i])는 str 이를 활용해 mean을 계산하려면 int화 시켜줘야돼
else:
    print("잘못된 개수를 입력했습니다.")
    ValueError

for i in range(K):
    print(round(PG[i],2))