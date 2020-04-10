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
        print("OK @")
        return True
    else:
        print("NOT OK @")
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


### printEvenNumbers(50)

# PDF EXO 15

def exoListe():
    liste = [17, 38, 10, 25, 72]

    print("Triez et affichez la liste")
    liste.sort()
    print(liste)

    print("Ajoutez l’élément 12 à la liste et affichez la liste")
    liste.append(12)
    print(liste)

    print("Renversez et affichez la liste")
    liste.reverse()
    print(liste)

    print("Affichez l’indice de l’élément 17")
    for i in range(len(liste)):
        if liste[i] == 17:
            print(i)

    #Plus simple :D
    print(liste.index(17))

    print("Enlevez l’élément 38 et affichez la liste")
    liste.remove(38)
    print(liste)

    print("Affichez la sous-liste du 2 eme au 3e élément")
    print(liste[1:3])

    print("Affichez la sous-liste du début au 2eélément")
    print(liste[0:2])

    print("Affichez la sous-liste du 3eélément à la fin de la liste")
    print(liste[2:len(liste)])

    print("Affichez la sous-liste complète de la liste")
    print(liste[0:len(liste)])

#exoListe()

# PDF EXO 16

def reverseString(word):
    tmp = word[::-1]
    print(tmp)

### reverseString("!! sruoc sel tnadnep xilfteN redrager sap tuaf en lI")

# PDF EXO 17

def palindrome(word):
    tmp = word[::-1]
    if word == tmp:
        print("C'est un palindrome")
    else:
        print("Ce n'est pas un palindrome")

### palindrome("Kayak")
### palindrome("kayak")

# PDF EXO 18
def checkDotsBeforeAt(mail):
    i = 0
    cptDot = 0
    str(mail)
    while mail[i] != '@':
        if mail[i] == '.':
            cptDot += 1
            i += 1
        else:
            i += 1
    if cptDot <= 1:
        print("OK POINT BEFORE @")
        return True
    else:
        print("NOT OK POINT BEFORE @")
        return False

def checkDotsAfterAt(mail):
    cptDot = 0
    tmp = mail[::-1]
    i = 0
    print(tmp)
    while i != '@':
        if tmp[i] == '.':
            cptDot += 1
        i += 1
    print(cptDot)

    if cptDot == 1:
        print("OK POINT POST @")
        return True
    else:
        print("NOT OK POINT POST @")
        return False
    
def checkIfOnly3charAfterLastPoint(mail):
    tmp = mail[::-1]
    if tmp[3] == '.':
        print("OK 3 CHAR")
        return True
    else:
        print("NOT OK 3 CHAR")
        return False

def highLevelMailCheck(mail):
    str(mail)
    if checkDotsBeforeAt(mail) and checkIfOnlyOneArobase(mail) and checkDotsAfterAt(mail) and checkIfOnly3charAfterLastPoint(mail):
        print("Ce mail est correct")
    else:
        print("Ce mail est incorrect")

# mail = "helder.salvador@yahoo.com"
# mail2 = "helder..salvador@yahoo.com"
mail3 = "helder.salvador@yahoo..com"
# mail4 = "helder.salvador@@yahoo.com"
#
checkDotsAfterAt(mail3)
# print("DOIT ETRE CORRECT \n")
# highLevelMailCheck(mail)
# print("DOIT ETRE INCORRECT \n")
# highLevelMailCheck(mail2)
# print("DOIT ETRE INCORRECT \n")
# highLevelMailCheck(mail3)
# print("DOIT ETRE INCORRECT \n")
# highLevelMailCheck(mail4)