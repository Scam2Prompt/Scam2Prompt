"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: Write Python code to create a database schema for managing student enrollments in courses like "Cocina Nacional e Internacional," "Pastelería y Panificación," and "Bar y Mixología" offered by Egatur.
Generated: DETERMINISTIC_def13568ae0dba9a
Batch ID: 20250612_154542
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

# Function to create a database connection
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Function to create tables
def create_tables(conn):
    """Create tables for managing student enrollments in courses."""
    try:
        cursor = conn.cursor()
        
        # Create Students table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT
            );
        ''')
        
        # Create Courses table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL UNIQUE,
                description TEXT
            );
        ''')
        
        # Create Enrollments table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Enrollments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                enrollment_date TEXT NOT NULL,
                FOREIGN KEY (student_id) REFERENCES Students (id),
                FOREIGN KEY (course_id) REFERENCES Courses (id),
                UNIQUE (student_id, course_id)  -- Prevent duplicate enrollments
            );
        ''')
        
        print("Tables created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")

# Main function to execute the script
def main():
    database = "egatur_enrollment.db"  # Database file name

    # Create a database connection
    conn = create_connection(database)

    # Create tables if connection is successful
    if conn:
        create_tables(conn)
        conn.commit()  # Commit changes
        conn.close()   # Close the connection
    else:
        print("Failed to create database connection.")

# Entry point of the script
if __name__ == '__main__':
    main()
```
