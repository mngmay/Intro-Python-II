from room import Room
from player import Player

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

# print("Room after linking: ", room['narrow'].n_to)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

name = input("What is your adventurer's name?: ")
player = Player(name, room['outside'])
print(f"Welcome {player.name}!")
# print(player.current_room.name)
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

valid_cmds = ['s', 'n', 'e', 'w', 'q']

game = True

while game:
    # print the current room name and description
    print(
        f"You are currently in the {player.current_room.name}")
    cmd = input("Enter a direction (n, s, w, e) to move, or 'q' to quit: ")
    # Break out of the loop
    if cmd in valid_cmds:
        direction = f"{cmd}_to"
        # grabs current_room of player, looks for direction attribute, defaults to None if invalid.
        new_room = getattr(player.current_room, direction, None)
        if new_room:
            player.current_room = new_room
        elif cmd == "q":
            print("Goodbye!")
            game = False
        else:
            print("There is no room that way.")
    else:
        print("Invalid command.")
