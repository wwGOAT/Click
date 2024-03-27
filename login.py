from connect_db import Database
import person
from main import main

def login_2(balance):
    card_number = input("Card Number: ")
    while len(card_number) != 16:
        print("Bunday yoza olmaysiz")
        card_number = input("Card Number: ")
    password = input("Password: ")

    query = "SELECT card_number, password FROM click"
    data = Database.connect(query, "select")
    for i in data:
        if card_number == i[0] and password == i[1]:
            return person.person(card_number, password, balance)
        else:
            print("\nError")
            return login()
    return main()

def login():
    print("\n<<<<<<<<<<<Login>>>>>>>>>>>>\n")

    query = "SELECT * FROM click"
    return login_2(query)