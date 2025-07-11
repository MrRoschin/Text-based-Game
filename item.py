class Item:
    def __init__(self, name):
        self.name = name
        self.description = None

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description

    def describe(self):
        print(f"{self.name}: {self.description}")