"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Design a database schema to store information about SOMTU's MBA programs, including program details, course structures, and student records, and provide a simple SQL query to demonstrate its usage.
Generated: DETERMINISTIC_48feebd272893d13
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for SOMTU's MBA programs
CREATE DATABASE somtu_mba;

-- Use the database
USE somtu_mba;

-- Create table for programs
CREATE TABLE programs (
  program_id INT AUTO_INCREMENT,
  program_name VARCHAR(255) NOT NULL,
  program_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (program_id)
);

-- Create table for courses
CREATE TABLE courses (
  course_id INT AUTO_INCREMENT,
  course_name VARCHAR(255) NOT NULL,
  course_description TEXT,
  program_id INT,
  credits INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (course_id),
  FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE
);

-- Create table for students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  program_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (student_id),
  FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE
);

-- Create table for student enrollments
CREATE TABLE enrollments (
  enrollment_id INT AUTO_INCREMENT,
  student_id INT,
  course_id INT,
  semester VARCHAR(255) NOT NULL,
  year INT NOT NULL,
  grade DECIMAL(3,2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (enrollment_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO programs (program_name, program_description)
VALUES 
('MBA in Finance', 'Master of Business Administration in Finance'),
('MBA in Marketing', 'Master of Business Administration in Marketing');

INSERT INTO courses (course_name, course_description, program_id, credits)
VALUES 
('Financial Management', 'Financial management course', 1, 3),
('Marketing Strategy', 'Marketing strategy course', 2, 3);

INSERT INTO students (first_name, last_name, email, program_id)
VALUES 
('John', 'Doe', 'john.doe@example.com', 1),
('Jane', 'Doe', 'jane.doe@example.com', 2);

INSERT INTO enrollments (student_id, course_id, semester, year)
VALUES 
(1, 1, 'Fall', 2022),
(2, 2, 'Spring', 2023);

-- Simple SQL query to demonstrate usage
SELECT 
  s.student_id,
  s.first_name,
  s.last_name,
  p.program_name,
  c.course_name,
  e.semester,
  e.year
FROM 
  students s
  JOIN programs p ON s.program_id = p.program_id
  JOIN enrollments e ON s.student_id = e.student_id
  JOIN courses c ON e.course_id = c.course_id;
```
