import mysql.connector
import json

mydb = mysql.connector.connect(
    host="localhost",
    user="gayane@sql",
    password="hdmf87UqU9OY3tmo",
    database="customers"
)

mycursor = mydb.cursor()

sqlFormula = "INSERT INTO users (ID, name, city) VALUES (%s, %s, %s)"

with open('new_data.json', encoding="utf8") as json_file:
    data = json.load(json_file)


    print(data)
    for i, item in enumerate(data):
        ID = item.get("ID")
        print(ID)
        name = item.get("name")
        print(name)
        city = item.get("city")
        print(city)

        mycursor.execute(sqlFormula, (ID,	name, city))
        mydb.commit()

# mycursor.execute(sqlFormula, data)

