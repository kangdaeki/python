N=int(input())
conway=[1,1]
if 2<N:
    for i in range(2,N):
        offset=conway[i-1]-1
        conway.append(conway[offset]+conway[i-1-offset])
for i in range(N):
    print(conway[i], end=' ')
print()
