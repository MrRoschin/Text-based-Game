from character import Enemy
from cave import Cave

cavern = Cave("Cavern")
grotto = Cave("Grotto")
dungeon = Cave("Dungeon")

cavern.set_description("A damp and dirty cave.\nYou hear the sound of dripping water.\nThe rocks feel slightly slimy to the touch.")
grotto.set_description("A small grotto with a pool of water in the center.\nThe walls are covered in moss and the air is humid.")
dungeon.set_description("A dark and eerie dungeon.\nThe air is cold and you can hear distant echoes of water dripping.\nVines hang from the cracked bricks and the torches are burnt out.\nThe metal gates guarding the empty rooms are rusty and crooked.\nCobwebs cover the corners and drawings are carved into the walls.")

cavern.link_cave("Dungeon", "south")
grotto.link_cave("Dungeon", "east")
dungeon.link_cave("Grotto", "west")
dungeon.link_cave("Cavern", "north")

harry = Enemy("Harry", "A smelly and hairy Wumpus")
harry.set_conversation("Hangry… Hanggrry")
harry.set_weakness("artifact acid")
dungeon.set_character(harry)


current_cave = cavern
dead = False
while dead == False:
    print("\n")
    current_cave.get_details()
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    current_cave = current_cave.move(command)
    if command in ["north", "south", "east", "west"]:
            current_cave = current_cave.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                # What happens if you win?
                print("Bravo,hero you won the fight!")
                current_room.set_character(None)
            else:
                print("Scurry home, you lost the fight.")
        else:
            print("There is no one here to fight with")