import sqlite3
conn = sqlite3.connect('sqlite.db')
data = conn.execute("SELECT * FROM student limit 0,5") #We use SQLite Limit Clause to retrieve the data that we want, which means we are going to just use the LIMIT VALUE to fetch the limited data. 
for n in data:
    print(n[0],n[1],n[2],n[3])
