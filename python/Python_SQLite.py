import sqlite3
conn = sqlite3.connect('sqlite.db')
print("Opened database successfully")
conn.execute('''
      Create table student(
          st_id int AUTO_INCREMENT PRIMARY KEY ,
          st_name VARCHAR(50),
          st_class VARCHAR(10),
          st_email VARCHAR(30)

      )
''')
conn.close()