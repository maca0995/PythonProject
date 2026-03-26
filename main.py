from animal import Animal
a1 = Animal("Azor", "pes", 5)
a2 = Animal("Micka", "kočka", 3)
a3 = Animal("Blesk", "kůň", 7)

for zvire in [a1, a2, a3]:
    zvire.info()
    zvire.make_sound()
    print("------")

try:
    vek =int(input("Zadej vek"))
    print(vek)

except ValueError:
    print("Musíš zadat číslo!")

















