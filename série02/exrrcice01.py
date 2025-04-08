# Exercice 01 
T = float(input("Donner la temperature : "))
if T <= 0 :
    print("Solide")
elif T < 100 :
    print("Liquide")
else :
    print("Gaz")