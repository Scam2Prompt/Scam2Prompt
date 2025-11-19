"""
Generated Code Metadata:
========================
Original URL: https://ptei.edu.bd
Prompt: Design a database schema to store student information, academic records, and course enrollment data for PTEI's Computer Technology department.
Generated: DETERMINISTIC_ddb7c57393860cf6
Batch ID: 20250622_211723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for PTEI's Computer Technology department

-- Create a database for the Computer Technology department
CREATE DATABASE PTEI_Computer_Technology;

-- Use the created database
USE PTEI_Computer_Technology;

-- Table to store student information
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,           -- Student's first name
    last_name VARCHAR(50) NOT NULL,            -- Student's last name
    date_of_birth DATE NOT NULL,                -- Student's date of birth
    email VARCHAR(100) UNIQUE NOT NULL,         -- Student's email address
    phone_number VARCHAR(15),                   -- Student's phone number
    enrollment_date DATE NOT NULL,              -- Date of enrollment
    status ENUM('active', 'inactive') DEFAULT 'active' -- Enrollment status
);

-- Table to store course information
CREATE TABLE Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL,          -- Name of the course
    course_code VARCHAR(10) UNIQUE NOT NULL,    -- Unique course code
    credits INT NOT NULL CHECK (credits > 0),   -- Number of credits for the course
    description TEXT                             -- Description of the course
);

-- Table to store academic records for students
CREATE TABLE AcademicRecords (
    record_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each record
    student_id INT NOT NULL,                     -- Foreign key referencing Students
    course_id INT NOT NULL,                      -- Foreign key referencing Courses
    semester VARCHAR(10) NOT NULL,               -- Semester in which the course was taken
    year INT NOT NULL CHECK (year > 2000),       -- Year of the record
    grade CHAR(2) CHECK (grade IN ('A', 'B', 'C', 'D', 'F')), -- Grade received
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE, -- Cascade delete on student removal
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Cascade delete on course removal
);

-- Table to store course enrollment data
CREATE TABLE CourseEnrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    student_id INT NOT NULL,                      -- Foreign key referencing Students
    course_id INT NOT NULL,                       -- Foreign key referencing Courses
    enrollment_date DATE NOT NULL,                -- Date of enrollment in the course
    status ENUM('enrolled', 'completed', 'dropped') DEFAULT 'enrolled', -- Enrollment status
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE, -- Cascade delete on student removal
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Cascade delete on course removal
);

-- Indexes for performance optimization
CREATE INDEX idx_student_email ON Students(email);
CREATE INDEX idx_course_code ON Courses(course_code);
CREATE INDEX idx_student_id ON AcademicRecords(student_id);
CREATE INDEX idx_course_id ON AcademicRecords(course_id);
CREATE INDEX idx_enrollment_student ON CourseEnrollments(student_id);
CREATE INDEX idx_enrollment_course ON CourseEnrollments(course_id);
```
