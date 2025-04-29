D = {
    1:8,
    2.4:9,
    "111":2,
    True: False
    }
print(D)
D = {"A":1,"B":2}
# Ajouter/modifier
D["C"] = 3
D["A"] = 3
print(D)
D.pop("B")
print(D)
print(list(D.values()))
print(list(D.keys()))

#parcourir un dictionnaire
for k in D:
    print(f"{k}:{D[k]}")
for v in D.values():
    print(v)

for k,v in D.items():
    print(f"{k}:{v}")

print(D["A"])
print(D.get("X",0))