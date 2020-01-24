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
room['outside'].e_to = None
room['outside'].w_to = None
room['outside'].s_to = None

room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = None
room['foyer'].s_to = room['outside']

room['overlook'].n_to = None
room['overlook'].e_to = None
room['overlook'].w_to = None
room['overlook'].s_to = room['foyer']

room['narrow'].n_to = room['treasure']
room['narrow'].e_to = None
room['narrow'].w_to = room['foyer']
room['narrow'].s_to = None

room['treasure'].n_to = None
room['treasure'].e_to = None
room['treasure'].w_to = None
room['treasure'].s_to = room['narrow']

#
# Main
#
def move(player):
    # Write a loop that:
    #
    # * Prints the current room name
    #print(player.room)
    # print(player.room.room_name)
    # * Prints the current description (the textwrap module might be useful here).
    
    # * Waits for user input and decides what to do.    
    dir = input("Enter a direction: ").lower()
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    valid_dirs = ["n", "e", "s", "w", "q"]
    if dir not in valid_dirs:
        print("Sorry, that's not a valid direction.\
             Please enter: 'N', 'E', 'W', 'S', or 'Q'")
        move(player)       
    if dir=='n':
        if player.room.n_to == None:
            print("Sorry, You can't move forward in this direction.")
        else :
            new_location = player.room.n_to
            player = Player(new_location)
            print(player.room.room_name)
        move(player)
                        
    if dir=='s':
        if player.room.s_to == None:
            print("Sorry, You can't move forward in this direction.")
        else :
            new_location = player.room.s_to
            player = Player(new_location)
            print(player.room.room_name)
            
        move(player)
                        
    if dir=='e':
        if player.room.e_to == None:
            print("Sorry, You can't move forward in this direction.")
        else :
            new_location = player.room.e_to
            player = Player(new_location)
            print(player.room.room_name)
        move(player)
    if dir=='w':
        if player.room.w_to == None:
            print("Sorry, You can't move forward in this direction.")
        else :
            new_location = player.room.w_to
            player = Player(new_location)
            print(player.room.room_name)
        move(player)

    # If the user enters "q", quit the game.
    if dir=='q':
        print('You are quitting the game!') 
        sys.exit()       

# Make a new player object that is currently in the 'outside' room.
player=Player(room['outside'])    
move(player)
