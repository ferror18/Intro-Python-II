# Implement a class to hold room information. This should have name and
# description attributes.
x = "Theres nothing is this direction"
class Room:
    def __init__(self, name, title, description, items=[]):
        self.name = name
        self.title = title
        self.description = description
        self.items = items
    def __str__(self):
        return f'''
            \t\tName: {self.name}
            \t\tTitle: {self.title}
            \t\tDescription: {self.description}
            \t\titems: {self.items}'''
    def searchRoom(self):
        print(f'You\'ve searched in {self.name}...')
        print(f'Congrats, you\'ve found this items:\n')
        for i in self.items:
            print(f' - {i} \n')
        print(f'\nUse "get [item name]" or "drop  [item name]" to get/drop these items\n\n')