#Nina Forlini
#sorry that this is both late and unfinished im sorry

print("Hearing the chattering voices, you try to calm yourself. \n"
    "Slowly the voices seem to get smaller; further away. \n"
      "Was this a dream? It couldn't have been. not with everything dying. \n\n"
      "Not with that...\n"
      "\x1B[3mthing...\x1B[0m\n"
      "Out there. It's taken so many. \n\n"
      "All you can do is focus on the village head's words \n"
      "They replay in your head, again and again. \n\n"
      "They've been drawing a lottery over the last few weeks. \n"
      "The village hadn't had much luck with the Nuckelavee. \n"
      "The men have gone to try to kill the monster.\n"
      "When they don't succeed, they become food to please it."
      "\n\n"
      "There's been a lot of sacrifices to the Nuckelavee \n"
      "And \x1B[3myou're\x1B[0m about to be the next one")
print("\n")
# Dictionary for all the items in each room of the world
rooms = {
     "Outside": ["Cliffside"],
     "Floor 1": ["Room 1"],
     "Floor 2": ["Room 2", "Room 3"],
     "Floor 3": ["Room 4", "Room 5"],
     "Floor 4": ["Room 6", "Room 7"],
      "Floor 5": ["Room 8"],
      "Basement": ["Room 9"]
}
items = {
    "Cliffside": [],
    "Room 1": [],
    "Room 2": ["matches"],
    "Room 3": ["sword"],
    "Room 4": ["cloak"],
    "Room 5": ["jar of freshwater"],
    "Room 6": ["dry seaweed"],
    "Room 7": ["bandages"],
    "Room 8": ["key"],
    "Room 9": []
}

#variable to track players location
player_location = rooms["Outside"][0]

#directional commands
command_list = "open, close, left, right, forward, back, up, down, take, drop, look, unlock, leave, enter lighthouse, help"

#inventory
inv = []

print("You see the lighthouse were the Nuckelavee has taken up ahead,\n"
      "Reaching the door, fear trembles you as you think of the options you have:\n"
      )
#######
user_input = ""
while user_input != "enter lighthouse":
    user_input = input("What will you do?\n").lower()
    if user_input == "help":
        print(command_list)
    elif user_input == "enter lighthouse":
        print("You step into the lighthouse\n"
              "The lighthouse is damp and dark,\n"
              "The musty smell shows the lighthouses age.\n"
              "It shows that humans haven't been here for a long time...\n")
        player_location = rooms["Floor 1"][0]
    elif user_input == "leave":
        print("You have chosen to abandon the lottery,\n"
              "You leave but cannot return to your home...\n"
              "You have lost the game, Thank you for playing!")
        quit()
    elif user_input == "look":
        print("You see the lighthouse were the Nuckelavee has taken up ahead,\n"
              "Reaching the door, fear trembles you as you think of the options you have:\n")
    else:
        print("This is not an option")


print("In this room, you see two doors,\n"
      "One on the left with a heavy lock on it, \nAnd another on the right, seemingly unlocked.\n")
user_input = ""
while user_input != "open right door":
    user_input = input("What will you do?\n").lower()
    if user_input == "help":
        print(command_list)
    elif user_input == "look":
        print("In this room, you see two doors,\n"
      "One on the left with a heavy lock on it, \nAnd another on the right, seemingly unlocked.\n")
    elif user_input == "open right door":
        print("You climb the creaky stairs and are let out into an open room\n\n"
              "The room, this first floor, \nIt looks to be split into two rooms\n")
        player_location = rooms["Floor 2"][0]
    elif user_input == "open left door":
        print("The old handle jiggles but does not move, the lock is sturdy,\n"
              "The only thing to unlock it is a key,\n")
    else:
        print("This is not an option.")


#2nd floor
user_input = ""
print("It shows that humans haven't been here for a long time... \n"
      "It has both a door on the right and what looked to be a pack of matches on the floor...")
while user_input != "open door" or user_input != "open right door":
    user_input = input("What will you do? \n").lower()
    if user_input == "help":
        print(command_list)
    elif user_input == "look" and not "matches" in inv:
        print("It shows that humans haven't been here for a long time... \n"
              "It has both a door and what looked to be a pack of matches on the floor...")
    elif user_input == "look" and "matches" in inv:
        print("It shows that humans haven't been here for a long time... \n"
              "There is a door on the right.")
    elif user_input == "take matches" and "matches" in inv:
        print("You have already taken those!\nYou're slightly worried they wont light...")
    elif user_input == "take matches" and not "matches" in inv:
        print("You take the matches, they're slightly damp \n"
              "From the moisture that lingers in the air \n"
              "You're slightly worried they won't light")
        inv.append("matches")
    elif user_input == "open door" or user_input == "open right door":
        print("You open the door, it leads to another room on this floor.\n")
        break
        player_location = rooms["Floor 2"][1]############################
    else:
        print("This is not an option.")

user_input = ""
print("The door lets out into a room with a sword leaning against a bookshelf\n"
      "and a door on the right.\n")
while user_input != "open door" or user_input != "open right door":
    user_input = input("What will you do? \n").lower()
    if user_input == "help":
        print(command_list)
    elif user_input == "look" and not "sword" in inv:
        print("The door lets out into a room with a sword leaning against a bookshelf\n"
              "and a door on the right.\n")
    elif user_input == "look" and "sword" in inv:
        print("It shows that humans haven't been here for a long time... \n"
              "There is a door on the right.")
    elif user_input == "take sword" and "sword" in inv:
        print("You have taken the sword already! \n")
    elif user_input == "take sword" and not "sword" in inv:
        print("you look at the sword, inspecting it there is an almost unnatural sheen to it.\n"
              "You take it, it might some in handy!\n")
        inv.append("sword")
    elif user_input == "open door" or "open right door":
        print("You climb the creaky stairs and are let out into an open room\n\n"
              "The room, this first floor, \nIt looks to be split into two rooms\n")
        break
        player_location = rooms["Floor 3"][0]
    else:
        print("This is not an option.")

#3rd floor
user_input = ""
print("The stairwell lets out into a room in the next floor,\n"
      "There is a door on the left, one that seem to have a cloak hanging from the hinges\n")
while user_input != "open door" or user_input != "open left door":
    user_input = input("What will you do? \n").lower()
    if user_input == "help":
        print(command_list)
    elif user_input == "look" and not "cloak" in inv:
        print("The stairwell lets out into a room in the next floor,\n"
              "There is a door on the left, one that seem to have a cloak hanging from the hinges\n")
    elif user_input == "look" and "cloak" in inv:
        print("It shows that humans haven't been here for a long time... \n"
              "There is a door on the right.")
    elif user_input == "take cloak" and "cloak" in inv:
        print("You have taken the cloak already! \n")
    elif user_input == "take cloak" and not "cloak" in inv:
        print("You grab the cloak,\nIt feels heavy in your hands,\nIt may add some needed protection.")
        inv.append("cloak")
    elif user_input == "open door" or "open left door":
        print("You open the door, let out into the next room\n")
        break
        player_location = rooms["Floor 3"][1]
    else:
        print("This is not an option.")
#3rd floor
user_input = ""
print("The door lets out into the next room,\n"
      "There is a bed with a small end-table next to it in the corner.\n"
      "Upon closer inspection, there looks to be a jar of water there. There is also a door on the left.\n")
while user_input != "open door" or user_input != "open left door":
    user_input = input("What will you do? \n").lower()
    if user_input == "help":
        print(command_list)
    elif user_input == "look" and not "jar of freshwater" in inv:
        print("The door lets out into the next room,\n"
              "There is a bed with a small end-table next to it in the corner.\n"
              "Upon closer inspection, there looks to be a jar of water there. There is also a door on the left.\n")
    elif user_input == "look" and "jar of freshwater" in inv:
        print("It shows that humans haven't been here for a long time... \n"
              "There is a door on the left.")
    elif user_input == "take jar" and "jar of freshwater" in inv:
        print("You have taken the jar already! \n")
    elif user_input == "take jar" and not "jar of freshwater" in inv:
        print("You grab the jar,\nIt doesn't smell like the salt-water you know,\nIt is freshwater.")
        inv.append("jar of freshwater")
    elif user_input == "open door" or "open left door":
        print("You climb the creaky stairs and are let out into an open room\n"
              "It looks to be split into two rooms\n")
        break
        player_location = rooms["Floor 4"][0]
    else:
        print("This is not an option.")


user_input = ""
print("The door lets out into a room with table.\n"
      "On it, is few plants, most dead and withered,\n"
      "Some dried, still attached to their long dead roots\n"
      "Nestled in all of the plants sit a morter and pestle and a few scattered sachets of dry seaweed\n"
      "And a door on the right.\n")
while user_input != "open door" or user_input != "open right door":
    user_input = input("What will you do? \n").lower()
    if user_input == "help":
        print(command_list)
    elif user_input == "look" and not "dry seaweed" in inv:
        print("The door lets out into a room with table.\nOn its few plants, most dead and withered,\n"
              "Some dried, still attached to their long dead roots\n"
              "Nestled in all of the plants sit a morter and pestle and a few scattered sachets.\n"
              "And a door on the right.\n")
    elif user_input == "look" and "dry seaweed" in inv:
        print("It shows that humans haven't been here for a long time... \n"
              "There is a door on the right.")
    elif user_input == "dry seaweed" and "dry seaweed" in inv:
        print("You have taken the dry seaweed already! \n")
    elif user_input == "take dry seaweed" and not "dry seaweed" in inv:
        print("You look at the table.\n"
              "Grabbing the few leaves, you grind them.\n"
              "They leave a dark green powder\n"
              "You fill a few sachets with it\n")
        inv.append("dry seaweed")
    elif user_input == "open door" or "open right door":
        print("You open the door, let out into the next room.\n")
        break
        player_location = rooms["Floor 4"][1]
    else:
        print("This is not an option.")


print("You enter into the next room, their seem to be medical supplies lying around and a table.\n"
      "It is large enough to a man to lay on, what happened here?\n"
      "You see some bandages lying around and a door.\n")
while user_input != "open door" or user_input != "open right door":
    user_input = input("What will you do? \n").lower()
    if user_input == "help":
        print(command_list)
    elif user_input == "look" and not "bandages" in inv:
        print("You enter into the next room, their seem to be medical supplies lying around and a table.\n"
              "It is large enough to a man to lay on, what happened here?\n"
              "You see some bandages lying around and a door.\n")
    elif user_input == "look" and "bandages" in inv:
        print("It shows that humans haven't been here for a long time... \n"
              "There is a door on the right.")
    elif user_input == "bandages" and "bandages" in inv:
        print("You have taken the bandages already! \n")
    elif user_input == "take bandages" and not "bandages" in inv:
        print("You look at the table.\nYou grab the few bandages.\n")
        inv.append("bandages")
    elif user_input == "open door" or "open right door":
        print("You climb the creaky stairs and are let out into an open room\n\n")
        break
        player_location = rooms["Floor 5"][0]
    else:
        print("This is not an option.")


#5th floor
print("You have reached the top of the lighthouse.\nYou can see almost nothing in the pitch black of the night.\n"
      "The light looks like it hasn't been lit in a very long time.\nLooking around you see a key,\n"
      "Near the now dead light on the floor.") #################################################this is where i stopped
while user_input != "open door" or user_input != "open right door":
    user_input = input("what will you do? \n").lower()
    if user_input == "help":
        print(command_list)
    elif user_input == "take key" and not "key" in inv:
        print("The key feels rough, bubbled from the age and rust that is eating away at it\n")
    elif user_input == "look" and "key" in inv:
        print("You start thinking of your decent\n")
    elif user_input == "take key" and "key" in inv:
        print("You have taken the key already! \n")
        inv.append("key")
    elif user_input == "go back" or "open right door":
        print("You open the door.\n")
        player_location = rooms["Floor 1"][0]
        break
    else:
        print("This is not an option.")
#decent
print("Now you begin your decent, with every step you feel the dread builing.\n"
      "You know you will have to fight this monster.\n"
      "How many have died before you trying to live?\n"
      "How many have been claimed, killed, to satisfy the Nuckelavee?\n"
      "Your thoughts consume you as you move, almost robotically to the start.\n"
      "To the heavy lock that you know is the only thing holding your death at bay.")
while user_input == input("what will you do? \n").lower():
    if user_input == "help":
        print(command_list)
    elif user_input== "unlock" and "key" in inv:
        print("The heavy, old, rusted padlock creaks.\n"
              "Its years of being maintained by the cleaners, show how often the lock has been relocked\n"
              "How many times someone has died here\n")
        player_location = rooms["Basement"]
    elif user_input == "unlock" and not "key" in inv:
        print("The lock is old and rusted,\n"
              "heavy to keep the monster at bay\n"
              "Find the key")
    elif user_input == "leave":
        print("You have chosen to abandon the lottery,\n"
              "You leave but cannot return to your home...\n"
              "You have lost the game, Thank you for playing!")

#basement
print("The basement is dark and has an unnatural chill to it.\n"
      "The door is open, giving a bit of light in the otherwise pitch black room.\n"
      "You move in further\n"
      "You hear breathing as you feel your light eclipse as the Nuckelavee moves being you.\n"
      "Breaking out into a cold sweat you turn around to face it\n"
      "\n"
      "\n"
      "Beast was a good word to describe this spirit.\n"
      "It was a mass of flesh and tendon.\n"
      "A cyclops horse with a human torso fused to it, riding in a perverse night hunt\n"
      "The arms of the 'human' were unnaturally long, almost dragging on the floor\n"
      "with long fingers that could be compared to talons"
      "You see the veins in the muscles, they were the only reality that show this wasn't a made up being\n"
      "\n"
      "\x1BThat it could be killed.\x1B"
      "\n"
      "\n"
      "\n"
      "The horse gnashed and the 'human' let out an unnatural screech as it came at you.\n"
      "Growing up in the small village, you never learned sword-play; it wasn't as useful as farming\n"
      "The Nuckelavee knocks you down, its hot breathe reeking in your face as it uses its arms to hold you down\n"
      "Fear grips you as you inch your hand into your pocket\n"
      "Gripping the few sachets you put there, you pull one out, the cloak providing you enough wiggle room.\n"
      "The Nuckelavee's face is getting closer with its mouth opening.\n"
      "In that instant, you toss the sachet into its mouth and it bites down reactively.\n"
      "It lets out a shriek of pain and launches away from you, the sachet burning the horse mouth\n"
      "Taking the jar of water out of your cloak, you pour it on the sword, hoping that it will help the blade some\n"
      "\n"
      "\n"
      "You run at the creature, sword drawn, throwing another sachet with your other hand.\n"
      "The sachet breaks open, releasing a find mist of dried seaweed over the creature.\n"
      "Closing the gap, you plunge the sword into the breast-plate of the horse-man\n"
      "The sound is something you will never forget.\n"
      "\n"
      "\n"
      "You did it. You killed the Nuckelavee\n"
      "You saved anyone else from having to win the lottery\n"
      "The curdling scream of the Nuckelavee would haunt you for the rest of your days\n"
      "You have truly won the lottery...")
