import sys
n=int(input())
s=[]

for i in range(n):
    ord=sys.stdin.readline().split()

    if ord[0]=='push':
        s.append(int(ord[1]))
    elif ord[0]=='pop':
        if len(s)==0:
            print(-1)
        else:
            print(s.pop(0))
    elif ord[0]=='size':
        print(len(s))
    elif ord[0]=='empty':
        if len(s)==0:
            print('1')
        else:
            print('0')
    elif ord[0]=='front':
        if len(s)==0:
            print('-1')
        else:
            print(s[0])
    else:
        if len(s)==0:
            print('-1')
        else:
            print(s[len(s)-1])