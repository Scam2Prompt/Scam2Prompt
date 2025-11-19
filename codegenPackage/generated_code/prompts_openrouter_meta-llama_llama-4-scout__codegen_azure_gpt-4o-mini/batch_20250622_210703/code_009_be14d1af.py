"""
Generated Code Metadata:
========================
Original URL: https://www.ahs.edu.np
Prompt: Design a database schema to store information about students, faculty, and courses at Ace Higher Secondary School.
Generated: DETERMINISTIC_be14d1af75245a6b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Ace Higher Secondary School

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS Enrollment;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Faculty;
DROP TABLE IF EXISTS Students;

-- Table to store student information
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL, -- Student's first name
    last_name VARCHAR(50) NOT NULL, -- Student's last name
    date_of_birth DATE NOT NULL, -- Student's date of birth
    email VARCHAR(100) UNIQUE NOT NULL, -- Student's email address
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE -- Date of enrollment
);

-- Table to store faculty information
CREATE TABLE Faculty (
    faculty_id SERIAL PRIMARY KEY, -- Unique identifier for each faculty member
    first_name VARCHAR(50) NOT NULL, -- Faculty member's first name
    last_name VARCHAR(50) NOT NULL, -- Faculty member's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Faculty member's email address
    hire_date DATE NOT NULL DEFAULT CURRENT_DATE -- Date of hiring
);

-- Table to store course information
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY, -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL, -- Name of the course
    course_code VARCHAR(10) UNIQUE NOT NULL, -- Unique course code
    credits INT NOT NULL CHECK (credits > 0), -- Number of credits for the course
    faculty_id INT REFERENCES Faculty(faculty_id) ON DELETE SET NULL -- Faculty member teaching the course
);

-- Table to store enrollment information linking students and courses
CREATE TABLE Enrollment (
    enrollment_id SERIAL PRIMARY KEY, -- Unique identifier for each enrollment record
    student_id INT REFERENCES Students(student_id) ON DELETE CASCADE, -- Student enrolled in the course
    course_id INT REFERENCES Courses(course_id) ON DELETE CASCADE, -- Course the student is enrolled in
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE, -- Date of enrollment in the course
    UNIQUE (student_id, course_id) -- Ensure a student cannot enroll in the same course multiple times
);

-- Indexes for faster lookups
CREATE INDEX idx_students_email ON Students(email);
CREATE INDEX idx_faculty_email ON Faculty(email);
CREATE INDEX idx_courses_code ON Courses(course_code);
```
