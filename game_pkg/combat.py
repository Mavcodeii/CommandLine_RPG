import random


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

    # def use_item(self):
    #     if player1.inventory:
    #         print(player1.inventory)
    #         use_this = input('Type the item to use: ')
    #         used = player1.inventory.remove(use_this)
    #     else:
    #         print('You have not items')
    #     return used

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
