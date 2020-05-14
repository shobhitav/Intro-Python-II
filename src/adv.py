from room import Room
from player import Player
import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player=Player("Ninja",room['outside'])

print(f'Welcome {player.name} to the adventure game .\n Current room is :  {player.current_room}')

def move(player, new_room):
    if new_room==None:
        # Print an error message if the movement isn't allowed.
        print("Sorry, You can't move forward in this direction.")
    else: 
        player.current_room=new_room
        print(f'You have entered {player.current_room}')


# Write a loop that:
while(True):
    #  * Prints the current room name
    print(f'{player.current_room.name}')
    # * Prints the current description (the textwrap module might be useful here).
    print(f'{player.current_room.description}')
    # * Waits for user input and decides what to do.
    direction = input("Enter a direction. Choose from  n for north, s for south , e for east, w for west or q for quit :")
    # If the user enters a cardinal direction, attempt to move to the room there.
    if direction == 'n':
        move(player, player.current_room.n_to)
    elif direction == 'e':
        move(player, player.current_room.e_to)
    elif direction == 'w':
        move(player, player.current_room.w_to)
    elif direction == 's':
        move(player, player.current_room.s_to)
    else:
        sys.exit(0)
