# Implement a class to hold room information. This should have name and
# description attributes.
x = "Theres nothing is this direction"
class Room:
    def __init__(self, name, title, description, keys=[]):
        self.name = name
        self.title = title
        self.description = description
        self.keys = keys
    def __str__(self):
        return f'''
            \t\tName: {self.name}
            \t\tTitle: {self.title}
            \t\tDescription: {self.description}
            \t\tKeys: {self.keys}'''
    def searchRoom(self):
        print(f'You\'ve searched in {self.name}...')
        print(f'Congrats, you\'ve found this keys:')
        for i in self.keys:
            print(f' - {i} \n')
        print(f'\nUse "get" or "drop" to get/drop these items\n\n')