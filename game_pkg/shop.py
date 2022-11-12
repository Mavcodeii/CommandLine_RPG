import random
import players
coin = 0


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
        print('  === Cleaverly named store ===         ')
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
