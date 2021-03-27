a = int(input())
b = input()

c = b[0:int(a/2)]
if b == c+c:
    print('Yes')
else:
    print('No')
