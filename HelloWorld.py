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

# PDF EXO 9
def boucleWhile():
    a = 0
    b = 10

    while a < b:
        print(a)
        a += 1

### boucleWhile()

# PDF EXO 10

def boucleWhileDecrement():
    a = 0
    b = 10

    while b > a:
        if b % 2 == 1:
            print(b)
        b -= 1

### boucleWhileDecrement()

# PDF EXO 11

def betweenOneAndTen():
    num = 1

    while True:
        num = int(input("Entez un nombre entre 1 et 10 \n"))
        if num < 1:
            print('Recommence')
        elif num > 10:
            print('Recommence')
        else:
            print("Bien joué")
            break

### betweenOneAndTen()

# PDF EXO 12

def boucleImbriquées():
    liste = ['Helder' , 'Gautier' , 'Sid']

    for i in range(len(liste)):
        for j in range(len(liste[i])):
            print(liste[i][j])

### boucleImbriquées()

# PDF EXO 13

def jump3by3():
    for i in range(3 , 13):
        if i % 3 == 0:
            print(i)

###jump3by3()

# PDF EXO 14

def printEvenNumbers(n):
    cpt = 0
    while cpt <= 1:
        for i in range(0 , n):
            if i % 2 == 0:
                print(i)
                cpt+=1


printEvenNumbers(50)
