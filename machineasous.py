import random
import time

credits:int = 1000
machineListe = ["🍇"]*10 + ["🍏"]*9 + ["🥝"]*8 + ["🍌"]*7 + ["🍓"]*6 + ["🍊"]*5 + ["🍒"]*4 + ["🥥"]*3 + ["🥭"]*2 + ["🍍"]
gameOn = True


def slots(mise: int):
    global credits

    slotsMachine = ["","",""]
    winCase = 0

    for i in range(3):
        rndNbr = random.randint(0,54)
        slotsMachine[i] = machineListe[rndNbr]
    time.sleep(0.5)
    print(f"""
          {slotsMachine[0]} | .. | ..
          """)
    time.sleep(0.5)
    print(f"""
          {slotsMachine[0]} | {slotsMachine[1]} | ..
          """)
    time.sleep(0.5)
    print(f"""
          {slotsMachine[0]} | {slotsMachine[1]} | {slotsMachine[2]}

          """)

    for item in slotsMachine:
        if slotsMachine.count(item) == 2:
            if slotsMachine[0] == slotsMachine[1] or slotsMachine[1] == slotsMachine[2]:
                winItem = item
                winCase = 2
                itemScore = 11-machineListe.count(item)
                gain = itemScore * mise
                credits += gain
                break

        if slotsMachine.count(item) == 3:
            winItem = item
            winCase = 3
            itemScore = 11-machineListe.count(item)
            gain = (itemScore * 3) * mise
            credits += gain
            break

    if winCase == 0:
        print(f"C'est perdu. Vous perdez {mise} crédits.")
    else:
        if itemScore == 10 and winCase == 3:
            print(f"Jackpot!!! Vous remportez {gain*2} crédits ! ")
            credits += (gain*2)-gain
        else:
            print(f"Gagné! {winItem} à une valeur de {itemScore} points, vous remportez donc {gain} crédits.")


print("Bienvenue aux machines à sous!")
while gameOn:
    while True:
        try:
            try:
                replay = int(replay)
                miseInp = replay
            except:
                print(f"Veuillez misez une somme, vous avez {credits:,} crédits : ")
                miseInp = int(input())
            if 0 < miseInp <= credits:
                credits -= miseInp
                print("Lancement de la machine à sous...")
                break
            else:
                print(f"Veuillez misez une somme entre 1 et {credits:,}.")
                replay = ""
        except ValueError:
            print("Mise non valide, réessayez. ")
    slots(miseInp)
    if credits <= 0:
        print("Vous êtes fauchés, par conséquent le casino vous a exclus.")
        input()
        gameOn=False
    else:
        print(f"Vous avez {credits:,} crédits. Souhaitez vous rejouer ? Entrez non/n pour partir du casino: ")
        replay = input()
        if replay.lower().replace(" ","") == "":
            continue
        elif replay.lower().replace(" ","")[0] == "n":
            gameOn = False



