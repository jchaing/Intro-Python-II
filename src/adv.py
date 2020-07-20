from room import Room
from player import Player

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
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

# player_create = str(input("Create a player name: "))
player = Player("JJ", room["outside"])


# current_room = room['outside']

# character = Player(current_room)

move = ""


def check_new_location(direction, current_location):
    attr = f"{direction}_to"
    # print(f"current_location, {current_location}")
    # print(f"attr, {attr}")
    if hasattr(current_location, attr):
        return getattr(current_location, attr)


print(f"Welcome {player.name}")
print(player.current_room.name)
print(player.current_room.description)

while move != "q":
    # Movement Selection
    move = str(
        input(
            "Choose a direction: [n] North [e] East [s] South [w] West [q] Quit\n"
        ).lower()
    )

    # Cardinal Direction
    if move == "n" or move == "s" or move == "w" or move == "e":
        new_location = check_new_location(move, player.current_room)
        # print(new_location)
        if new_location:
            player.current_room = new_location
            print(
                f"{player.name} heads {move} and enters {player.current_room.name}, {player.current_room.description}"
            )
        else:
            print(f"{player.name} tries to head {move}, but cannot go that way")

    # Quit the game
    elif move == "q":
        print(f"{player.name} is a quitter. Come back soon!")

    else:
        print(f"Invalid selection, please try again!")

# while move != "q":
#     if move == "n":
#         player.current_room = player.current_room.n_to
#         if print(player.current_room) == print(player.current_room.n_to):
#             print("You cannot go that way")
#         else:
#             print(player)
#         # print(player.current_room)
#         # print("---------------------")
#         # print(player.current_room.n_to)
#     elif move == "s":
#         player.current_room = player.current_room.s_to
#         # print(player.current_room)
#     elif move == "w":
#         player.current_room = player.current_room.w_to
#     elif move == "e":
#         player.current_room = player.current_room.e_to
#     else:
#         print("You cannot go that way")
#     # print(player)

# print('You quitter')
