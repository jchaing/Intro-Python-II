class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        return f"You picked up {self.name}: {self.description}"

    def on_drop(self):
        return f"You dropped {self.name}"

    def __str__(self):
        return f"Item: {self.name}, Description: {self.description}"
