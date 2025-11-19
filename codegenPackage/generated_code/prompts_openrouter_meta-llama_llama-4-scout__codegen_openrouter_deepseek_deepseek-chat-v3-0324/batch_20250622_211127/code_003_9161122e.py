"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: "Design a database schema for storing student records, faculty information, and course details for an educational institution with multiple centers like Potencia Academy."
Generated: DETERMINISTIC_9161122e4ebcbb71
Batch ID: 20250622_211127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database Schema for Educational Institution Management System

import sqlite3
from typing import Optional
from datetime import date

def initialize_database(db_name: str = 'education_management.db') -> sqlite3.Connection:
    """
    Initialize the SQLite database with required tables.
    Returns a connection to the database.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create tables with proper schema and constraints
    cursor.executescript("""
    PRAGMA foreign_keys = ON;

    -- Centers table for multiple institution locations
    CREATE TABLE IF NOT EXISTS centers (
        center_id INTEGER PRIMARY KEY AUTOINCREMENT,
        center_name TEXT NOT NULL UNIQUE,
        address TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        country TEXT NOT NULL DEFAULT 'USA',
        postal_code TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- Departments table for academic divisions
    CREATE TABLE IF NOT EXISTS departments (
        department_id INTEGER PRIMARY KEY AUTOINCREMENT,
        center_id INTEGER NOT NULL,
        department_name TEXT NOT NULL,
        head_of_department TEXT,
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (center_id) REFERENCES centers(center_id) ON DELETE CASCADE,
        UNIQUE(center_id, department_name)
    );

    -- Faculty members table
    CREATE TABLE IF NOT EXISTS faculty (
        faculty_id INTEGER PRIMARY KEY AUTOINCREMENT,
        department_id INTEGER NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone TEXT,
        address TEXT,
        hire_date DATE NOT NULL,
        position TEXT NOT NULL,
        salary REAL,
        is_active BOOLEAN DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (department_id) REFERENCES departments(department_id) ON DELETE CASCADE
    );

    -- Students table
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        center_id INTEGER NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone TEXT,
        address TEXT,
        date_of_birth DATE NOT NULL,
        enrollment_date DATE NOT NULL,
        graduation_date DATE,
        is_active BOOLEAN DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (center_id) REFERENCES centers(center_id) ON DELETE CASCADE
    );

    -- Courses table
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        department_id INTEGER NOT NULL,
        course_code TEXT NOT NULL,
        course_name TEXT NOT NULL,
        description TEXT,
        credit_hours INTEGER NOT NULL,
        is_active BOOLEAN DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (department_id) REFERENCES departments(department_id) ON DELETE CASCADE,
        UNIQUE(department_id, course_code)
    );

    -- Course offerings per semester/term
    CREATE TABLE IF NOT EXISTS course_offerings (
        offering_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_id INTEGER NOT NULL,
        faculty_id INTEGER NOT NULL,
        term TEXT NOT NULL,  -- e.g., 'Fall 2023', 'Spring 2024'
        schedule TEXT NOT NULL,  -- e.g., 'MWF 10:00-11:00'
        room_number TEXT NOT NULL,
        max_capacity INTEGER NOT NULL,
        current_enrollment INTEGER DEFAULT 0,
        is_active BOOLEAN DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
        FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id) ON DELETE CASCADE,
        UNIQUE(course_id, term, schedule)
    );

    -- Student enrollments in course offerings
    CREATE TABLE IF NOT EXISTS enrollments (
        enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        offering_id INTEGER NOT NULL,
        enrollment_date DATE NOT NULL,
        grade TEXT,  -- e.g., 'A', 'B+', etc.
        status TEXT DEFAULT 'active',  -- 'active', 'withdrawn', 'completed'
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
        FOREIGN KEY (offering_id) REFERENCES course_offerings(offering_id) ON DELETE CASCADE,
        UNIQUE(student_id, offering_id)
    );

    -- Attendance records
    CREATE TABLE IF NOT EXISTS attendance (
        attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
        enrollment_id INTEGER NOT NULL,
        date DATE NOT NULL,
        status TEXT NOT NULL,  -- 'present', 'absent', 'late', 'excused'
        notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
        UNIQUE(enrollment_id, date)
    );
    """)

    # Create indexes for performance
    cursor.executescript("""
    CREATE INDEX IF NOT EXISTS idx_students_center ON students(center_id);
    CREATE INDEX IF NOT EXISTS idx_faculty_department ON faculty(department_id);
    CREATE INDEX IF NOT EXISTS idx_courses_department ON courses(department_id);
    CREATE INDEX IF NOT EXISTS idx_offerings_course ON course_offerings(course_id);
    CREATE INDEX IF NOT EXISTS idx_offerings_faculty ON course_offerings(faculty_id);
    CREATE INDEX IF NOT EXISTS idx_enrollments_student ON enrollments(student_id);
    CREATE INDEX IF NOT EXISTS idx_enrollments_offering ON enrollments(offering_id);
    CREATE INDEX IF NOT EXISTS idx_attendance_enrollment ON attendance(enrollment_id);
    """)

    conn.commit()
    return conn

def add_sample_data(conn: sqlite3.Connection) -> None:
    """Add sample data for testing purposes"""
    try:
        cursor = conn.cursor()

        # Add sample centers
        cursor.executemany("""
        INSERT INTO centers (center_name, address, city, state, country, postal_code, phone, email)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, [
            ('Potencia Academy Main Campus', '123 Education St', 'San Francisco', 'CA', 'USA', '94105', '555-123-4567', 'main@potencia.edu'),
            ('Potencia Academy East Campus', '456 Learning Ave', 'Oakland', 'CA', 'USA', '94612', '555-234-5678', 'east@potencia.edu')
        ])

        # Add sample departments
        cursor.executemany("""
        INSERT INTO departments (center_id, department_name, head_of_department, description)
        VALUES (?, ?, ?, ?)
        """, [
            (1, 'Computer Science', 'Dr. Smith', 'Department of Computer Science and Engineering'),
            (1, 'Mathematics', 'Dr. Johnson', 'Department of Mathematics'),
            (2, 'Business Administration', 'Dr. Williams', 'Department of Business and Management')
        ])

        # Add sample faculty
        cursor.executemany("""
        INSERT INTO faculty (department_id, first_name, last_name, email, phone, hire_date, position, salary)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, [
            (1, 'John', 'Doe', 'john.doe@potencia.edu', '555-111-2222', '2020-01-15', 'Professor', 85000),
            (1, 'Jane', 'Smith', 'jane.smith@potencia.edu', '555-222-3333', '2019-05-20', 'Associate Professor', 75000),
            (2, 'Robert', 'Brown', 'robert.brown@potencia.edu', '555-333-4444', '2018-08-10', 'Professor', 90000)
        ])

        # Add sample students
        cursor.executemany("""
        INSERT INTO students (center_id, first_name, last_name, email, phone, date_of_birth, enrollment_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, [
            (1, 'Alice', 'Johnson', 'alice.johnson@student.potencia.edu', '555-444-5555', '2000-05-15', '2022-08-20'),
            (1, 'Bob', 'Williams', 'bob.williams@student.potencia.edu', '555-555-6666', '2001-02-28', '2022-08-20'),
            (2, 'Charlie', 'Davis', 'charlie.davis@student.potencia.edu', '555-666-7777', '1999-11-10', '
