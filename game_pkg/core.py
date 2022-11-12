
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
