# coding: utf-8

import comMorse

def texte(phrase):
<<<<<<< HEAD
    """Fonction prennant une phrase ou un mot et renvoyant son equivalent en morse
    sous forme de chaine de caractere.
    Pour faciliter la lecture, des espaces sont inserer entre les codes.
    Des / sont aussi inserer pour representer les espaces entre les mots"""
    
=======
>>>>>>> ajout matrice3D et finlaisation exos morse
    reponse=""
    for lettre in phrase:
        if lettre != " ":
            reponse= reponse + comMorse.encode(lettre)
            reponse= reponse + " "
        else:
            reponse= reponse + "/ "
    return reponse



def morse(morseBrut):
<<<<<<< HEAD
    """Fonction prennant une phrase ou un mot en morse et renvoyant son equivalent texte
    sous forme de chaine de caractere."""

=======
>>>>>>> ajout matrice3D et finlaisation exos morse
    reponse=""
    morseBrut = str.split(morseBrut," ")
    for element in morseBrut:
            if element != "/" and element != "":
                reponse= reponse + comMorse.decode(element)
            else:
                reponse= reponse + " "
    return reponse

print("tapez un mot ou une phrase courte")
phrase = input()
print(texte(phrase))

print("tapez un mot ou une phrase courte en morse")
morseBrut = input()
print(morse(morseBrut))