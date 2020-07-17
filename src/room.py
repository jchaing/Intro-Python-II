# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, n_to='', s_to='', e_to='', w_to=''):
        self.name = name
        self.description = description
        # self.items = items
        # self.n_to = self
        self.n_to = self
        self.s_to = self
        self.e_to = self
        self.w_to = self

    def __str__(self):
        return f"{self.name}, {self.description}"
