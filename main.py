from character import Enemy, Friend
from character import Character
from cave import Cave
from item import Item

def print_menu():
    print("\nWhat would you like to do?")
    print("Options:")
    print(" - Move [north/south/east/west]")
    print(" - talk")
    print(" - fight")
    print(" - pat")
    print(" - search")
    print(" - take")
    print(" - distract")
    print(" - inventory")
    print(" - quit")

cavern = Cave("Cavern")
grotto = Cave("Grotto")
dungeon = Cave("Dungeon")

cavern.set_description("A damp and dirty cave.\nYou hear the sound of dripping water.\nThe rocks feel slightly slimy to the touch.")
grotto.set_description("A small grotto with a pool of water in the center.\nThe walls are covered in moss and the air is humid.")
dungeon.set_description("A dark and eerie dungeon.\nThe air is cold and you can hear distant echoes of water dripping.\nVines hang from the cracked bricks and the torches are burnt out.\nThe metal gates guarding the empty rooms are rusty and crooked.\nCobwebs cover the corners and drawings are carved into the walls.")

cavern.link_cave(dungeon, "south")
grotto.link_cave(dungeon, "east")
dungeon.link_cave(grotto, "west")
dungeon.link_cave(cavern, "north")

harry = Enemy("Harry", "A smelly and hairy Wumpus")
harry.set_conversation("Hangry… Hanggrry")
harry.set_weakness("artifact acid")
dungeon.set_character(harry)

josephine = Friend("Josephine", "A friendly bat")
josephine.set_conversation("Gidday")
grotto.set_character(josephine)

honey_jar = Item("Jar of Honey")
honey_jar.set_description("A jar filled with sweet, sticky honey. A tasty and distracting treat for the Wumpus!")
cavern.set_item(honey_jar)

artifact_acid = Item("Artifact Acid")
artifact_acid.set_description("A mysterious acid that is extracted from ancient artifacts. It is the Wumpus's weakness.")
dungeon.set_item(artifact_acid)

bag = []
harry_distracted = False
honey_found = False
acid_found = False

artifact_acid_attempts = 0

current_cave = cavern
dead = False

# Print details and inhabitant description once at the start
print("\n")
current_cave.get_details()

while not dead:
    print_menu()
    command = input("> ").strip().lower()
    inhabitant = current_cave.get_character()

    #search command for honey jar in cavern
    if command == "search":
        item = current_cave.get_item()
        if item is not None:
            item.describe()
        else:
            print("Nothing can be found here.")

        # if current_cave == cavern and not honey_found:
        #     print("You have found a Jar of Honey!")
        #     bag.append("Jar of Honey")
        #     honey_found = True
        
        # elif current_cave == cavern and honey_found:
        #     print("Nothing can be found in this area.")

    elif command == "inventory":
        if bag:
            print("You have: " + ", ".join(bag))
        else:
            print("Your bag is empty.")

    #distract command for Harry in Dungeon
    elif command == "distract":
        if current_cave == dungeon and inhabitant is not None and isinstance(inhabitant, Enemy):
            if "Jar of Honey" in bag and not harry_distracted:
                print("Harry is enjoying himself... for now...")
                harry_distracted = True
                bag.remove("Jar of Honey")

    #prevent moving from Dungeon if Harry is not distracted or defeated
    elif command in ["north", "west"]:
        if current_cave == dungeon and inhabitant is not None and isinstance(inhabitant, Enemy) and not harry_distracted:
            print("Harry blocks your way! You must distract or defeat him to proceed.")
        else:
            current_cave = current_cave.move(command)
            print("\n")
            current_cave.get_details()

    #allow moving south or east as normal
    elif command in ["south", "east"]:
        current_cave = current_cave.move(command)
        print("\n")
        current_cave.get_details()

    #take command for Artifact Acid in Grotto (after Harry is distracted)
    elif command == "take":
        item = current_cave.get_item()
        if item is not None:
            if item.get_name() == "Artifact Acid" and not harry_distracted:
                artifact_acid_attempts += 1
                if artifact_acid_attempts >= 2:
                    print("You are too slow to distract Harry! He catches you and he enjoys his meal...")
                    print("G A M E   O V E R")
                    dead = True
                else:
                    print("Harry is preventing you from proceeding! You must do something before it's too late...")
            else:
                print("You put the " + item.get_name() + " in your bag")
                bag.append(item.get_name())
                if item.get_name() == "Artifact Acid":
                    acid_found = True
                current_cave.set_item(None)
        else:
            print("Nothing can be found in this area.")

    elif command == "look":
        print("\n")
        current_cave.get_details()
        inhabitant = current_cave.get_character()
        if inhabitant is not None:
            inhabitant.describe()

    elif command == "talk":
        # Talk to the inhabitant - check whether there is one
        if inhabitant is not None:
            inhabitant.talk()

        else:
            print("There is no one here to talk to")

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with) == True:
                    print("Bravo, hero! You won the fight!")
                    current_cave.set_character(None)
                    harry_distracted = True
                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have survived another adventure!")
                        dead = True

                    current_cave(None)
                else:
                    print("Scurry home, you lost the fight.")
                    print("G A M E   O V E R")
                    dead = True
            else:
                print("You don't have " + fight_with.title() + ".")
        else:
            print("There is no one here to fight with")

    elif command == "pat":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you…")
            else:
                inhabitant.pat()
        else:
            print("There is no one here to pat :(")

    elif command == "take":
        item = current_cave.get_item()
        if item is not None:
            print("You put the " + item.get_name() + " in your bag")
            bag.append(item.get_name())
            current_cave.set_item(None)
        else:
            print("There is nothing to take here")

    else:
        print("I don't understand that command.")