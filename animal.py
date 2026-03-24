class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def info(self):
        print(f"Jmeno: {self.name}")
        print(f"Druh: {self.species}")
        print(f"Vek: {self.age} let")

    def make_sound(self):
        if self.species == "pes":
            print("Haf haf")
        elif self.species == "kočka":
            print("Mnau")
        elif self.species == "kůň":
            print("iha")
        else:
            print("neznamy zvuk")

