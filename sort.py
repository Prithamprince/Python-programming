p=int(input())
q=input()
q=q.split(" ")
q=list(map(int,q))
s=sorted(q)
print(*s,sep=" ")
