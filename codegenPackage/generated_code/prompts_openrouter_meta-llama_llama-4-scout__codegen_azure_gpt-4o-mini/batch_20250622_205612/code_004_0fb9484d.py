"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: "Create a basic structure for a school management system using a database, including tables for students, teachers, and courses, reflecting the bilingual education system of Del Sol Montessori."
Generated: DETERMINISTIC_0fb9484d0fad6b09
Batch ID: 20250622_205612
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3

# Database connection and setup
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_tables(conn):
    """Create tables for students, teachers, and courses."""
    try:
        cursor = conn.cursor()
        
        # Create Students table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                date_of_birth DATE NOT NULL,
                language_preference TEXT NOT NULL
            );
        ''')
        
        # Create Teachers table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS teachers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                subject TEXT NOT NULL,
                language TEXT NOT NULL
            );
        ''')
        
        # Create Courses table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_name TEXT NOT NULL,
                teacher_id INTEGER,
                FOREIGN KEY (teacher_id) REFERENCES teachers (id)
            );
        ''')
        
        conn.commit()
        print("Tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

def main():
    """Main function to set up the database and create tables."""
    database = "school_management_system.db"
    
    # Create a database connection
    conn = create_connection(database)
    
    # Create tables if connection is successful
    if conn:
        create_tables(conn)
        conn.close()
        print("Database connection closed.")
    else:
        print("Failed to create database connection.")

if __name__ == '__main__':
    main()
```
