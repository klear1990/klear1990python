alphabet_list = list(map(chr, range(ord('a'), ord('z') + 1)))

A = input()
for i in range(26):
    if A == alphabet_list[i]:
        print(alphabet_list[i+1])
    else:
        pass

    
