n,q = list(map(int,input().split()))
l = list(map(int,input().split()))
cal=0
sum1=0
for i in range(q):
    inp=list(map(int,input().split()))
    if(inp[0]==1):
        if(l[inp[1]-1]==0):
            l[inp[1]-1] = l[inp[1]-1]+1
        else:
            l[inp[1]-1] = l[inp[1]-1]-1
    else:
        if(l[inp[2]-1]==1):
            print("ODD")
        else:
            print("EVEN")
