"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: Create a database schema for managing student records, faculty information, and course schedules for an institution like Trentino.
Generated: DETERMINISTIC_58d583d79153bcdf
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for Trentino institution

-- Create database
CREATE DATABASE trentino_institution;

-- Use database
USE trentino_institution;

-- Create table for faculties
CREATE TABLE faculties (
    faculty_id INT AUTO_INCREMENT,
    faculty_name VARCHAR(255) NOT NULL,
    faculty_email VARCHAR(255) UNIQUE NOT NULL,
    faculty_phone VARCHAR(20),
    faculty_address VARCHAR(255),
    PRIMARY KEY (faculty_id)
);

-- Create table for departments
CREATE TABLE departments (
    department_id INT AUTO_INCREMENT,
    department_name VARCHAR(255) NOT NULL,
    faculty_id INT,
    PRIMARY KEY (department_id),
    FOREIGN KEY (faculty_id) REFERENCES faculties(faculty_id) ON DELETE SET NULL
);

-- Create table for courses
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT,
    course_name VARCHAR(255) NOT NULL,
    course_code VARCHAR(20) UNIQUE NOT NULL,
    department_id INT,
    course_description TEXT,
    PRIMARY KEY (course_id),
    FOREIGN KEY (department_id) REFERENCES departments(department_id) ON DELETE SET NULL
);

-- Create table for students
CREATE TABLE students (
    student_id INT AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    student_email VARCHAR(255) UNIQUE NOT NULL,
    student_phone VARCHAR(20),
    student_address VARCHAR(255),
    date_of_birth DATE,
    PRIMARY KEY (student_id)
);

-- Create table for student enrollments
CREATE TABLE student_enrollments (
    enrollment_id INT AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    semester VARCHAR(20) NOT NULL,
    academic_year VARCHAR(20) NOT NULL,
    PRIMARY KEY (enrollment_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Create table for faculty courses
CREATE TABLE faculty_courses (
    faculty_course_id INT AUTO_INCREMENT,
    faculty_id INT,
    course_id INT,
    semester VARCHAR(20) NOT NULL,
    academic_year VARCHAR(20) NOT NULL,
    PRIMARY KEY (faculty_course_id),
    FOREIGN KEY (faculty_id) REFERENCES faculties(faculty_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Create table for course schedules
CREATE TABLE course_schedules (
    schedule_id INT AUTO_INCREMENT,
    course_id INT,
    schedule_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    location VARCHAR(255) NOT NULL,
    PRIMARY KEY (schedule_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_student_email ON students (student_email);
CREATE INDEX idx_faculty_email ON faculties (faculty_email);
CREATE INDEX idx_course_code ON courses (course_code);
```

```python
# Python code to interact with the database

import mysql.connector
from mysql.connector import Error

class TrentinoDatabase:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to database successfully")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def create_tables(self):
        # SQL queries to create tables
        queries = [
            """
            CREATE TABLE IF NOT EXISTS faculties (
                faculty_id INT AUTO_INCREMENT,
                faculty_name VARCHAR(255) NOT NULL,
                faculty_email VARCHAR(255) UNIQUE NOT NULL,
                faculty_phone VARCHAR(20),
                faculty_address VARCHAR(255),
                PRIMARY KEY (faculty_id)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS departments (
                department_id INT AUTO_INCREMENT,
                department_name VARCHAR(255) NOT NULL,
                faculty_id INT,
                PRIMARY KEY (department_id),
                FOREIGN KEY (faculty_id) REFERENCES faculties(faculty_id) ON DELETE SET NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS courses (
                course_id INT AUTO_INCREMENT,
                course_name VARCHAR(255) NOT NULL,
                course_code VARCHAR(20) UNIQUE NOT NULL,
                department_id INT,
                course_description TEXT,
                PRIMARY KEY (course_id),
                FOREIGN KEY (department_id) REFERENCES departments(department_id) ON DELETE SET NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS students (
                student_id INT AUTO_INCREMENT,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                student_email VARCHAR(255) UNIQUE NOT NULL,
                student_phone VARCHAR(20),
                student_address VARCHAR(255),
                date_of_birth DATE,
                PRIMARY KEY (student_id)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS student_enrollments (
                enrollment_id INT AUTO_INCREMENT,
                student_id INT,
                course_id INT,
                semester VARCHAR(20) NOT NULL,
                academic_year VARCHAR(20) NOT NULL,
                PRIMARY KEY (enrollment_id),
                FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
                FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS faculty_courses (
                faculty_course_id INT AUTO_INCREMENT,
                faculty_id INT,
                course_id INT,
                semester VARCHAR(20) NOT NULL,
                academic_year VARCHAR(20) NOT NULL,
                PRIMARY KEY (faculty_course_id),
                FOREIGN KEY (faculty_id) REFERENCES faculties(faculty_id) ON DELETE CASCADE,
                FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS course_schedules (
                schedule_id INT AUTO_INCREMENT,
                course_id INT,
                schedule_date DATE NOT NULL,
                start_time TIME NOT NULL,
                end_time TIME NOT NULL,
                location VARCHAR(255) NOT NULL,
                PRIMARY KEY (schedule_id),
                FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
            );
            """
        ]

        cursor = self.connection.cursor()
        for query in queries:
            try:
                cursor.execute(query)
            except Error as e:
                print(f"Error creating table: {e}")
        cursor.close()

    def insert_faculty(self, faculty_name, faculty_email, faculty_phone, faculty_address):
        query = """
            INSERT INTO faculties (faculty_name, faculty_email, faculty_phone, faculty_address)
            VALUES (%s, %s, %s, %s);
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (faculty_name, faculty_email, faculty_phone, faculty_address))
            self.connection.commit()
        except Error as e:
            print(f"Error inserting faculty: {e}")
        cursor.close()

# Example usage
if __name__ == "__main__":
    db = TrentinoDatabase("localhost", "trentino_institution", "root", "password")
    db.connect()
    db.create_tables()
    db.insert_faculty("John Doe", "john.doe@example.com", "123-456-7890", "123 Main St")
```
