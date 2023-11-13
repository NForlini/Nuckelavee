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

#how to call on dict, 0 is the index for matches
# floor2_all_rooms = rooms["Floor 2"]
# room2_item1 = items["Room 2"][0]
print(items["Room 2"][0])
#YO INVENTORY
inv = []
#oldest = 0
