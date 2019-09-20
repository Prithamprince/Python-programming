def quicksort(array):
       if(len(array)<2):
             return array
       else:
          pivot=array[0]
          less=[i for i in i<=pivot]
          greater=[i for i in i>pivot]
          return quicksort(less)+[pivot]+quicksort(greater)
array=list(map(int,input().split(" ")))
print(quicksort(array))
