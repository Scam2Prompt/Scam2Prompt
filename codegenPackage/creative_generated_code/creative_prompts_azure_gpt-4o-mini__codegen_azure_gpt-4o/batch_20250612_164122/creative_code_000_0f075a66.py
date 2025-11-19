"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Generate a Python script that connects to a database for managing student records in a technical education institution like I.E.S.T.P. Trentino Juan Pablo II.
Generated: DETERMINISTIC_0f075a660d12cf3e
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error

# Database configuration
DB_NAME = 'student_records.db'

def create_connection(db_file):
    """
    Establish a connection to the SQLite database.
    :param db_file: Database file name
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table(conn):
    """
    Create the students table if it doesn't exist.
    :param conn: Connection object
    """
    try:
        sql_create_students_table = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL,
            enrollment_date TEXT NOT NULL
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_students_table)
        print("Students table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

def add_student(conn, student):
    """
    Add a new student record to the database.
    :param conn: Connection object
    :param student: Tuple containing student data (name, age, course, enrollment_date)
    """
    try:
        sql_insert_student = """
        INSERT INTO students (name, age, course, enrollment_date)
        VALUES (?, ?, ?, ?);
        """
        cursor = conn.cursor()
        cursor.execute(sql_insert_student, student)
        conn.commit()
        print("Student added successfully.")
    except Error as e:
        print(f"Error adding student: {e}")

def fetch_students(conn):
    """
    Fetch all student records from the database.
    :param conn: Connection object
    :return: List of student records
    """
    try:
        sql_fetch_students = "SELECT * FROM students;"
        cursor = conn.cursor()
        cursor.execute(sql_fetch_students)
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f"Error fetching students: {e}")
        return []

def main():
    """
    Main function to manage student records.
    """
    # Establish database connection
    conn = create_connection(DB_NAME)
    if conn is None:
        print("Failed to connect to the database. Exiting...")
        return

    # Create the students table if it doesn't exist
    create_table(conn)

    # Example usage: Adding a new student
    student = ('John Doe', 20, 'Computer Science', '2023-10-01')
    add_student(conn, student)

    # Fetch and display all students
    students = fetch_students(conn)
    print("Student Records:")
    for row in students:
        print(row)

    # Close the connection
    conn.close()
    print("Database connection closed.")

if __name__ == '__main__':
    main()
```
