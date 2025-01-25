import sqlite3
conn = sqlite3.connect("sqlite.db")
print("STUDENT ID","STUDENT NAME","STUDENT FEES")
data = conn.execute("SELECT f.student_id,s.st_name,f.fee_amount FROM fees as f  inner join student as s on f.student_id=s.st_id")
for a in data:
    print(a)
conn.close