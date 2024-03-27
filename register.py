from connect_db import Database
import login


def register():
    print("Register Page")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    password_1 = input("Password: ")
    password_2 = input("Reply Password: ")
    while password_1 != password_2:
        print("\nPasswordlar to'g'ri kelmadi\n")
        password_1 = input("Password: ")
        password_2 = input("Reply Password: ")
    telephone_number = input("Telephone Number: ")
    card_number = input("Card Number: ")
    while len(card_number) != 16:
        print("Bunday yoza olmaysiz")
        card_number = input("Card Number: ")
    balance = int(0)

    query = f"""INSERT INTO click(first_name, last_name, email, password, telephone_number, card_number, balance)
            VALUES('{first_name}', '{last_name}', '{email}', '{password_2}', {telephone_number}, {card_number}, {balance})"""

    print(Database.connect(query, "insert"))
    return login.login()