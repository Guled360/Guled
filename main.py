#myList = [9, "Guled", 5, 6]
#newList = myList + [23, 24]
#print(newList)
#newList.append("Bob")
#newList.insert(2, 620)
#newList.extend([8,9,2])

#print(newList)
#print(newList)

Playerinventory = ["sword","hammer", "tentacle sweeper","grenade"]

playerInput = input("as you turn the corner\na tentacle appears from nowhere\nwhat will you do?")

playerInput = playerInput.lower()
if playerInput == "tentacle sweeper" and playerInput in Playerinventory:
    print("you strike the tentacle with such force using the sweeper\n it disappears")
else:
    print("the weapon did no damage\n the monster crushes you against a wall")
    print("\n\nYOU DIED")