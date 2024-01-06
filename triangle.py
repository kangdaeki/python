# https://www.youtube.com/watch?v=6vAw0kB88Wg&ab_channel=LiuZuoLin
# https://math.stackexchange.com/questions/3492701/why-does-this-pattern-occur-123456789-times-8-9-987654321 

def triangle(n):
    print(*[sum([(j%10)*10**(i-j) for j in range(1,i+1)]) for i in range(1,n+1)],sep='\n')
    print()
    [print(sum([(j%10)*10**(i-j) for j in range(1,i+1)])) for i in range(1,n+1)]
    print()
    # original solution
    [print(''.join([str((j%10)) for j in range(1,i+1)])) for i in range(1,n+1)]
    print()

def triangle2(n): # using mathematical generating function: only works for [1..9]
    [print((int("1"*(i+1))-(i+1))//9) for i in range(1,n+1)]
    print()

def triangle3(): # another mathematical generating function
    print(*[int("123456789"[:i])*8+i for i in range(1,10)],sep='\n')
    print()

# solution by clivegreen7139
def triangle4(n): 
    [print('54321'[0:n-i]) for i in range(n)]
    print()

# solution by yowtfallnamestaken
def triangle5(n): 
    [print(*range(n, n-i, -1), sep="") for i in range(n, 0, -1)]
    print()

# another solution by clivegreen7139
def triangle_n(count: int, descending=False) -> None:
    [print(' '.join([str(num) for num in range(1, count-i+2 if descending else i+1)])) for i in range(1, count + 1)]
    print()

triangle_n(5, True)
triangle(5)
triangle2(5)
triangle3()
triangle4(5)
triangle5(5)
triangle_n(5, True)
