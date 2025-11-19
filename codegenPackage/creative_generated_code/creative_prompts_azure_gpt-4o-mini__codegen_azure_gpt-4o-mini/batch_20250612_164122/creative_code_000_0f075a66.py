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

class DatabaseManager:
    """A class to manage database connection and operations."""

    def __init__(self, db_file):
        """Initialize the DatabaseManager with the database file path."""
        self.connection = None
        self.db_file = db_file
        self.connect()

    def connect(self):
        """Establish a database connection."""
        try:
            self.connection = sqlite3.connect(self.db_file)
            print("Connection to the database established.")
        except Error as e:
            print(f"Error while connecting to database: {e}")

    def create_table(self):
        """Create a table for student records if it doesn't exist."""
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
            cursor = self.connection.cursor()
            cursor.execute(sql_create_students_table)
            print("Students table created successfully.")
        except Error as e:
            print(f"Error while creating table: {e}")

    def add_student(self, name, age, course, enrollment_date):
        """Insert a new student record into the students table."""
        try:
            sql_insert_student = """
            INSERT INTO students (name, age, course, enrollment_date)
            VALUES (?, ?, ?, ?);
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_insert_student, (name, age, course, enrollment_date))
            self.connection.commit()
            print("Student added successfully.")
        except Error as e:
            print(f"Error while adding student: {e}")

    def get_students(self):
        """Fetch all student records from the students table."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM students;")
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error while fetching students: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

def main():
    """Main function to run the database manager."""
    db_manager = DatabaseManager("students.db")
    db_manager.create_table()

    # Example usage
    db_manager.add_student("John Doe", 20, "Computer Science", "2023-09-01")
    db_manager.add_student("Jane Smith", 22, "Information Technology", "2023-09-01")

    students = db_manager.get_students()
    print("Student Records:")
    for student in students:
        print(student)

    db_manager.close_connection()

if __name__ == "__main__":
    main()
```
