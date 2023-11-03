import sys
Total = 0


for i in range(5):
    ON, OFF = map(str, input().split())
    ONHH, ONMM = map(int, ON.split(':'))
    OFFHH, OFFMM = map(int, OFF.split(':'))

    if 0 <= ONHH <= 24 or 0 <= OFFHH <= 24 or 0 <= ONMM <= 59 or 0 <= OFFMM <= 59:
        if OFFMM >= ONMM:
            MM = OFFMM - ONMM
            HTM = (OFFHH - ONHH) * 60
            # hour to minute
            minutes = MM + HTM
            Total += minutes

        elif OFFMM < ONMM:
            MM = OFFMM + 60 - ONMM
            HTM = (OFFHH - ONHH - 1) * 60
            minutes = MM + HTM
            Total += minutes

    else:
        ValueError

print(Total)