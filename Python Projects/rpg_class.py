class Characters:
    def __init__(self, name = "Hero",max_health = 100, health = 100, damage = 10, level = 1,credits = 0,equipment = 0):
        self.name = name
        self.max_health = max_health
        self.health = health
        self.damage = damage
        self.level = level
        self.credits = credits
        self.equipment = equipment

    def equip(self, item):
        self.equipment = int(item)

    def levelUp(self):
        self.level += 1
        self.max_health += 25
        self.health += 25
        self.damage += 5
        self.credits += 25 * self.level
        print(f"You're now level {self.level} ! You gained 25 max hp, 5 base damage and {25*self.level} credits !")

    def lose(self):
        if self.health <= 0:
            print(f"You died.")
            return True

class Weapons:
    def __init__(self, name, damage, price):
        self.name = name
        self.damage = damage
        self.price = price

class Consommables:
    def __init__(self, name, health, price):
        self.name = name
        self.health = health
        self.price = price
