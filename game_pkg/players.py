
class Player:
    def __init__(self):
        self.name = None
        self.race = None
        self.weapon = None
        self.weapon_damage = 0
        self.hp = 0
        self.stanima = 0
        self.inventory = []
        self.coin = 0

    def available_classes(self):
        print("""
                        ===  Choose a race  ===
-----------------------------------------------------------------
|        1           |          2          |            3        |
|----------------------------------------------------------------|
|Race: Dwarf         | Race: Human         | Race: Dwarf         |
|Weapon: Battle Axe  | Weapon: Sword       | Weapon: Battle Axe  |
|HP: 200             | HP: 100             | HP: 200             |
|Stanima: 200        | Stanima: 200        | Stanima: 200        |
-----------------------------------------------------------------
        """)

    def createplayer(self, selection, name):
        available_race = [
            {'race': 'Dwarf', 'weapon': 'battle axe',
                'weapon_damage': 50, 'hp': 200, 'stanima': 200},
            {'race': 'Human', 'weapon': 'Sword',
                'weapon_damage': 40, 'hp': 100, 'stanima': 200},
            {'race': 'Elf', 'weapon': 'Magic Bow', 'weapon_damage': 30, 'hp': 150, 'stanima': 150}]
        if selection == '1':
            self.name = name
            self.race = available_race[0]['race']
            self.weapon = available_race[0]['weapon']
            self.weapon_damage = available_race[0]['weapon_damage']
            self.hp = available_race[0]['hp']
            self.stanima = available_race[0]['stanima']
        elif selection == '2':
            self.name = name
            self.race = available_race[1]['race']
            self.weapon = available_race[1]['weapon']
            self.weapon_damage = available_race[1]['weapon_damage']
            self.hp = available_race[1]['hp']
            self.stanima = available_race[1]['stanima']
        elif selection == '3':
            self.name = name
            self.race = available_race[2]['race']
            self.weapon = available_race[2]['weapon']
            self.weapon_damage = available_race[2]['weapon_damage']
            self.hp = available_race[2]['hp']
            self.stanima = available_race[2]['stanima']
        else:
            print('Invalid selection')

    def character_readout(self):
        print('Name:', self.name, '\nWeapon:', self.weapon,
              '\nWeapon_damage:', self.weapon_damage, '\nHP: ', self.hp, '\nStanima: ', self.stanima,)
        print()


class NPC:
    def __init__(self):
        self.name = 'Monster'
        self.weapon = 'Hatchet'
        self.weapon_damage = 40
        self.hp = 100
        self.stanima = 100
