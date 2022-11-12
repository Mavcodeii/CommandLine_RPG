import random

# -------------------------Game classes-------------------------


class GameStart:
    def menu(self):
        print(' === A Repeating Dungeon -Training grounds ===')
        print('---------------------------------------------')
        print('| 1.            Create Character            |')
        print('---------------------------------------------')
        print('| 2.           Start Your Journey           |')
        print('---------------------------------------------')
        print('| 3.               Exit                     |')
        print('---------------------------------------------')
        selection = input('Enter your selection: ')
        return selection


class Player:
    def __init__(self):
        self.name = None
        self.race = None
        self.weapon = None
        self.weapon_damage = 0
        self.hp = 0
        self.stanima = 0
        self.inventory = []

    def available_classes(self):
        print("""
                        ===  Choose a race  ===
-----------------------------------------------------------------
|        1           |          2          |            3        |
|----------------------------------------------------------------|
|Race: Dwarf         | Race: Human         | Race: elf           |
|Weapon: Battle Axe  | Weapon: Sword       | Weapon: Bow         |
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


class StoryBeats:
    def intro_story(self, encounter_num):
        if encounter_num == 0:
            # consider storying inside a text file and haveing python file reader grab the story beats
            print("""
TODO: Add intro story for character inside city <will be longer>
This story should bring the character to the game store before leaving on the quest

You've been given 200 coin!
""")
        elif encounter_num == 1:
            print('TODO: Add story for the continuation of journey')
        elif encounter_num == 2:
            print('TDO: Create story for the boss level')

    def end_story(self, flag):
        if flag == 1:
            print("""
TODO: Add story about how the encounter was avoided and the player has successfully
made it to the actual dungeon although without real world expierence.

""")
        elif flag == 2:
            print("""
TODO: Add story about how the enemy was defeated and the patht to the real
challenge awaits ahead. Let the player know they now know a taste of what it
will be like in the dungeon.

""")
        elif flag == 3:
            print("You've died as many before you, you were not worthy of the task ahead")


class Store:   # Creates a random list of items to buy at the store everytime it is entered
    def game_shop(self):
        random_set = set()  # uses set to remove duplciates
        mylist = ['Weapon Upgrade', 'Healing Item', 'Stanima Item']
        while len(random_set) != 2:
            random_set.add(random.choice(mylist))

        # going for tuple for the smallest memory size as it will it no change, This creates the option numbers for the items
        options = (1, 2)
        num = 0  # starting point for the tuple call
        value_dict = {}
        print('  === Cleverly named store ===         ')
        for value in random_set:
            print('----------------------------------')
            print('|', options[num], '.', value, '| Cost: 100 Coin       ')
            value_dict[str(options[num])] = value
            num += 1
        num += 1
        print('----------------------------------')
        print('|', num, '.', 'What else you got?', '| Cost: 200 Coin')
        print('----------------------------------')
        print('|', num + 1, '.', 'Nothing interests me')
        print('----------------------------------')
        print('coin amount: ', coin)
        print()
        value_dict['Player_Selection'] = input('Select and item to buy: ')
        return value_dict

    def game_shop_story(self):
        print("""
TODO: Add shop keeper story lines right before offering the two items to sell
""")


class Combat:
    def player_turn(self, player_count):
        player_order = {}
        for players in player_count:
            player_order[players] = random.randint(0, 300)
        return player_order

    def hidden_option(self):
        print()
        print('---------------------------------------------')
        print('| 1.           Try and sneak attack         |')
        print('---------------------------------------------')
        print('| 2.           Try and avoid                |')
        print('---------------------------------------------')
        print()
        initial = input('What do you want to do? ')
        print()
        return initial

    def combat_option(self):
        print()
        print('---------------------------------------------')
        print('| 1.           Attack                       |')
        print('---------------------------------------------')
        print('| 2.           Special Attack               |')
        print('---------------------------------------------')
        print('| 3.           Item Use                     |')
        print('---------------------------------------------')
        print()
        turn_choice = input('Choose an option? ')
        print()
        return turn_choice

    def sneak_attack(self, threshold=6):
        hit_threshold = threshold
        hit_roll = random.randrange(0, 11)
        if hit_roll >= hit_threshold:
            print()
            print('You rolled a: ', hit_roll)
            return 1
        else:
            print()
            print('You rolled a: ', hit_roll)
            return 0

    def spec_attack(self, threshold=7):
        hit_threshold = threshold
        hit_roll = random.randrange(0, 11)
        if hit_roll >= hit_threshold:
            print()
            print('You rolled a: ', hit_roll)
            return 1
        else:
            print()
            print('You rolled a: ', hit_roll)
            return 0

    def use_item(self):
        if player1.inventory:
            print(player1.inventory)
            use_this = input('Type the item to use: ')
            used = player1.inventory.remove(use_this)
        else:
            print('You have not items')
        return used

    def avoid(self):
        hit_threshold = 6
        hit_roll = random.randrange(0, 11)
        if hit_roll >= hit_threshold:
            print('You rolled a: ', hit_roll)
            return 1
        else:
            print('You rolled a: ', hit_roll)
            return 0

    def enemey_attack(self):
        hit_threshold = 8
        hit_roll = random.randrange(0, 11)
        if hit_roll >= hit_threshold:
            print()
            print('Enemy rolled a: ', hit_roll)
            return 1
        else:
            print()
            print('Enemy rolled a: ', hit_roll)
            return 0


# ------------------------------------------------------------
# ---------------------Game logic------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------
#  Declare variables
start = GameStart()
player1 = None
encounter_num = 0
coin = 0
visit_flag = 0
#  Home screen logic


while True:
    option = start.menu()
    if option == '1':
        if player1 is None:
            player1 = Player()
            player1.available_classes()
            player1.createplayer(input('Enter character selection: '),
                                 input('Enter character name: '))
            print("\nYou've created the character: \n")
            player1.character_readout()
            story1 = StoryBeats()  # Initiate story mode
        else:
            print("You've aleady created a character")
    elif option == '2':
        if player1 is not None:
            print()
            story1.intro_story(encounter_num)
            coin += 200
            store = Store()
            break
        else:
            print('Please create a character to proceed')
            print()
    elif option == '3':
        print('Ending game')
        exit()

#-----------------------------------------------------------------------------------------------
# Game story logic

while True:
    if visit_flag == 0:  # <--- To prevent the story function to be called when refreshing store items or an invalid selection
        store.game_shop_story()
        shopping = store.game_shop()
    elif visit_flag == 1:
        shopping = store.game_shop()
    if shopping['Player_Selection'] == '1':
        if coin >= 100:
            coin -= 100
            if shopping['1'] == 'Weapon Upgrade':
                player1.weapon_damage += 10
            elif shopping['1'] == 'Healing Item':
                player1.inventory.append('Healing Item')
            elif shopping['1'] == 'Stanima Item':
                player1.inventory.append('Stanima Item')
        else:
            print("That's not enough money? You trying to play me?")
            visit_flag = 1
    elif shopping['Player_Selection'] == '2':
        if coin >= 100:
            coin -= 100
            if shopping['1'] == 'Weapon Upgrade':
                player1.weapon_damage += 10
            elif shopping['1'] == 'Healing Item':
                player1.inventory.append('Healing Item')
            elif shopping['1'] == 'Stanima Item':
                player1.inventory.append('Stanima Item')
        else:
            print("That's not enough money? You trying to play me?")
            visit_flag = 1
    elif shopping['Player_Selection'] == '3':
        if coin >= 200:
            coin -= 200
            shopping = store.game_shop()
        else:
            print("You don't got that kinda cash, what you see is what you get.")
            visit_flag = 1
    elif shopping['Player_Selection'] == '4':
        print('Leaving store...')
        break


story2 = StoryBeats()
story2.intro_story(encounter_num + 1)
enemy = NPC()
combat = Combat()
combat_choice = combat.hidden_option()
print()
print('Player HP:', player1.hp)
print('Enemy HP:', enemy.hp)
print()

while True:
    if combat_choice == '1':
        roll = combat.sneak_attack()
        if roll == 1:
            print('You hit the enemy for ', player1.weapon_damage)
            enemy.hp = enemy.hp - player1.weapon_damage
            print('Player HP:', player1.hp)
            print('Enemy HP:', enemy.hp)
            break
        else:
            print('You alerted the enemey and was hit for', enemy.weapon_damage)
            player1.hp = player1.hp - enemy.weapon_damage
            print('Player HP:', player1.hp)
            print('Enemy HP:', enemy.hp)
            break
    elif combat_choice == '2':
        roll = combat.avoid()
        if roll == 1:
            story2.end_story(1)
            exit()
        else:
            print('You alerted the enemey and was hit for', enemy.weapon_damage)
            player1.hp = player1.hp - enemy.weapon_damage
            print('Player HP:', player1.hp)
            print('Enemy HP:', enemy.hp)
            break


# Combat
# Player order
# The player count is hard coded right now but future versions will be dynamic
turn_order = combat.player_turn([player1.name, enemy.name])
if turn_order[player1.name] > turn_order[enemy.name]:
    print()
    print(player1.name, 'has the first move')
    move_flag = player1.name
else:
    print()
    print(enemy.name, 'has the first move')
    move_flag = enemy.name


while player1.hp and enemy.hp > 0:
    if move_flag == player1.name:
        fight = combat.combat_option()
        if fight == '1':
            roll = combat.sneak_attack(4)
            if roll == 1:
                print('You hit the enemy for ', player1.weapon_damage)
                enemy.hp = enemy.hp - player1.weapon_damage
                print('Player HP:', player1.hp)
                print('Enemy HP:', enemy.hp)
                move_flag = enemy.name
                continue
            else:
                print('You missed')
                print('Player HP:', player1.hp)
                print('Enemy HP:', enemy.hp)
                move_flag = enemy.name
                continue
        elif fight == '2':
            roll = combat.spec_attack()
            if roll == 1:
                print('You hit the enemy for ', player1.weapon_damage)
                # bonus for spec attack
                enemy.hp = enemy.hp - (player1.weapon_damage + 5)
                player1.stanima = player1.stanima - 10  # cost of using it
                print('Player Stanima:', player1.stanima)
                print('Player HP:', player1.hp)
                print('Enemy HP:', enemy.hp)
                move_flag = enemy.name
                continue
            else:
                print('You missed')
                print('Player Stanima:', player1.stanima)
                print('Player HP:', player1.hp)
                print('Enemy HP:', enemy.hp)
                move_flag = enemy.name
                continue
        elif fight == '3':
            use = combat.use_item()
            if use == 'Healing Item':
                player1.hp = player1.hp + 10
                print(player1.inventory)
                move_flag = enemy.name
                continue
            elif use == 'Stanima Item':
                player1.stanima = player1.stanima + 10
                print(player1.inventory)
                move_flag = enemy.name
                continue
    elif move_flag == enemy.name:
        eroll = combat.enemey_attack()
        if eroll == 1:
            print('You hit the enemy for ', player1.weapon_damage)
            player1.hp = player1.hp - enemy.weapon_damage
            print('Player HP:', player1.hp)
            print('Enemy HP:', enemy.hp)
            move_flag = player1.name
            continue
        else:
            print('Enemy missed')
            print('Player HP:', player1.hp)
            print('Enemy HP:', enemy.hp)
            move_flag = player1.name
            continue


if player1.hp <= 0:
    encounter_num = 3
    story2.end_story(encounter_num)
    print()
    print('Leaving game')
    exit()
elif enemy.hp <= 0:
    encounter_num = 2
    story2.end_story(encounter_num)
    print()
    print('Leaving game... To be continued')
    exit()
