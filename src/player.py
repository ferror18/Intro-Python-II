# Write a class to hold player information, e.g. what room they are in
# currently.
directionMap = { 'n': 'north', 's':'south', 'e': 'east', 'w': 'west'}
class Player:
    def __init__(self, room, name="chicken little", keys=[], win=False):
        self.name = name
        self.room = room
        self.keys = keys
        self.win = win
    def countKeys(self):
        print(f'Congrats {self.name}, you\'ve found this keys:')
        for i in self.keys:
            print(i)
        print(f'Total: {len(self.keys)} out of 1')
    def __str__(self):
        return f'''\n\tName: {self.name}\n\tRoom: {self.room}\n\tKeys: {self.keys} \n'''
    def getItem(self):
            self.keys.append(self.room.keys.pop(self.room.keys.index('golden')))
    def dropItem(self):
            self.room.keys.append(self.keys.pop(self.keys.index('golden')))
    def move(self, direction):
            # print('direction:', direction, 'golden' in self.keys )
            print(f'\n\n\n You\'ve choosen to go {directionMap.get(direction)}...\n')
            nextRoom = getattr(self.room, f'{direction}_to', None)
            if nextRoom is None:
                print(f'There is nothing in this direction, so you go back...')
            elif nextRoom.name == 'treasure':
                if 'golden' in self.keys:
                    self.room = nextRoom
                    print(f'\t\nYou find yourself {self.room.title}, you use the key to open it')
                    print(f'\t\n{self.room.description}')
                    print(f'\t\nEnd of the game for our hero {self.name}')
                    self.win = True
                else:
                    print(f'You find a massive vault door, it\'s locked and it seems to need a key')
                    print(f'to open, you go back trying to search for the key.\n')
            else:
                self.room = nextRoom
                    