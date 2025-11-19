"""
Generated Code Metadata:
========================
Original URL: https://workshopgranada.com
Prompt: "Design a database schema for storing information about sewing classes, instructors, and students, including features for tracking attendance, assignments, and progress."
Generated: DETERMINISTIC_02c2eb23a1a58589
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE sewing_school;

-- Use database
USE sewing_school;

-- Create table for instructors
CREATE TABLE instructors (
  instructor_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  bio TEXT,
  PRIMARY KEY (instructor_id)
);

-- Create table for students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  PRIMARY KEY (student_id)
);

-- Create table for classes
CREATE TABLE classes (
  class_id INT AUTO_INCREMENT,
  class_name VARCHAR(255) NOT NULL,
  class_description TEXT,
  instructor_id INT,
  start_date DATE,
  end_date DATE,
  PRIMARY KEY (class_id),
  FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
);

-- Create table for student enrollments
CREATE TABLE enrollments (
  enrollment_id INT AUTO_INCREMENT,
  student_id INT,
  class_id INT,
  enrollment_date DATE NOT NULL,
  PRIMARY KEY (enrollment_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (class_id) REFERENCES classes(class_id)
);

-- Create table for attendance
CREATE TABLE attendance (
  attendance_id INT AUTO_INCREMENT,
  enrollment_id INT,
  class_date DATE NOT NULL,
  attended BOOLEAN NOT NULL DEFAULT FALSE,
  PRIMARY KEY (attendance_id),
  FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id)
);

-- Create table for assignments
CREATE TABLE assignments (
  assignment_id INT AUTO_INCREMENT,
  class_id INT,
  assignment_name VARCHAR(255) NOT NULL,
  due_date DATE NOT NULL,
  PRIMARY KEY (assignment_id),
  FOREIGN KEY (class_id) REFERENCES classes(class_id)
);

-- Create table for student assignments
CREATE TABLE student_assignments (
  student_assignment_id INT AUTO_INCREMENT,
  enrollment_id INT,
  assignment_id INT,
  submission_date DATE,
  grade DECIMAL(3, 2),
  PRIMARY KEY (student_assignment_id),
  FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id),
  FOREIGN KEY (assignment_id) REFERENCES assignments(assignment_id)
);

-- Create table for progress tracking
CREATE TABLE progress (
  progress_id INT AUTO_INCREMENT,
  enrollment_id INT,
  progress_date DATE NOT NULL,
  notes TEXT,
  PRIMARY KEY (progress_id),
  FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id)
);
```

```python
# database.py
import mysql.connector
from mysql.connector import Error

class Database:
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
            print("Connected to database")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"Error executing query: {e}")

    def execute_read_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error executing query: {e}")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

# Example usage
if __name__ == "__main__":
    db = Database("localhost", "sewing_school", "root", "password")
    db.connect()

    # Create schema
    with open("schema.sql", "r") as f:
        queries = f.read().split(";")
        for query in queries:
            if query.strip():
                db.execute_query(query)

    db.close_connection()
```
