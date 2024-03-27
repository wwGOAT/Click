from connect_db import Database

def create_table():
    click = """
        CREATE TABLE click(
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            email VARCHAR(50),
            password VARCHAR,
            telephone_number BIGINT NOT NULL,
            card_number BIGINT NOT NULL,
            balance NUMERIC NOT NULL,
            create_date TIMESTAMP DEFAULT now())
            """

    data = {
        "click": click
    }

    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")


if __name__ == "__main__":
    create_table()