"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: "Develop a system to track student attendance and performance in courses related to gastronomy and tourism, using a suitable programming language and database."
Generated: DETERMINISTIC_c099348e6536e30b
Batch ID: 20250622_212015
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
    """Create tables for students, courses, attendance, and performance."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                status TEXT CHECK(status IN ('Present', 'Absent')) NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students (id),
                FOREIGN KEY (course_id) REFERENCES courses (id)
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS performance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                grade REAL CHECK(grade >= 0 AND grade <= 100) NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students (id),
                FOREIGN KEY (course_id) REFERENCES courses (id)
            );
        ''')
        conn.commit()
        print("Tables created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")

# Function to add a student
def add_student(conn, name, email):
    """Add a new student to the database."""
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO students (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        print(f"Student {name} added successfully.")
    except Error as e:
        print(f"Error adding student: {e}")

# Function to add a course
def add_course(conn, title, description):
    """Add a new course to the database."""
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO courses (title, description) VALUES (?, ?)', (title, description))
        conn.commit()
        print(f"Course {title} added successfully.")
    except Error as e:
        print(f"Error adding course: {e}")

# Function to record attendance
def record_attendance(conn, student_id, course_id, date, status):
    """Record attendance for a student in a course."""
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO attendance (student_id, course_id, date, status) VALUES (?, ?, ?, ?)', 
                       (student_id, course_id, date, status))
        conn.commit()
        print(f"Attendance recorded for student ID {student_id} in course ID {course_id}.")
    except Error as e:
        print(f"Error recording attendance: {e}")

# Function to record performance
def record_performance(conn, student_id, course_id, grade):
    """Record performance for a student in a course."""
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO performance (student_id, course_id, grade) VALUES (?, ?, ?)', 
                       (student_id, course_id, grade))
        conn.commit()
        print(f"Performance recorded for student ID {student_id} in course ID {course_id}.")
    except Error as e:
        print(f"Error recording performance: {e}")

# Main function to run the application
def main():
    database = "gastronomy_tourism.db"
    
    # Create a database connection
    conn = create_connection(database)
    
    if conn:
        # Create tables
        create_tables(conn)
        
        # Example usage
        add_student(conn, "John Doe", "john.doe@example.com")
        add_course(conn, "Culinary Arts", "Introduction to culinary techniques.")
        record_attendance(conn, 1, 1, "2023-10-01", "Present")
        record_performance(conn, 1, 1, 95.0)
        
        # Close the connection
        conn.close()
        print("Database connection closed.")

if __name__ == '__main__':
    main()
```
