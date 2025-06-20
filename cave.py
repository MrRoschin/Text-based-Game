class Cave():
    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None
        self.linked_caves = {}
        self.character = None
        self.item = None

    def get_description(self):
        return self.description
    
    def set_description(self, cave_description):
        self.description = cave_description

    def get_name(self):
        return self.name
    
    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def describe(self):
        print(self.description)
    
    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link

    def get_details(self):
        print(self.name)
        print("---------------------------")
        print(self.description)
        for direction in self.linked_caves:
            cave = self.linked_caves[direction]
            print(f"The {cave.get_name()} is {direction}.")

        if self.character is not None:
            self.character.describe()
   
    def move(self, direction):
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print(f"You can't go {direction} from here.")
            return self

    def get_item(self):
        return self.item
    
    def set_item(self, item_name):
        self.item = item_name

    def describe(self):
        print(f"{self.name}: {self.description}")