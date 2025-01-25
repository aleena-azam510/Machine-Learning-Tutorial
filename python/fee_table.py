import sqlite3

def create_fees_table():
    """Creates a 'fees' table with student_id as primary key (auto-increment)."""

    conn = sqlite3.connect('sqlite.db')  # Connect to the database (creates if it doesn't exist)
    cursor = conn.cursor()

    # Create the table with student_id as primary key and auto-increment
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fees (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            fee_amount REAL
        )
    ''')

    # Insert initial fee records for student IDs 1 to 8
    for i in range(1, 9):
        cursor.execute("INSERT INTO fees (fee_amount) VALUES (?)", (1000.0,))  # Assuming initial fee is 1000

    conn.commit()  # Save changes to the database
    conn.close()

if __name__ == "__main__":
    create_fees_table()
    print("Fees table created successfully!")