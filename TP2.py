"""
Vincent Mayer 023
TP2 - Jeu de devinettes avec chiffre
"""
import random

start_game = True
nombre_min = 0
nombre_max = 100


def bornes():
    global nombre_min, nombre_max
    nombre_max = int(input("Pour commencer choisisser de nombre maximum pour la devinette:"))
    nombre_min = int(input("Ensuite, choisisser le nombre minimum pour la devinette:"))


while start_game:
    bornes()
    print("Maintenant, je vais trouver un nombre en les deux nombres que vous avez choisi.")
    nombre_random = random.randint(nombre_min, nombre_max)
    print(f"Bon je vous ai trouvez un nombre entre {nombre_min} et {nombre_max}")
    print(
        "Pour le trouver, vous devez ecrire des nombre et je vais vous dire si vous visez trop haut ou trop bas. Bonne chance!")
    nb_try = 1
    boucle_jeu = True
    while boucle_jeu == True:
        essai = int(input(f"Essai numéro {nb_try}, Entrez un nombre:"))
        nb_try += 1
        if nb_try < nombre_random:
            print("Visé un nombre plus grand.")
        elif essai > nombre_random:
            print("Visé un nombre plus petit.")
        elif essai == nombre_random:
            print("Bien joué vous avez trouvez!")
            rejouer = input("Voulez recommencer pour voir si vous pouvez trouvez en moin d'essai?")
            if rejouer == "oui":
                boucle_jeu = False
            else:
                print("Merci et aurevoir")
                boucle_jeu = False
                start_game = False
