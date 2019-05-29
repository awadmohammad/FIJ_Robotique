#il existe 3 types de variable sous python

variable1 = 5 #integer > int qui symbolise un nombre entier
variable2 = 3.2 # float > float qui symbolise un chiffre a virgule
variable3 = "coucou" # string > str qui symbolise du texte
variable4 = True # boolean > bool symbolise une variable soit vrai
                 #soit faux
variable5 = ["1er","2eme","3eme"] #list > une variable liste qui
                                  #comprendre 3 string
# fonction qui permet d'afficher du texte et le contenu d'un variable
# a l'ecran
print("du texte", variable1, variable2, variable3, variable4, )
print( variable5[1])

#lere fonction qui permet d'afficher d'un variable a l'ecran
print("du texte", variable1, variable2, variable3)

#fonction permetant de connaitre le type d'une variable 
type( type(variable1) )

typeDeVariable = type(variable1)

print("le type de la variable =", typeDeVariable)

#Ici, on modifie le type de variable1 en string
variable1 = str(variable1)

typeDeVariable = type(variable1)
print("le type de la variable =", typeDeVariable)

# En python, il existe plusieurs operateurs
# addition          >    +
# soustraction      >    -
# multiplication    >    *
# division          >    /
# division          >    //
# modulo            >    %
