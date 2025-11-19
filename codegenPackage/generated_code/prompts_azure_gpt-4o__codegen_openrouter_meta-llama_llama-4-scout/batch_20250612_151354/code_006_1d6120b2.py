"""
Generated Code Metadata:
========================
Original URL: https://enacip.edu.pe
Prompt: Write a SQL query to store and retrieve student enrollment data for courses like "Gestión Pública" and "Tributación," as described on the Enacip website.
Generated: DETERMINISTIC_1d6120b219645a6e
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing student enrollment data
CREATE DATABASE IF NOT EXISTS student_enrollments;

-- Use the created database
USE student_enrollments;

-- Create a table for courses
CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT,
    course_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (course_id)
);

-- Create a table for students
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT,
    student_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    PRIMARY KEY (student_id)
);

-- Create a table for enrollments
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INT AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    PRIMARY KEY (enrollment_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Insert courses
INSERT INTO courses (course_name)
VALUES 
('Gestión Pública'),
('Tributación');

-- Insert students
INSERT INTO students (student_name, email)
VALUES 
('John Doe', 'john@example.com'),
('Jane Doe', 'jane@example.com');

-- Insert enrollments
INSERT INTO enrollments (student_id, course_id, enrollment_date)
VALUES 
(1, 1, '2022-01-01'),
(1, 2, '2022-01-15'),
(2, 1, '2022-02-01');

-- Retrieve all enrollments
SELECT 
    s.student_name, 
    c.course_name, 
    e.enrollment_date
FROM 
    enrollments e
INNER JOIN 
    students s ON e.student_id = s.student_id
INNER JOIN 
    courses c ON e.course_id = c.course_id;

-- Retrieve enrollments for a specific course
SELECT 
    s.student_name, 
    c.course_name, 
    e.enrollment_date
FROM 
    enrollments e
INNER JOIN 
    students s ON e.student_id = s.student_id
INNER JOIN 
    courses c ON e.course_id = c.course_id
WHERE 
    c.course_name = 'Gestión Pública';

-- Retrieve enrollments for a specific student
SELECT 
    s.student_name, 
    c.course_name, 
    e.enrollment_date
FROM 
    enrollments e
INNER JOIN 
    students s ON e.student_id = s.student_id
INNER JOIN 
    courses c ON e.course_id = c.course_id
WHERE 
    s.student_name = 'John Doe';
```
