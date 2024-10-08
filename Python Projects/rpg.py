from rpg_class import *

shop = [
Consommables("Health Flask", 25, 20),
Consommables("Health Potion", 75, 50),
Consommables("Health Cooking Pot", 165, 100),
Consommables("Health Sea", 999, 200),
Consommables("Heart Container", 50, 75),
Weapons("Wooden Sword", 2, 0),
Weapons("Short Bow", 4, 30),
Weapons("Crossbow", 6, 50),
Weapons("Dagger", 10, 80),
Weapons("Throwing Axe", 14, 120),
Weapons("Iron Sword", 16, 150),
Weapons("Diamond Sword", 22, 200),
Weapons("Gun", 25, 240),
Weapons("Skyfall", 30, 280),
Weapons("Nightfall", 40, 350),
Weapons("The Darkin Blade", 50, 400)
]

listeEnemies = [
Characters("Goblin",max_health = 10, health = 10, damage = 2,level = 1),
Characters("Barbarian",max_health = 25, health = 25, damage = 5,level = 2),
Characters("Archer", max_health = 50, health = 50, damage = 10, level = 3),
Characters("Wizard", max_health = 65, health = 65, damage = 15, level = 4),
Characters("Giant", max_health = 100, health = 100, damage = 25, level = 5),
Characters("Barbarian King", max_health = 120, health = 120, damage = 30, level = 6),
Characters("Baby PEKKA", max_health = 150, health = 150, damage = 50, level = 7),
Characters("Dragon", max_health = 200, health = 200, damage = 60, level = 8),
Characters("Archer Queen", max_health = 250, health = 250, damage = 80, level = 9),
Characters("PEKKA", max_health = 300, health = 300, damage = 100, level = 10),
Characters("Lord PEKKA", max_health = 500, health = 500, damage = 200, level = 11)
]

def shopFunc():
    while True:
        choiceWeapon = input(f"Which item would you like to buy? ({Hero.credits} credits) ")
        try: 
            choiceWeapon = int(choiceWeapon)
            if choiceWeapon == 0:
                print("You left the shop.")
                break
            elif choiceWeapon > len(shop):
                print("Please enter a valid choice!")
            else:
                if Hero.credits >= shop[choiceWeapon-1].price:
                    print(f"You have bought {shop[choiceWeapon-1].name} for {shop[choiceWeapon-1].price} credits!")
                    Hero.credits -= shop[choiceWeapon-1].price
                    try:
                        Hero.equip(shop[choiceWeapon-1].damage)
                        print(f"You're now equipped with {shop[choiceWeapon-1].name} and deal {Hero.damage+Hero.equipment} damage!")
                    except AttributeError:
                        if shop[choiceWeapon-1].name == "Heart Container":
                            Hero.health += shop[choiceWeapon-1].health
                            Hero.max_health += shop[choiceWeapon-1].health
                            print(f"You gained 50 max hp and now have {Hero.health}/{Hero.max_health}hp.")
                        else:   
                            Hero.health += shop[choiceWeapon-1].health
                            if Hero.health >= Hero.max_health:
                                Hero.health = Hero.max_health
                            print(f"You regained {shop[choiceWeapon-1].health} health and now have {Hero.health}/{Hero.max_health}hp.")
                    break
                else:
                    print(f"You don't have enough credits to buy {shop[choiceWeapon-1].name}!")
        except ValueError:
            print("Please enter a valid choice!")




gameOn = True
heroName = input("Enter your name: ")
Hero = Characters(name=heroName)
while gameOn:
    print(f"You've encountered {listeEnemies[Hero.level - 1].name} ({listeEnemies[Hero.level - 1].max_health}hp)!")
    while Hero.health > 0 and listeEnemies[Hero.level - 1].health > 0:
        choiceFight = ""
        choiceFight = input(f"""What will you do ?
1. Attack
2. Defend
3. Flee
""")
        try: 
            choiceFight = int(choiceFight)
            if choiceFight == 1:
                print(f"{listeEnemies[Hero.level - 1].name} attacks you for {listeEnemies[Hero.level - 1].damage} damage !")
                print(f"You attack {listeEnemies[Hero.level - 1].name} for {Hero.damage+Hero.equipment} damage !")
                Hero.health -= listeEnemies[Hero.level - 1].damage
                listeEnemies[Hero.level - 1].health -= Hero.damage+Hero.equipment
                print(f"You now have {Hero.health}hp and {listeEnemies[Hero.level - 1].name} has {listeEnemies[Hero.level - 1].health}hp.")
            elif choiceFight == 2:
                print(f"{listeEnemies[Hero.level - 1].name} attacks you for {listeEnemies[Hero.level - 1].damage} damage !")
                print("But you successfully defended and took no damage!")
                print(f"You now have {Hero.health}hp and {listeEnemies[Hero.level - 1].name} has {listeEnemies[Hero.level - 1].health}hp.")
            elif choiceFight == 3:
                print(f"You fled from {listeEnemies[Hero.level - 1].name}")
                break
            else:
                print("Please enter a valid choice!")
        except ValueError:
            print("Please enter a valid choice !")
    if Hero.lose() == True:
        break
    elif listeEnemies[Hero.level - 1].health <= 0:
        print("You won the fight!")
        Hero.levelUp()



    while True:
        choiceAdv = input(f"""What will you do ?
1. Continue to the next level
2. Go to shop ({Hero.credits} credits)
3. Stop the game
""")
        try: 
            choiceAdv = int(choiceAdv)
            if choiceAdv == 1:
                break
            elif choiceAdv == 2:
                print("Welcome to the shop! Choose between any of these item: ")
                print(f"0. Cancel")
                for i in range(len(shop)):
                    try : 
                        print(f"{i+1}. {shop[i].name} (+{shop[i].damage} damage) - {shop[i].price} credits")
                    except AttributeError:
                        if shop[i].name == "Heart Container":
                            print(f"{i+1}. {shop[i].name} (+{shop[i].health} max hp) - {shop[i].price} credits")
                        else:
                            print(f"{i+1}. {shop[i].name} (+{shop[i].health}hp) - {shop[i].price} credits")
                shopFunc()
            elif choiceAdv == 3:
                gameOn = False       
                break
            else:
                print("Please enter a valid choice!")
        except ValueError:
            print("Please enter a valid choice !")
