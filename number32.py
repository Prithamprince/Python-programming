p=input()
p=p.split(" ")
p=list(map(int,p))
n=p[0]
k=p[1]
q=input()
q=q.split(" ")
q=list(map(int,q))
r=sorted(q)
print(r[k-1])
