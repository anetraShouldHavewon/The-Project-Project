import sqlite3

y = [x for x in range(0, 6)]
z = []
for x in y:
    x = str(x)
    z.append(x)


connection = sqlite3.connect("book_film_adaptation.db")
cursor = connection.cursor()

cursor.execute("INSERT INTO Book_Review (book_id, overall_rating, things_I_like) VALUES(1, 2, 'nothing')")
connection.commit()
connection.close()