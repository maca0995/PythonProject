
numbers = [1,2,4,-6,7,8,100,-125,11,123]
for number in numbers:
    if number<0:
        continue
    print (number)

names = ["Petr", "Ales", "Honza", "Lenka", "Andrea", "Alice"]
i = 0
while i < len(names):
    if names[i] == "Alice":
        break
    print(names[i])
    i+=1
random_codes = ["1-okdsaaa", "0-nFnldd", "0-AA", "0-uwqqq", "2-ZSTh", "0-RKOcsxxx", "1-LwWtss"
, "0-cdKiddd", "2KpAAaa", "3-sOdSxhcds"]
new_list = [code for code in random_codes if "0" in code]
print(new_list)


