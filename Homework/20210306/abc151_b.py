n, k, m = map(int, input().split())
A = [*map(int, input().split())]

total = sum(A)
if m * n - total > k:
    print(-1)
elif m * n - total < 0:
    print(0)
else:
    print(m * n - total)
