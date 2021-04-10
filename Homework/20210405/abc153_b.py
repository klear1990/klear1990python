H, N = map(int,input().split())
a = list(map(int,input().split()))
A = sum(a)

if A >= H:
    print('Yes')
else:
    print('No')
