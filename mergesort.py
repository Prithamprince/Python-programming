def merge(a):
      if(len(a)==1):
            return a
      else:
         mid=int(len(a)/2)
         l=merge(a[mid:])
         r=merge(a[ :mid])
      i=j=0
      result=[]
      while(i<len(l) and j<len(r)):
          if(l[i]<r[j]):
                result.append(l[i])
                i+=1
          else:
              result.append(r[j])
              j+=1
      result+=l[i:]
      result+=r[j:]
      return result
a=list(map(int,input().split(" ")))
print(*merge(a),sep=" ")
         
