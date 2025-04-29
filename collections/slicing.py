L = list(range(10,30))
print(L)
print(L[5:11])
print(L[5:11:2])
# L[start:end-1:step]
print(L[-2:-6:-1])
print(L[:])

L =  [1,2,3]
L2 = L.copy()
L2 = L[:]
L2[0] = 10
print(L)


L = [31,5,"EFM","DRBK",[2,0,2,3],0]
print(L[-4:-1])
print(L[::2])
print(L[2:5:1])
print(L[-len(L):len(L)])
print(L[-6:6])

print(len(L))
L.insert(4,"Digital")
L.remove([2,0,2,3])
print(L)