import sqlite3
            
# Membuat koneksi ke database
connection = sqlite3.connect('movie.db')

cursor = connection.cursor()

cursor.execute('''
SELECT * FROM movies
WHERE title LIKE 'Harry Potter%';
''')

result = cursor.fetchall()


num = 0
for row in result:
    num += 1
    print(num, row)
