"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: Generate a Python script that connects to a database for managing student records in a technical education institution like I.E.S.T.P. Trentino Juan Pablo II.
Generated: DETERMINISTIC_0f075a660d12cf3e
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from sqlite3 import Error

class StudentDatabase:
    """A class to manage student records in a SQLite database."""

    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create a table for storing student records."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Student table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_student(self, name, age, course):
        """Add a new student record to the database."""
        sql = '''INSERT INTO students(name, age, course) VALUES(?,?,?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, age, course))
            self.connection.commit()
            print(f"Student {name} added successfully.")
        except Error as e:
            print(f"Error adding student: {e}")

    def get_students(self):
        """Retrieve all student records from the database."""
        sql = '''SELECT * FROM students'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error retrieving students: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    # Database file path
    database = "students.db"

    # Create a StudentDatabase instance
    student_db = StudentDatabase(database)

    # Create the students table
    student_db.create_table()

    # Add sample students
    student_db.add_student("Alice Johnson", 20, "Computer Science")
    student_db.add_student("Bob Smith", 22, "Information Technology")

    # Retrieve and print all students
    students = student_db.get_students()
    print("Student Records:")
    for student in students:
        print(student)

    # Close the database connection
    student_db.close_connection()
```
