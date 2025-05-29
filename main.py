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

current_cave = cavern
while True:
    print("\n")
    current_cave.get_details()
    command = input("> ")
    current_cave = current_cave.move(command)