from room import Room
from player import Player
from item import Item

# Declare items

item = {'chicken': Item(
    "Chicken", "Golden and fried to perfection, this piece of poultry is delicious on its own or paired with a waffle."),
    'shoes': Item("Shoes", "Perfect for protecting your feet and keeping that hipster vibe. Not great for arch support."),
    'glasses': Item("Glasses", "Black rimmed and lookin hip. Just the thing to view an overlook with."),
    'wrapper': Item("Wrapper", "Looks like it had something cool in it but someone must have gotten to it first. You snooze you lose.")}


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item['chicken'], item['shoes']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item['glasses']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item['wrapper']]),
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

game = True

while game:
    # print the current room name and description
    print(
        f"You are currently in the {player.current_room.name}. {player.current_room.description}.")
    # print the items in a room
    if len(player.current_room.items) > 0:
        print("This room has the following items:")
        for i, item in enumerate(player.current_room.items, start=1):
            print(
                f"{i}) {item.name}: {item.description}")

    else:
        print("There are no items here.")

    # prompt player for direction
    cmd = input("What would you like to do? \n n: Move North \n s: Move South \n e: Move East \n w: Move West  \n get <item name>: Pick up an item \n drop <item name>: Drop an item \n q: Quit the game \n Your selection: ")

    valid_cmds = ['s', 'n', 'e', 'w', 'q', 'get', 'take', 'drop']
    action = cmd.split()[0]

    # if the first word entered is a valid command
    if action in valid_cmds:
        direction = f"{cmd}_to"
        # grabs current_room of player, looks for direction attribute, defaults to None if invalid.
        new_room = getattr(player.current_room, direction, None)

        if new_room:
            player.current_room = new_room
        elif action == 'get' or action == 'take':
            # if there is an item followed by the command check to see if the item is in the room
            if len(cmd.split()) > 1 and len(cmd.split()) < 3:
                requested_item = cmd.split()[1].lower()
                valid_items = getattr(
                    player.current_room, "items")
                grabbed_item = False
                for i in valid_items:
                    # if the requested item is in the room add it to player's inventory and remove it from the room's items list
                    if i.name.lower() == requested_item:
                        print("matches!!!")
                        print("before", player.inventory,
                              player.current_room.items)
                        player.inventory.append(i)
                        player.current_room.items.remove(i)
                        print("after", player.inventory,
                              player.current_room.items)
                        grabbed_item = True
                        break
                if grabbed_item == False:
                    print("That item is not in the room.")

            else:
                print("You need to include an item after your get command.")
        elif action == 'drop':
            if len(cmd.split()) > 1:
                print("Valid drop command", cmd)
            else:
                print("You need to include an item after your get command.")
        elif cmd == "q":
            print("Goodbye!")
            game = False
        else:
            print("There is no room that way.")
    else:
        print("Invalid command.")
