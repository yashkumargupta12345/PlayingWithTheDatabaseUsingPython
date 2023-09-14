import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query columns
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)


# Insert new rows
new_rows = [('Cats', 'Cat city', '2088.10.17'),
            ('Hens', 'Hens city', '2088.10.17')]

cursor.executemany("INSERT INTO EVENTS VALUES(?,?,?)", new_rows)
connection.commit()

# display the data into the table
cursor.execute("select * from events")
rows = cursor.fetchall()
print(rows)
