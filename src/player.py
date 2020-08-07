# Write a class to hold player information, e.g. what room they are in
# currently.
directionMap = { 'n': 'north', 's':'south', 'e': 'east', 'w': 'west'}
class Player:
    def __init__(self, room, name="chicken little", items=[], win=False):
        self.name = name
        self.room = room
        self.items = items
        self.win = win
    def countItems(self):
        print(f'\nCongrats {self.name}, you\'ve found this items so far:\n')
        for i in self.items:
            print(f' - {i} \n')
        print(f'Total: {len(self.items)} out of 1\n')
    def __str__(self):
        return f'''\n\tName: {self.name}\n\tRoom: {self.room}\n\tItems: {self.items} \n'''
    def getItem(self, item=None):
        if item is None:
            print(f'Please provide an item name like so --> get example')
        elif item not in self.room.items:
            print(f'You do not have item --> {item}')
        else:
            print(f'You collected item --> {item}! \n\n')
            self.items.append(self.room.items.pop(self.room.items.index(item)))
    def dropItem(self, item=None):
        if item is None:
            print(f'Please provide an item name to drop like so --> drop example')
        elif item not in self.items:
            print(f'You do not have item --> {item}')
        else:
            print(f'You dropped the item --> {item}! \n\n')
            self.room.items.append(self.items.pop(self.items.index(item)))
    def move(self, direction):
            # print('direction:', direction, 'golden' in self.items )
            print(f'\n\n\n You\'ve choosen to go {directionMap.get(direction)}...\n')
            nextRoom = getattr(self.room, f'{direction}_to', None)
            if nextRoom is None:
                print(f'There is nothing in this direction, so you go back...')
            elif nextRoom.name == 'treasure':
                if 'key' in self.items:
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
                    