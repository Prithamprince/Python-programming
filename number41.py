f=input()
g=input()
f=f.split(" ")
h=f[1]
g=g.split(" ")
for i in g:
       if(i==h):
           print("Yes")
           break
else:
   print("No")
