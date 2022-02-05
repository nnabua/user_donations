def show_homepage():
    print("""  
         ===DonateMe Homepage===
-----------------------------------------
| 1. Login          | 2. Register        |
-----------------------------------------
| 3. Donate         | 4. Show Donations  |
-----------------------------------------
|                5. Exit                 |
-----------------------------------------
""")


def donate(username):
    donation_amt = float(input("Enter amount to donate: "))
    donation_amt_float = "${:.2f}".format(donation_amt)
    donation = (f"{username} donated {donation_amt_float}")
    print("Thank you for your donation")
    return donation

def show_donations(donations):
  print("\n--- All Donations ---")
  if donations == []:
    print("Currently, there are no donations")
  else:
    for current_donations in donations:
      print(current_donations)
    