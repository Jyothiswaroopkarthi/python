n=int(input())
l=list(map(int,input().split()))
q=int(input())
d=dict.fromkeys(l,0)
for i in l:
    d[i]+=1
while(q):
    i=int(input())
    try:
        print(d[i])
    except KeyError:
        print("NOT PRESENT")
    q=q-1
