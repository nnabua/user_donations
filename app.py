from donations_pkg import homepage, user

database = {"admin": "password123"}
donations = []
authorized_user = ""

homepage.show_homepage()

if len(authorized_user) == 0:
    print("You must be logged in to donate.")

while True:
    options = int(input("\nChoose an option: "))
    if options == 1:
        global username
        username = input("\nEnter username: ")
        global password
        password = input("Enter password: ")
        authorized_user = user.login(database, username, password)
    elif options == 2:
        username = input("\nEnter username: ")
        password = input("Enter password: ")
        authorized_user = user.register(database, username)
        if authorized_user != "":
          database[username] = password
    elif options == 3:
        if authorized_user != "":
          donations.append(homepage.donate(username))
        else:
            print("You're not logged in")
    elif options == 4:
        homepage.show_donations(donations)
    elif options == 5:
        print("Leaving DonateMe")
        break
    continue
