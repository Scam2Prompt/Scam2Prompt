"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: "Design a simple database schema to store information about students, instructors, and courses for a school offering programs in hospitality management and culinary arts."
Generated: DETERMINISTIC_0ae0402b92416027
Batch ID: 20250622_212015
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
CREATE DATABASE school;

-- Use database
USE school;

-- Create table for programs
CREATE TABLE programs (
  program_id INT AUTO_INCREMENT,
  program_name VARCHAR(255) NOT NULL,
  program_description TEXT,
  PRIMARY KEY (program_id)
);

-- Create table for courses
CREATE TABLE courses (
  course_id INT AUTO_INCREMENT,
  course_name VARCHAR(255) NOT NULL,
  course_description TEXT,
  program_id INT,
  PRIMARY KEY (course_id),
  FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE SET NULL
);

-- Create table for instructors
CREATE TABLE instructors (
  instructor_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  PRIMARY KEY (instructor_id)
);

-- Create table for students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  PRIMARY KEY (student_id)
);

-- Create table for course enrollments
CREATE TABLE course_enrollments (
  enrollment_id INT AUTO_INCREMENT,
  student_id INT,
  course_id INT,
  enrollment_date DATE NOT NULL,
  PRIMARY KEY (enrollment_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Create table for instructor course assignments
CREATE TABLE instructor_courses (
  assignment_id INT AUTO_INCREMENT,
  instructor_id INT,
  course_id INT,
  assignment_date DATE NOT NULL,
  PRIMARY KEY (assignment_id),
  FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO programs (program_name, program_description)
VALUES 
('Hospitality Management', 'Program for hospitality management'),
('Culinary Arts', 'Program for culinary arts');

INSERT INTO courses (course_name, course_description, program_id)
VALUES 
('Introduction to Hospitality', 'Introduction to hospitality management', 1),
('Culinary Techniques', 'Basic culinary techniques', 2),
('Hotel Management', 'Hotel management and operations', 1),
('Pastry Arts', 'Pastry arts and desserts', 2);

INSERT INTO instructors (first_name, last_name, email)
VALUES 
('John', 'Doe', 'john.doe@example.com'),
('Jane', 'Smith', 'jane.smith@example.com'),
('Bob', 'Johnson', 'bob.johnson@example.com');

INSERT INTO students (first_name, last_name, email)
VALUES 
('Alice', 'Williams', 'alice.williams@example.com'),
('Mike', 'Brown', 'mike.brown@example.com'),
('Emily', 'Davis', 'emily.davis@example.com');

INSERT INTO course_enrollments (student_id, course_id, enrollment_date)
VALUES 
(1, 1, '2022-01-01'),
(2, 2, '2022-01-01'),
(3, 3, '2022-01-01');

INSERT INTO instructor_courses (instructor_id, course_id, assignment_date)
VALUES 
(1, 1, '2022-01-01'),
(2, 2, '2022-01-01'),
(3, 3, '2022-01-01');
```
