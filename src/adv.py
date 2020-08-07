from room import Room
from player import Player
import sys, os

# Declare all the rooms
# hOpt = {
#     "name": sys.args[1] if len(sys.argv) >= 2 else None
# }
clear = lambda: os.system('clear')
room = {
    'outside':  Room("outside","Outside a Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("foyer", "in a Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("overlook", "at a Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['key']),

    'narrow':   Room("narrow","in a Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("treasure","at the Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
# print(hOpt)
#
# Main
#
Hero = Player(room['outside'])
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print(f'''
    Welcome {Hero.name} the Hero!, \n
    collect the 4 mystic keys to open the treasure after you find it to win.
    There is a total of 4 keys, water, fire, earth and wind.
    Collect all of them to open the treasure once you've found it.
    If you can open the treasure you can find eternal glory! 
    (Yes like in harry potter part IV) Good Luck!
''')
while True:
    # print(Hero)
    if Hero.room.name == 'treasure':
        pass
    else:
        print(f'CURRENT ROOM : {Hero.room.name.upper()}\n\n\n\n')
        print(f'You find yourself {Hero.room.title}, \n{Hero.room.description}\n')
    action = str(input(''' 
        \n\n \t What to do next?
        n -> Go north
        s -> Go south
        e -> Go east
        w -> Go west
        i -> To check items
        s -> Search this room for items
        q -> quit
    '''))
    if action == 'q':
        print('Ok see you later.')
        break
    elif 'get' in action:
        if len(Hero.room.items) == 0:
            clear()
            print('There is no items to get in this room \n\n')
            
        else:
            clear()
            Hero.getItem(action.split()[1])
    elif 'drop' in action:
        if len(Hero.items) == 0:
            clear()
            print('There is no items to drop \n\n')
            
        else:
            clear()
            Hero.dropItem(action.split()[1])
    elif action == 'i':
        if len(Hero.items) == 0:
            clear()
            print('You don\'t have any items \n\n')
            
        else:
            clear()
            Hero.countItems()
    elif action == 'search':
        if len(Hero.room.items) == 0:
            clear()
            print('There is no items in this room\n\n')
            
        else:
            clear()
            Hero.room.searchRoom()
    else:
        clear()
        Hero.move(action)
        if Hero.win:
            break
        
        
        
