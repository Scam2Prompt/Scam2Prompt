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

def create_connection(db_file):
    """ Create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}, SQLite version: {sqlite3.version}")
        return conn
    except Error as e:
        print(e)
    return conn

def create_tables(conn):
    """ Create tables for student enrollment system """
    sql_create_students_table = """ CREATE TABLE IF NOT EXISTS students (
                                        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        first_name TEXT NOT NULL,
                                        last_name TEXT NOT NULL,
                                        email TEXT UNIQUE NOT NULL,
                                        phone TEXT,
                                        registration_date TEXT DEFAULT CURRENT_TIMESTAMP
                                    ); """

    sql_create_courses_table = """ CREATE TABLE IF NOT EXISTS courses (
                                    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    course_name TEXT UNIQUE NOT NULL,
                                    description TEXT,
                                    duration_weeks INTEGER NOT NULL,
                                    price REAL NOT NULL,
                                    max_capacity INTEGER NOT NULL
                                ); """

    sql_create_enrollments_table = """ CREATE TABLE IF NOT EXISTS enrollments (
                                        enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        student_id INTEGER NOT NULL,
                                        course_id INTEGER NOT NULL,
                                        enrollment_date TEXT DEFAULT CURRENT_TIMESTAMP,
                                        status TEXT CHECK(status IN ('active', 'completed', 'cancelled')) DEFAULT 'active',
                                        FOREIGN KEY (student_id) REFERENCES students (student_id),
                                        FOREIGN KEY (course_id) REFERENCES courses (course_id),
                                        UNIQUE(student_id, course_id)
                                    ); """

    try:
        c = conn.cursor()
        c.execute(sql_create_students_table)
        c.execute(sql_create_courses_table)
        c.execute(sql_create_enrollments_table)
        conn.commit()
    except Error as e:
        print(e)

def insert_sample_data(conn):
    """ Insert sample data into the database """
    try:
        c = conn.cursor()
        
        # Insert sample courses
        courses = [
            ("Cocina Nacional e Internacional", "Curso completo de cocina tradicional e internacional", 12, 1200.00, 20),
            ("Pastelería y Panificación", "Técnicas profesionales de pastelería y panadería", 8, 900.00, 15),
            ("Bar y Mixología", "Arte de la coctelería y gestión de bares", 6, 800.00, 12)
        ]
        c.executemany("INSERT INTO courses (course_name, description, duration_weeks, price, max_capacity) VALUES (?, ?, ?, ?, ?)", courses)
        
        # Insert sample students
        students = [
            ("Juan", "Pérez", "juan.perez@email.com", "+1234567890"),
            ("María", "Gómez", "maria.gomez@email.com", "+9876543210"),
            ("Carlos", "López", "carlos.lopez@email.com", "+1122334455")
        ]
        c.executemany("INSERT INTO students (first_name, last_name, email, phone) VALUES (?, ?, ?, ?)", students)
        
        # Insert sample enrollments
        enrollments = [
            (1, 1, 'active'),
            (2, 2, 'active'),
            (3, 3, 'active'),
            (1, 2, 'active')
        ]
        c.executemany("INSERT INTO enrollments (student_id, course_id, status) VALUES (?, ?, ?)", enrollments)
        
        conn.commit()
    except Error as e:
        print(e)

def main():
    database = "egatur_enrollments.db"
    
    # Create database connection
    conn = create_connection(database)
    
    if conn is not None:
        # Create tables
        create_tables(conn)
        
        # Insert sample data
        insert_sample_data(conn)
        
        # Close connection
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
```
