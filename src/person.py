class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def fullname(self):
        return self.first_name + " " + self.last_name