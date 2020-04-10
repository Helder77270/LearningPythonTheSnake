from math import *

print("Hello World")

# PDF EXO 1
def calculVitesse(d , t):
    v = 0
    v = d/t
    print(v)
    return v

### calculVitesse(6.892, 19.7)

# PDF EXO 2
def printAgeEtNom():
    print("Quel est votre nom ?")
    nom = str(input())
    print("Quel est votre age ?")
    age = int(input())
    print('Je suis ' + nom + ' j\'ai ' + age)

### printAgeEtNom()

# PDF EXO 3

def squareFloat():
    print("Entrez un flottant nul ou positif : \n")
    value = float(input())
    if value >= 0.0:
        print(sqrt(value))
    else:
        print("ERROR")
        return 69

### squareFloat()

# PDF EXO 4

def lexicographicOrder():
    word1 = str(input("Entrez votre premier mot :"))
    word2 = str(input("Entrez votre second mot :"))

    if word1 == word2:
        print("Ce sont les même mots :) ")
        return 0
    if word1 < word2:
        print("Le mot " + word1 + " est le plus petit dans l\'ordre lexicographique")
    else:
        print("Le mot " + word2 + " est le plus petit dans l\'ordre lexicographique")

# lexicographicOrder()

# PDF EXO 5

def enceintePression(pSeuil, vSeuil):
    if pSeuil > 2.3 and vSeuil > 7.41:
        print("Arrêt immédiat")
        return 0
    if pSeuil > 2.3 and vSeuil <= 7.41:
        print("Augmentez le volume de l'enceinte")
        return 1
    if pSeuil <= 2.3 and vSeuil > 7.41:
        print("Diminuez le volume de l’enceinte")
        return 2
    print("Tout va bien")

enceintePression(2.4 , 7.42)
enceintePression(2.4 , 7.40)
enceintePression(2.2 , 7.42)
enceintePression(2.2 , 7.40)




