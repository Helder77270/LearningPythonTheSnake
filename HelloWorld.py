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
    elif word1 < word2:
        print("Le mot " + word1 + " est le plus petit dans l\'ordre lexicographique")
    else:
        print("Le mot " + word2 + " est le plus petit dans l\'ordre lexicographique")

# lexicographicOrder()

# PDF EXO 5

def enceintePression(pSeuil, vSeuil):
    if pSeuil > 2.3 and vSeuil > 7.41:
        print("Arrêt immédiat")
        return 0
    elif pSeuil > 2.3 and vSeuil <= 7.41:
        print("Augmentez le volume de l'enceinte")
        return 1
    elif pSeuil <= 2.3 and vSeuil > 7.41:
        print("Diminuez le volume de l’enceinte")
        return 2
    print("Tout va bien")

### enceintePression(2.4 , 7.42)
### enceintePression(2.4 , 7.40)
### enceintePression(2.2 , 7.42)
### enceintePression(2.2 , 7.40)

# PDF EXO 6

def checkIfOnlyOneArobase(chaine):
    cpt = 0
    for i in range(len(chaine)):
        if chaine[i] == '@':
            cpt += 1

    if cpt == 1:
       # print("OK")
        return True
    else:
       # print("NOT OK")
        return False

def checkIfMail(chaine):
    if chaine.endswith('.com') and checkIfOnlyOneArobase(chaine):
        print("E-mail valide !")
    else:
        print("E-mail invalide !")

### checkIfMail("helder.salvador@yahoo.com")

# PDF EXO 7

def boucleX10():
    for i in range(1,11):
        print("Message " + str(i))

### boucleX10()

# PDF EXO 8

def boucleLetter(word):
    for i in range(len(word)):
        print(word[i])

### boucleLetter("Confinement")