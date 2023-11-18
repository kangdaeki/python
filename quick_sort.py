from typing import List
def partition(A:List[int], lo:int, hi:int)->List[int]:
    i=lo
    j=hi-1
    pivot=A[hi]
    while i<j:
        while A[i]<pivot and i<j: 
            i+=1
        while A[j]>=pivot and i<j: 
            j-=1
        if i<j:
            A[i],A[j]=A[j],A[i]
    if A[j]>pivot:
        A[j],A[hi]=A[hi],A[j]
        return j
    else:
        return j+1

def quick_sort(A:List[int], lo:int, hi:int)->List[int]:
    if lo<hi:
        pivot=partition(A,lo,hi)
        quick_sort(A,lo,pivot-1)
        quick_sort(A,pivot+1,hi)
    return A

n=1000
b=1000
import random
A = [random.randint(1,b) for i in range(n)]
print(A)
print(quick_sort(A,0,n-1))
