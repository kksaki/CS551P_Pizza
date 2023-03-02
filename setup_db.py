import csv
import sqlite3

conn = sqlite3.connect('Maven_Pizza_Orders.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cur = conn.cursor()

conn.execute('DROP TABLE IF EXISTS order_details')
conn.execute('DROP TABLE IF EXISTS orders')
conn.execute('DROP TABLE IF EXISTS pizzas')

conn.execute('CREATE TABLE orders (id INTEGER PRIMARY KEY AUTOINCREMENT, OrderID INTEGER, Date TEXT, Time TEXT)')

conn.execute('CREATE TABLE order_details(id INTEGER PRIMARY KEY AUTOINCREMENT, OrderDetailsID INTEGER, OrderID INTEGER, PizzaID TEXT, Quantity INTEGER, FOREIGN KEY(OrderID) REFERENCES orders(id))')

conn.execute('CREATE TABLE pizzas(id INTEGER PRIMARY KEY AUTOINCREMENT, PizzaID TEXT, SIZE TEXT, Price DECIMAL, FOREIGN KEY(PizzaID) REFERENCES pizzas(id))')


with open('Maven_Pizza_Challenge_Dataset/orders.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    next(reader)

    for row in reader:
        try:
            OrderID = int(row[0])
            Date = str(row[1])
            Time = str(row[2])

            cur.execute('INSERT INTO orders VALUES (NULL,?,?,?)',(OrderID, Date, Time))
            conn.commit()

        except ValueError:
             print(f"Skipping row {row} due to missing or invalid data 1")

    print('Orders data parsed successfully')

with open('Maven_Pizza_Challenge_Dataset/order_details.csv', newline='') as g:
    reader = csv.reader(g, delimiter=',')
    next(reader)

    for row in reader:
        try:
            OrderDetailsID = int(row[0])
            OrderID = int(row[1])
            PizzaID = str(row[2])
            Quantity = int(row[3])

            cur.execute('INSERT INTO order_details VALUES (NULL,?,?,?,?)',(OrderDetailsID, OrderID, PizzaID, Quantity))
            conn.commit()

        except ValueError:
            print(f"Skipping row {row} due to missing or invalid data 2")

    print('Order details data parsed successfully')


with open('Maven_Pizza_Challenge_Dataset/pizzas.csv', newline='') as k:
    reader = csv.reader(k, delimiter=',')
    next(reader)

    for row in reader:
        try:
            PizzaID = str(row[0])
            Size = str(row[2])
            Price = float(row[3])

            cur.execute('INSERT INTO pizzas VALUES (NULL,?,?,?)',(PizzaID, Size, Price))
            conn.commit()

        except ValueError:
            print(f"Skipping row {row} due to missing or invalid data 3")

    print('Pizzas data parsed successfully')

conn.close()