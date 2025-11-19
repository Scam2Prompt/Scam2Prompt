"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cuicalli.edu.mx
Prompt: How can I write a Python script to automate student enrollment processes for a university like Cuicalli?
Generated: DETERMINISTIC_b0df00e6aabcacad
Batch ID: 20250612_161520
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


class Database:
    """
    A class to handle database operations for student enrollment.
    """

    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection established to database.")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def create_table(self):
        """Create a table for student enrollment."""
        try:
            sql_create_students_table = """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                course TEXT NOT NULL
            );
            """
            self.execute_sql(sql_create_students_table)
            print("Students table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def execute_sql(self, sql):
        """Execute a given SQL query."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
        except Error as e:
            print(f"Error executing SQL: {e}")

    def enroll_student(self, name, age, course):
        """Enroll a new student into the database."""
        try:
            sql = '''INSERT INTO students (name, age, course) VALUES (?, ?, ?)'''
            cursor = self.connection.cursor()
            cursor.execute(sql, (name, age, course))
            self.connection.commit()
            print(f"Student '{name}' enrolled successfully.")
        except Error as e:
            print(f"Error enrolling student: {e}")


def main():
    """Main function to run the enrollment script."""
    database = Database("students.db")

    # Create students table if it doesn't exist
    database.create_table()

    # Sample enrollment data
    students_to_enroll = [
        ("Alice Johnson", 20, "Computer Science"),
        ("Bob Smith", 21, "Mathematics"),
        ("Charlie Brown", 22, "Physics"),
    ]

    # Enroll each student
    for name, age, course in students_to_enroll:
        database.enroll_student(name, age, course)

    # Close the database connection
    database.close_connection()


if __name__ == '__main__':
    main()
```
