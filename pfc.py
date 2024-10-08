import random


while True:
    userInput = input("Pierre Feuille Ciseaux : ")
    pfc = ["pierre","feuille","ciseaux"]
    compInput = pfc[random.randint(0,2)]

    if userInput.lower() == "pierre" or userInput.lower() == "p":
        if compInput == "pierre":
            print("egalité")
        if compInput == "feuille":
            print("perdu")
        if compInput == "ciseaux":
            print("gagné")

    elif userInput.lower() == "feuille" or userInput.lower() == "f":
        if compInput == "pierre":
            print("gagné")
        if compInput == "feuille":
            print("egalité")
        if compInput == "ciseaux":
            print("perdu")
        
    elif userInput.lower() == "ciseaux" or userInput.lower() == "c":
        if compInput == "pierre":
            print("perdu")
        if compInput == "feuille":
            print("gagné")
        if compInput == "ciseaux":
            print("égalité")
    else:
        print("Entrée non valide, veuillez entrez 'pierre', 'feuille' ou 'ciseaux' ")