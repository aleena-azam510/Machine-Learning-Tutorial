import sqlite3
conn = sqlite3.connect("sqlite.db")
data = conn.execute("SELECT * FROM student") 
for n in data:
    print(n[0],n[1],n[2],n[3])
print("")
print("")
st_name = input("enter the student name: ")
st_class = input("enter the class name: ")
data = conn.execute("SELECT * FROM student where st_name like '%"+st_name+"%' and   st_class = '"+st_class+"' ")
for n in data:
    print(n[0],n[1],n[2],n[3])
