def is_adult(age):
    return age >= 18
def is_name_valid(username):
    return len(username) >= 4
def create_user(username, age, email):
    if not is_name_valid(username):
        return {"success": False, "error": "Username musi mit alespon 4 znaky"}
    if not is_adult(age):
        return {"success": False, "error": "Uzivatel musi byt dospely"}
    user = {
        "username": username,
        "age": age,
        "email": email,
    }
    return{"success": True, "user": user}
def print_user_info(result):
    if result["success"]:
        user = result["user"]
        print("Uzivatel:")
        print("Jmeno:", user["username"])
        print("Vek:", user["age"])
        print("Email:", user["email"])
        print()
    else:
        print("Chyba:", result["error"])
        print()
users = []

users.append(create_user("Martin", 25, "martin@email.cz"))
users.append(create_user("Eva", 30, "eva@email.cz"))
users.append(create_user("Tom",17, "tom@email.cz"))
users.append(create_user("Anna", 22, "anna@email.cz"))
for user in users:
    print_user_info(user)


