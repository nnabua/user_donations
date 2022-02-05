def login(database, username, password):
    while True:
        if username in database:
            if database[username] == password:
                print("\nWelcom back", username)
                return(username, password)

            else:
                print("\nWrong password")
                return ""
        else:
            print("\nUser not found. Please Register.")
            return ""


def register(database, username):
    while True:
        if username in database:
            print("\nUsername already registered")
            return ""
        else:
            print(f"\nUsername {username} registered!")
        break
