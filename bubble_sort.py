from typing import List
def bubble_sort(A:List[int])->List[int]:
    n=len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j]>A[j+1]: A[j],A[j+1]=A[j+1],A[j]
    return A

import random
A = [random.randint(1,100) for i in range(10)]
print(A)
print(bubble_sort(A))
