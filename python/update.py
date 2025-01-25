import sqlite3
conn = sqlite3.connect("sqlite.db")
conn.execute = ('''
              update student set st_name = 'elsa' where st_id=3

''')
conn.commit()
conn.close()