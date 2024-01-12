import mysql.connector


connection = mysql.connector.connect(
    host="localhost", user="user", password="password", database="db"
)

print(connection)

cursor = connection.cursor()

# CREATE
food_title = "Ramen"
food_description = "Delicious"
food_price = 11.99
query = f"""
INSERT INTO menu (title, description, price)
VALUES
    ("{food_title}", "{food_description}", {food_price})
"""
cursor.execute(query)
connection.commit()

# READ
query = "SELECT * FROM menu"
cursor.execute(query)
result = cursor.fetchall()
print(result)

# UPDATE
old_title = "pizza"
new_title = "Pizza"
new_description = "Neapolitan Pizza"
id = 1
query = f"""
UPDATE menu SET description = "{new_description}"
WHERE ID = {id}
"""

cursor.execute(query)
connection.commit()

# DELETE
id = 2
query = f"""
DELETE FROM menu WHERE ID = {id}
"""
cursor.execute(query)
connection.commit()

# FINALIZE
cursor.close()
connection.close()
