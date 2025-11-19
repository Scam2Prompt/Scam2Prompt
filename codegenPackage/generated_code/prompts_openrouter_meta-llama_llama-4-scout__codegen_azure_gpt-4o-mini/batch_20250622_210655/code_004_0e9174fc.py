"""
Generated Code Metadata:
========================
Original URL: https://kiddooplayway.com
Prompt: Design a simple database schema to store information about students, teachers, and activities offered by a play school like Kiddoo Playway, and write a Python script to interact with this database.
Generated: DETERMINISTIC_0e9174fcc45b4e07
Batch ID: 20250622_210655
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

# Database connection function
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
    """Create tables for students, teachers, and activities."""
    try:
        cursor = conn.cursor()
        
        # Create Students table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                parent_contact TEXT NOT NULL
            );
        ''')
        
        # Create Teachers table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS teachers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                subject TEXT NOT NULL,
                contact TEXT NOT NULL
            );
        ''')
        
        # Create Activities table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS activities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                teacher_id INTEGER,
                FOREIGN KEY (teacher_id) REFERENCES teachers (id)
            );
        ''')
        
        conn.commit()
        print("Tables created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")

# Function to add a student
def add_student(conn, name, age, parent_contact):
    """Add a new student to the students table."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO students (name, age, parent_contact)
            VALUES (?, ?, ?);
        ''', (name, age, parent_contact))
        conn.commit()
        print(f"Student {name} added successfully.")
    except Error as e:
        print(f"Error adding student: {e}")

# Function to add a teacher
def add_teacher(conn, name, subject, contact):
    """Add a new teacher to the teachers table."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO teachers (name, subject, contact)
            VALUES (?, ?, ?);
        ''', (name, subject, contact))
        conn.commit()
        print(f"Teacher {name} added successfully.")
    except Error as e:
        print(f"Error adding teacher: {e}")

# Function to add an activity
def add_activity(conn, name, description, teacher_id):
    """Add a new activity to the activities table."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO activities (name, description, teacher_id)
            VALUES (?, ?, ?);
        ''', (name, description, teacher_id))
        conn.commit()
        print(f"Activity {name} added successfully.")
    except Error as e:
        print(f"Error adding activity: {e}")

# Main function to run the script
def main():
    database = "kiddoo_playway.db"
    
    # Create a database connection
    conn = create_connection(database)
    
    if conn:
        # Create tables
        create_tables(conn)
        
        # Example data insertion
        add_student(conn, "Alice Johnson", 4, "555-1234")
        add_teacher(conn, "Mr. Smith", "Art", "555-5678")
        add_activity(conn, "Painting", "Creative painting sessions", 1)
        
        # Close the connection
        conn.close()
        print("Database connection closed.")

if __name__ == '__main__':
    main()
```
