# ecrire()
# lire(c)
c = input("donner un caractère : ")
# Si c >= '0' et c<='9' alors
if c>='0' and c<= '9':
    print(c , " est un chiffre")
elif c >= 'A' and c<='Z' :
    print(c , " est une Majuscule")
elif  c >= 'a' and c<='z' :
    print(c , " est une Miniscule")
else : 
    print(c , " est un Symbole")

