from room import Room
from player import Player
from item import Item

# Items

items = {
    "sword": Item("sword", "2 handed broad sword"),
    "mace": Item("mace", "Large blunt hammer"),
    "book": Item("book", "Spellbook to increase power"),
    "axe": Item("axe", "Large 2 handed dwarven axe"),
    "shield": Item("shield", "Dragon shield"),
    "potion": Item("potion", "Recovers health to 100%"),
}

# Declare all the rooms

room = {
    "outside": Room(
        "Outside Cave Entrance", "North of you, the cave mount beckons", [items["mace"]]
    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
        [],
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        [items["shield"], items["book"]],
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
        items["axe"],
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        [items["potion"]],
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]


#
# Main
#

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

player_create = str(input("Create a player name: "))
player = Player(player_create, room["outside"], [items["sword"]])
print(f"Welcome {player.name}")
print("--------------------------------------")
print(player.current_room.name)
print(player.current_room.description)
print("--------------------------------------")


# Empty string for player_input
player_input = ""

# Checks new location input if it has room attribute, then returns new room
def check_new_location(direction, current_location):
    attr = f"{direction}_to"
    if hasattr(current_location, attr):
        return getattr(current_location, attr)


def take_item(item_selection, current_player):
    # Checks for item in room
    for item in current_player.current_room.items:
        # If item is in room, add to inventory and remove from room list
        if item.name == item_selection:
            current_player.items.append(item)
            current_player.current_room.items = [
                item
                for item in current_player.current_room.items
                if item.name != item_selection
            ]
            return True


def drop_item(item_selection, current_player):
    # check if item is in inventory
    for item in current_player.items:
        if item.name == item_selection:
            # if item is in inventory, add to room list and remove from inventory
            current_player.current_room.items.append(item)
            current_player.items = [
                item for item in current_player.items if item.name != item_selection
            ]
            return True


while player_input != "q":

    # Input Selection
    player_input = str(
        input(
            "Choose a direction: [n] North [e] East [s] South [w] West [i] inventory [q] Quit\nOr enter [get] [item] / [drop] [item]\n"
        ).lower()
    )

    parse_selection = player_input.split(" ")

    # checks if user enters 1 word: direction, inventory or quit
    if len(parse_selection) == 1:
        # Cardinal Direction input
        if (
            player_input == "n"
            or player_input == "s"
            or player_input == "w"
            or player_input == "e"
        ):
            new_location = check_new_location(player_input, player.current_room)
            if new_location:
                player.current_room = new_location
                print("-------------------------------------")
                print(
                    f"{player.name} heads {player_input} and enters {player.current_room.name}, {player.current_room.description}"
                )
                print("-------------------------------------")
            else:
                print(
                    f"{player.name} tries to head {player_input}, but cannot go that way"
                )

        # displays players inventory
        elif player_input == "i":
            if len(player.items) > 0:
                print([item.name for item in player.items])
            else:
                print(f"{player.name}'s inventory is empty")

        # quit the game
        elif player_input == "q":
            print(f"Sorry to see you go, {player.name}. Come back soon!")

        # invalid selection
        else:
            print(f"Invalid selection, please try again!")

    # if user enters 2 words, determine if get or drop item
    elif len(parse_selection) == 2:
        if parse_selection[0] == "get":
            # process input for take_item function
            take = take_item(parse_selection[1], player)
            # if success, call on_take method to print the result
            if take:
                print(items[parse_selection[1]].on_take())
            # else, print error
            else:
                print(
                    f"{player.current_room.name} doesn't contain {parse_selection[1]}"
                )
        elif parse_selection[0] == "drop":
            # process input for drop_item function
            drop = drop_item(parse_selection[1], player)
            # if success, call on_drop method to print result
            if drop:
                print(items[parse_selection[1]].on_drop())
            # else, print error
            else:
                print(f"{player.name} does not have {parse_selection[1]}")
        else:
            print(f"{player.name} made an invalid command, try again!")
    else:
        print(f"{player.name} made an invalid input.")
