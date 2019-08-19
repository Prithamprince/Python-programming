l,m=input().split(" ")
n=input()
p=n.replace(m,"")
q=p.replace("  "," ")
if(len(q)<1):
     print("empty")
else:
     print(q)

