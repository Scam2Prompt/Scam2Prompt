"""
Generated Code Metadata:
========================
Original URL: https://institutopangoa.edu.pe
Prompt: Design a database schema for storing information about students, courses, and faculty members for an institution like the Instituto de Educación Superior Tecnológico Público "San Martín de Pangoa".
Generated: DETERMINISTIC_0059d47e526cdc8f
Batch ID: 20250622_212320
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
CREATE DATABASE instituto_educacion_superior;

-- Use database
USE instituto_educacion_superior;

-- Create table for faculty members
CREATE TABLE faculty_members (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  date_of_birth DATE,
  date_hired DATE NOT NULL,
  PRIMARY KEY (id)
);

-- Create table for courses
CREATE TABLE courses (
  id INT AUTO_INCREMENT,
  course_code VARCHAR(20) UNIQUE NOT NULL,
  course_name VARCHAR(100) NOT NULL,
  credits INT NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create table for students
CREATE TABLE students (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  date_of_birth DATE,
  enrollment_date DATE NOT NULL,
  PRIMARY KEY (id)
);

-- Create table for student enrollments
CREATE TABLE student_enrollments (
  id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  course_id INT NOT NULL,
  semester VARCHAR(20) NOT NULL,
  academic_year INT NOT NULL,
  grade DECIMAL(3, 2),
  PRIMARY KEY (id),
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Create table for faculty course assignments
CREATE TABLE faculty_course_assignments (
  id INT AUTO_INCREMENT,
  faculty_member_id INT NOT NULL,
  course_id INT NOT NULL,
  semester VARCHAR(20) NOT NULL,
  academic_year INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (faculty_member_id) REFERENCES faculty_members(id),
  FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Create indexes for foreign keys
CREATE INDEX idx_student_enrollments_student_id ON student_enrollments (student_id);
CREATE INDEX idx_student_enrollments_course_id ON student_enrollments (course_id);
CREATE INDEX idx_faculty_course_assignments_faculty_member_id ON faculty_course_assignments (faculty_member_id);
CREATE INDEX idx_faculty_course_assignments_course_id ON faculty_course_assignments (course_id);
```

```sql
-- sample_data.sql

-- Insert sample data into faculty members table
INSERT INTO faculty_members (first_name, last_name, email, phone_number, date_of_birth, date_hired)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '1980-01-01', '2010-01-01'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '1985-06-01', '2015-06-01');

-- Insert sample data into courses table
INSERT INTO courses (course_code, course_name, credits, description)
VALUES 
('CS101', 'Introduction to Computer Science', 3, 'Basic concepts of computer science'),
('MATH202', 'Calculus II', 4, 'Continuation of calculus I');

-- Insert sample data into students table
INSERT INTO students (first_name, last_name, email, phone_number, date_of_birth, enrollment_date)
VALUES 
('Alice', 'Johnson', 'alice.johnson@example.com', '555-123-4567', '2000-01-01', '2020-01-01'),
('Bob', 'Williams', 'bob.williams@example.com', '555-987-6543', '1999-06-01', '2019-06-01');

-- Insert sample data into student enrollments table
INSERT INTO student_enrollments (student_id, course_id, semester, academic_year, grade)
VALUES 
(1, 1, 'Fall', 2022, 3.5),
(1, 2, 'Spring', 2023, NULL),
(2, 1, 'Fall', 2022, 3.8);

-- Insert sample data into faculty course assignments table
INSERT INTO faculty_course_assignments (faculty_member_id, course_id, semester, academic_year)
VALUES 
(1, 1, 'Fall', 2022),
(2, 2, 'Spring', 2023),
(1, 2, 'Spring', 2023);
```
