"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: "Develop a system for tracking student attendance and performance in a modular certification program like the one offered at Trentino Institute."
Generated: DETERMINISTIC_fdacdcdb0bc468cc
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime

# Database setup
def create_database():
    """Create a SQLite database for tracking student attendance and performance."""
    conn = sqlite3.connect('student_attendance_performance.db')
    cursor = conn.cursor()
    
    # Create tables for students, attendance, and performance
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            attendance_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            date TEXT NOT NULL,
            status TEXT CHECK(status IN ('Present', 'Absent')) NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students (student_id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS performance (
            performance_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_name TEXT NOT NULL,
            score INTEGER CHECK(score BETWEEN 0 AND 100) NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students (student_id)
        )
    ''')
    
    conn.commit()
    conn.close()

# Function to add a new student
def add_student(name, email):
    """Add a new student to the database."""
    try:
        conn = sqlite3.connect('student_attendance_performance.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO students (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Error: A student with email {email} already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Function to record attendance
def record_attendance(student_id, status):
    """Record attendance for a student."""
    try:
        conn = sqlite3.connect('student_attendance_performance.db')
        cursor = conn.cursor()
        date = datetime.now().strftime('%Y-%m-%d')
        cursor.execute('INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)', (student_id, date, status))
        conn.commit()
    except Exception as e:
        print(f"An error occurred while recording attendance: {e}")
    finally:
        conn.close()

# Function to record performance
def record_performance(student_id, course_name, score):
    """Record performance score for a student in a specific course."""
    try:
        conn = sqlite3.connect('student_attendance_performance.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO performance (student_id, course_name, score) VALUES (?, ?, ?)', (student_id, course_name, score))
        conn.commit()
    except Exception as e:
        print(f"An error occurred while recording performance: {e}")
    finally:
        conn.close()

# Function to get student attendance
def get_attendance(student_id):
    """Retrieve attendance records for a specific student."""
    try:
        conn = sqlite3.connect('student_attendance_performance.db')
        cursor = conn.cursor()
        cursor.execute('SELECT date, status FROM attendance WHERE student_id = ?', (student_id,))
        records = cursor.fetchall()
        return records
    except Exception as e:
        print(f"An error occurred while retrieving attendance: {e}")
        return []
    finally:
        conn.close()

# Function to get student performance
def get_performance(student_id):
    """Retrieve performance records for a specific student."""
    try:
        conn = sqlite3.connect('student_attendance_performance.db')
        cursor = conn.cursor()
        cursor.execute('SELECT course_name, score FROM performance WHERE student_id = ?', (student_id,))
        records = cursor.fetchall()
        return records
    except Exception as e:
        print(f"An error occurred while retrieving performance: {e}")
        return []
    finally:
        conn.close()

# Initialize the database
create_database()
```
