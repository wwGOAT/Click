from connect_db import Database
from main import main
def person(card_number, password, balance):
    print("<<<<<<<<<Person>>>>>>>>>>")
    service = input("""
    1. Ma'lumotlar
    2. Pul o'tkazish
    0. Orqaga
            >>>""")

    if service == "1":
        query = "SELECT * FROM click"
        data = Database.connect(query, "select")

        for i in data:
            if i[6] == card_number and i[4] == password:
                print(f"""
                ID: {i[0]}
                First_name: {i[1]}
                Last_name: {i[2]}
                Email: {i[3]}
                Password: {i[4]}
                Telephone_number: {i[5]}
                Card_number: {i[6]}
                Balance: {i[7]}
                Create_date: {i[8]}
                """)
            else:
                print("\nError")
                return person(card_number, password, balance)
            return person(card_number, password, balance)

    elif service == "2":
        card = input("Enter card number: ")
        query = "SELECT card_number FROM click"
        data = Database.connect(query, "select")
        for i in data:
            if {i[0]} == card:
                summa = input("Summani kiriting: ")
                if summa <= balance:
                    print("Xizmat yakunlandi")
                else:
                    print("Kartada mablag' yetarli emas!\n Iltimos hisobingizni to'ldiring")
                    return person(card_number, password, balance)
            else:
                print("\nBunday karta mavjud emas")
                return person(card_number, password, balance)
            return person(card_number, password, balance)

    elif service == "0":
        return main()

    else:
        print("Error")
        return person(card_number, password, balance)