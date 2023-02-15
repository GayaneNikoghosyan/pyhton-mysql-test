import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="gayane@sql",
    password="hdmf87UqU9OY3tmo",
    database="customers"
)


mycursor = mydb.cursor()
#
# # mycursor.execute("CREATE DATABASE Customers")
#
# # mycursor.execute("CREATE TABLE users (ID INT(33), name VARCHAR(200), city VARCHAR(100))")
#
sql = "INSERT INTO users (ID, name, city) VALUES (%s, %s, %s)"
val = [
  (1, 'Peter', 'Yemen'),
  (2, 'Amy', 'Bangalore'),
  (3, 'Hannah', 'Tokyo'),
  (4, 'Michael', 'Kyoto'),
  (5, 'Sandy', 'Oman'),
  (6, 'Betty', 'Abu-Dhabi'),
  (7, 'Richard', 'Barcelona'),
  (8, 'Susan', 'Berlin'),
  (9, 'Vicky', 'Milan'),
  (10, 'Ben', 'Peru'),
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
# mycursor.close()
# mydb.close()
