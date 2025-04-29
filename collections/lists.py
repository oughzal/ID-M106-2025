# créer une liste 
L1 = [1, 2, 3, 4, 5]
L2 = []
#accéder à un élément de la liste
print(L1[3])
print(L1[-1])
L1[3] = 10
L1[0] = L1[2] + L1[4] + 6
print(L1) # [9, 2, 3, 10, 5]
# ajouter un élément à la liste
L1.append(6) # [9, 2, 3, 10, 5,6]
#insérer dans une position
L1.insert(2,8)
L1.insert(2,8)

L1.extend([10,11,12])
L1 = L1 + [13,14,15]
#supprimer par valeur
L = [1,2,3,5,9,10]
L.remove(9)
print(L)
#supprimer par index
L.pop(1)
print(L)

del L[0]
print(L)

# rechercher
L = [1,2,3,4,3,5]

# compter le nombre d'occurence
print(L.count(3))
if L.count(3) != 0 :
    print(L.index(3))

L = [3,6,1,0,12,8]
L2 = sorted(L)
L.sort()
L = [3,6,1,0,12,8]
L.reverse()
L3 = reversed(L)
print(L)

L = list(range(1,11))
print(L)
print(L[3:6])
print(len(L))

print(L[0:6])
print(L[6:])
print(L[:4])
print(L[::2])
print(L[::-2])
print(L[::-1])

L = [1,2,3] + [4,5,6]

L = list(range(100))
print(L)

#parcourir une liste
for i in range(len(L)):
    print(L[i],end=",")
print()
for e in L:
    print(e,end=",")

for i,e in enumerate(L):
    print(f"{i}:{e}")

if 5 in L:
    print("existe")
else :
    print("n'existe pas")
