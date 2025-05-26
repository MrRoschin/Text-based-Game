from cave import Cave

cavern = Cave("cavern")
cavern.set_description("A damp and dirty cave.\nYou hear the sound of dripping water.\nThe rocks feel slightly slimy to the touch.")
cavern.describe()
cavern.link_cave("dungeon", "south")

grotto = Cave("grotto")
grotto.set_description("A small grotto with a pool of water in the center.\nThe walls are covered in moss and the air is humid.")
grotto.link_cave("dungeon", "east")

dungeon = Cave("dungeon")
dungeon.set_description("A dark and eerie dungeon.\nThe air is cold and you can hear distant echoes of water dripping.\nVines hang from the cracked bricks and the torches are burnt out.\nThe metal gates guarding the empty rooms are rusty and crooked.\nCobwebs cover the corners and drawings are carved into the walls.")
dungeon.link_cave("grotto", "west")
dungeon.get_details()