A, B, C = map(int,input().split())
if A - B == 0 or A - C == 0 or B - C == 0:
    if A == B == C:
        print('No')
    else:
        print('Yes')
else:
    print('No')
