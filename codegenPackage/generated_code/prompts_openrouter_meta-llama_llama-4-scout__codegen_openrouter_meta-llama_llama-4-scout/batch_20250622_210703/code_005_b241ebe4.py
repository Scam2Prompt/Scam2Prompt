"""
Generated Code Metadata:
========================
Original URL: https://enafo.cl
Prompt: "Design a database schema for storing information about ENAFO's courses, instructors, and students, and write a simple query to demonstrate its usage."
Generated: DETERMINISTIC_b241ebe40a3922f4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for ENAFO's courses, instructors, and students

-- Create database
CREATE DATABASE enafo;

-- Use database
USE enafo;

-- Create table for courses
CREATE TABLE courses (
  course_id INT AUTO_INCREMENT,
  course_name VARCHAR(255) NOT NULL,
  course_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (course_id)
);

-- Create table for instructors
CREATE TABLE instructors (
  instructor_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (instructor_id)
);

-- Create table for students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (student_id)
);

-- Create table for course instructors
CREATE TABLE course_instructors (
  course_id INT NOT NULL,
  instructor_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (course_id, instructor_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
  FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON DELETE CASCADE
);

-- Create table for course enrollments
CREATE TABLE course_enrollments (
  course_id INT NOT NULL,
  student_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (course_id, student_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO courses (course_name, course_description)
VALUES 
('Introduction to Python', 'Basic Python programming skills'),
('Data Structures and Algorithms', 'Data structures and algorithms in Python');

INSERT INTO instructors (first_name, last_name, email, phone_number)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210');

INSERT INTO students (first_name, last_name, email, phone_number)
VALUES 
('Alice', 'Johnson', 'alice.johnson@example.com', '555-123-4567'),
('Bob', 'Williams', 'bob.williams@example.com', '555-987-6543');

INSERT INTO course_instructors (course_id, instructor_id)
VALUES 
(1, 1),
(2, 2);

INSERT INTO course_enrollments (course_id, student_id)
VALUES 
(1, 1),
(1, 2),
(2, 1);

-- Simple query to demonstrate usage
SELECT 
  c.course_name, 
  i.first_name AS instructor_first_name, 
  i.last_name AS instructor_last_name, 
  s.first_name AS student_first_name, 
  s.last_name AS student_last_name
FROM 
  courses c
  JOIN course_instructors ci ON c.course_id = ci.course_id
  JOIN instructors i ON ci.instructor_id = i.instructor_id
  JOIN course_enrollments ce ON c.course_id = ce.course_id
  JOIN students s ON ce.student_id = s.student_id;
```
