import os

def shutdown(time):
   os.popen("shutdown -s -t " + str(time))

def cancel():
    os.popen("shutdown -a")
    print("Arrêt annulé.")


print("Entrez le temps en secondes avant l'arrêt ou cancel pour annuler l'arrêt.")

while True:

    choice = input()

    if choice == "":
        break

    elif choice == "cancel" or choice.replace(" ","")[0] == "c":
        cancel()


    else:
        try:
            if choice.replace(" ","")[0] == "h":
                choice = str(choice+"0")
                choice = float(choice[1:-1]) * 3600

            elif choice.replace(" ","")[0] == "m":
                choice = str(choice+"0")
                choice = float(choice[1:-1]) * 60

            elif choice.replace(" ","")[0] == "e":
                choice = str(choice+"0")
                choice = float(choice[1:-1]) * 60 * 24

            time = int(choice)
            if time <= 30:
                print("Veuillez entrer une valeur supérieure à 30 secondes...")
            
            else:
                shutdown(time)
                if time >= 3600:
                    print(f"L'arrêt de la machine aura lieu dans {int(time/3600)} heures.")
                elif 60 <= time < 3600:
                    print(f"L'arrêt de la machine aura lieu dans {int(time/60)} minutes.")
                else:
                    print(f"L'arrêt de la machine aura lieu dans {time} secondes.")
            

        except ValueError:
            print("Veuillez entrer un nombre valide.")
                     