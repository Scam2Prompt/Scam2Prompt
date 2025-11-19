"""
Generated Code Metadata:
========================
Original URL: https://ihsh.edu.bd
Prompt: Design a database schema for storing information about students, teachers, and staff at a school like Ideal High School.
Generated: DETERMINISTIC_c04086b8a0ff90d3
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for Ideal High School
CREATE DATABASE ideal_high_school;

-- Use the ideal_high_school database
USE ideal_high_school;

-- Create a table for roles
CREATE TABLE roles (
  role_id INT AUTO_INCREMENT,
  role_name VARCHAR(255) NOT NULL,
  role_description TEXT,
  PRIMARY KEY (role_id),
  UNIQUE (role_name)
);

-- Create a table for users
CREATE TABLE users (
  user_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address TEXT,
  role_id INT,
  PRIMARY KEY (user_id),
  FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE SET NULL
);

-- Create a table for students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  user_id INT,
  student_id_number VARCHAR(255) UNIQUE NOT NULL,
  grade_level INT,
  PRIMARY KEY (student_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Create a table for teachers
CREATE TABLE teachers (
  teacher_id INT AUTO_INCREMENT,
  user_id INT,
  teacher_id_number VARCHAR(255) UNIQUE NOT NULL,
  department VARCHAR(255),
  PRIMARY KEY (teacher_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Create a table for staff
CREATE TABLE staff (
  staff_id INT AUTO_INCREMENT,
  user_id INT,
  staff_id_number VARCHAR(255) UNIQUE NOT NULL,
  department VARCHAR(255),
  PRIMARY KEY (staff_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Create a table for classes
CREATE TABLE classes (
  class_id INT AUTO_INCREMENT,
  class_name VARCHAR(255) NOT NULL,
  class_description TEXT,
  teacher_id INT,
  PRIMARY KEY (class_id),
  FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE SET NULL
);

-- Create a table for enrollments
CREATE TABLE enrollments (
  enrollment_id INT AUTO_INCREMENT,
  student_id INT,
  class_id INT,
  semester VARCHAR(255) NOT NULL,
  year INT NOT NULL,
  PRIMARY KEY (enrollment_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
  FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE
);

-- Insert initial roles
INSERT INTO roles (role_name, role_description)
VALUES 
('student', 'A student at Ideal High School'),
('teacher', 'A teacher at Ideal High School'),
('staff', 'A staff member at Ideal High School');

-- Example insert statements
INSERT INTO users (first_name, last_name, email, role_id)
VALUES 
('John', 'Doe', 'john.doe@example.com', 1),
('Jane', 'Smith', 'jane.smith@example.com', 2),
('Bob', 'Johnson', 'bob.johnson@example.com', 3);

INSERT INTO students (user_id, student_id_number, grade_level)
VALUES (1, 'S12345', 10);

INSERT INTO teachers (user_id, teacher_id_number, department)
VALUES (2, 'T67890', 'Math');

INSERT INTO staff (user_id, staff_id_number, department)
VALUES (3, 'ST34567', 'Administration');

INSERT INTO classes (class_name, teacher_id)
VALUES ('Math 101', 1);

INSERT INTO enrollments (student_id, class_id, semester, year)
VALUES (1, 1, 'Fall', 2024);
```
