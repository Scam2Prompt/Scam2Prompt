"""
Generated Code Metadata:
========================
Original URL: https://siprosa.org
Prompt: Design a simple database schema to manage information about students, teachers, and classrooms for a school like Siprosa School, with a focus on low student-to-teacher ratio.
Generated: DETERMINISTIC_0efb95d680a98792
Batch ID: 20250622_211412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for school management
CREATE DATABASE siprosa_school;

-- Use the database
USE siprosa_school;

-- Create table for classrooms
CREATE TABLE classrooms (
  classroom_id INT AUTO_INCREMENT,
  classroom_name VARCHAR(255) NOT NULL,
  capacity INT NOT NULL,
  PRIMARY KEY (classroom_id)
);

-- Create table for teachers
CREATE TABLE teachers (
  teacher_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  date_of_birth DATE,
  hire_date DATE NOT NULL,
  PRIMARY KEY (teacher_id)
);

-- Create table for students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  date_of_birth DATE NOT NULL,
  admission_date DATE NOT NULL,
  classroom_id INT,
  PRIMARY KEY (student_id),
  FOREIGN KEY (classroom_id) REFERENCES classrooms(classroom_id) ON DELETE SET NULL
);

-- Create table for teacher_classroom assignments
CREATE TABLE teacher_classroom_assignments (
  assignment_id INT AUTO_INCREMENT,
  teacher_id INT NOT NULL,
  classroom_id INT NOT NULL,
  academic_year VARCHAR(255) NOT NULL,
  PRIMARY KEY (assignment_id),
  FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE CASCADE,
  FOREIGN KEY (classroom_id) REFERENCES classrooms(classroom_id) ON DELETE CASCADE,
  UNIQUE (teacher_id, classroom_id, academic_year)
);

-- Create table for student_teacher assignments (e.g., homeroom or advisory)
CREATE TABLE student_teacher_assignments (
  assignment_id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  teacher_id INT NOT NULL,
  academic_year VARCHAR(255) NOT NULL,
  PRIMARY KEY (assignment_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
  FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE CASCADE,
  UNIQUE (student_id, teacher_id, academic_year)
);
```

```python
# school_management.py

import mysql.connector
from mysql.connector import Error

class SchoolManagement:
  def __init__(self, host_name, db_name, user_name, user_password):
    self.host_name = host_name
    self.db_name = db_name
    self.user_name = user_name
    self.user_password = user_password
    self.connection = None

  def create_connection(self):
    try:
      self.connection = mysql.connector.connect(
        host=self.host_name,
        database=self.db_name,
        user=self.user_name,
        password=self.user_password
      )
      print("Connection to database established")
    except Error as e:
      print(f"Error: '{e}'")

  def execute_query(self, query):
    try:
      cursor = self.connection.cursor()
      cursor.execute(query)
      self.connection.commit()
      print("Query executed successfully")
    except Error as e:
      print(f"Error: '{e}'")

  def insert_classroom(self, classroom_name, capacity):
    query = f"INSERT INTO classrooms (classroom_name, capacity) VALUES ('{classroom_name}', {capacity})"
    self.execute_query(query)

  def insert_teacher(self, first_name, last_name, email, date_of_birth, hire_date):
    query = f"INSERT INTO teachers (first_name, last_name, email, date_of_birth, hire_date) VALUES ('{first_name}', '{last_name}', '{email}', '{date_of_birth}', '{hire_date}')"
    self.execute_query(query)

  def insert_student(self, first_name, last_name, email, date_of_birth, admission_date, classroom_id):
    query = f"INSERT INTO students (first_name, last_name, email, date_of_birth, admission_date, classroom_id) VALUES ('{first_name}', '{last_name}', '{email}', '{date_of_birth}', '{admission_date}', {classroom_id})"
    self.execute_query(query)

  def close_connection(self):
    if self.connection.is_connected():
      self.connection.close()
      print("Database connection closed")

if __name__ == "__main__":
  school_db = SchoolManagement('localhost', 'siprosa_school', 'your_username', 'your_password')
  school_db.create_connection()

  # Example usage:
  school_db.insert_classroom('Math Room', 30)
  school_db.insert_teacher('John', 'Doe', 'john.doe@example.com', '1990-01-01', '2020-01-01')
  school_db.insert_student('Jane', 'Doe', 'jane.doe@example.com', '2000-01-01', '2020-01-01', 1)

  school_db.close_connection()
```
