vek = int(input("zadej svůj věk: "))
zustatek = float(input("zadej svůj zůstatek peněz  (Kč): "))
cena_piva = float(input("Zadej cenu piva (Kč):"))
print("\n--- Vyhodnocení ---")
if  vek < 18:
    print("Nemuzes si koupit pivo - nejsi plnolety/a.")
elif zustatek < cena_piva:
    print("nemuzes si koupit pivo - nemas dostatek penez")
else:
    zustatek -= cena_piva
    print("muzes si koupit pivo ")
    print("Zustatek po nakupu:", zustatek, "Kc")
