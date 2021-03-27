string = input().split()
a = len(string[0])
b = len(string[1])
 
if a >= b:
    print(string[1],string[0],sep='')
else:
    print(string[0],string[1],sep='')
