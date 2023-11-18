from typing import List
def partition(A:List[int], lo:int, hi:int)->List[int]:
    i=hi
    return i

def quick_sort(A:List[int], lo:int, hi:int)->List[int]:
    if lo<hi:
        pivot=partition(A,lo,hi)
        quick_sort(A,lo,pivot-1)
        quick_sort(A,pivot+1,hi)
    return A

import random
A = [random.randint(1,100) for i in range(100)]
print(A)
print(quick_sort(A,1,100))
print(A)
