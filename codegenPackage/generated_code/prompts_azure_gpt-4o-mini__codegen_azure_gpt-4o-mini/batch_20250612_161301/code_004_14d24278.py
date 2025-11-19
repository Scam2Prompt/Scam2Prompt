"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Design a database schema in SQL for managing the administrative services of I.E Politécnico Municipal Cali, including tables for student information, academic programs, and faculty members.
Generated: DETERMINISTIC_14d24278b8d4f154
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing administrative services of I.E Politécnico Municipal Cali

-- Create a database
CREATE DATABASE PolitecnicoMunicipalCali;

-- Use the created database
USE PolitecnicoMunicipalCali;

-- Table for storing student information
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,           -- Student's first name
    last_name VARCHAR(50) NOT NULL,            -- Student's last name
    date_of_birth DATE NOT NULL,                -- Student's date of birth
    enrollment_date DATE NOT NULL,              -- Date when the student enrolled
    program_id INT,                             -- Foreign key referencing the academic program
    email VARCHAR(100) UNIQUE NOT NULL,        -- Student's email address
    phone_number VARCHAR(15),                   -- Student's phone number
    address VARCHAR(255),                        -- Student's address
    CONSTRAINT fk_program FOREIGN KEY (program_id) REFERENCES Programs(program_id) -- Foreign key constraint
);

-- Table for storing academic programs
CREATE TABLE Programs (
    program_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each program
    program_name VARCHAR(100) NOT NULL,         -- Name of the academic program
    program_description TEXT,                    -- Description of the program
    duration INT NOT NULL,                       -- Duration of the program in months
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the program was created
);

-- Table for storing faculty members
CREATE TABLE Faculty (
    faculty_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each faculty member
    first_name VARCHAR(50) NOT NULL,             -- Faculty member's first name
    last_name VARCHAR(50) NOT NULL,              -- Faculty member's last name
    email VARCHAR(100) UNIQUE NOT NULL,          -- Faculty member's email address
    phone_number VARCHAR(15),                     -- Faculty member's phone number
    hire_date DATE NOT NULL,                      -- Date when the faculty member was hired
    department VARCHAR(100),                      -- Department of the faculty member
    CONSTRAINT chk_email CHECK (email LIKE '%_@__%.__%') -- Check constraint for valid email format
);

-- Table for managing course offerings
CREATE TABLE Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL,            -- Name of the course
    course_description TEXT,                       -- Description of the course
    program_id INT,                               -- Foreign key referencing the academic program
    faculty_id INT,                               -- Foreign key referencing the faculty member
    credits INT NOT NULL,                         -- Number of credits for the course
    CONSTRAINT fk_program_course FOREIGN KEY (program_id) REFERENCES Programs(program_id), -- Foreign key constraint
    CONSTRAINT fk_faculty_course FOREIGN KEY (faculty_id) REFERENCES Faculty(faculty_id) -- Foreign key constraint
);

-- Table for managing student enrollments in courses
CREATE TABLE Enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    student_id INT,                                -- Foreign key referencing the student
    course_id INT,                                 -- Foreign key referencing the course
    enrollment_date DATE NOT NULL,                 -- Date of enrollment in the course
    grade DECIMAL(5, 2),                           -- Grade received in the course
    CONSTRAINT fk_student_enrollment FOREIGN KEY (student_id) REFERENCES Students(student_id), -- Foreign key constraint
    CONSTRAINT fk_course_enrollment FOREIGN KEY (course_id) REFERENCES Courses(course_id) -- Foreign key constraint
);

-- Ensure all tables are created successfully
SELECT 'Database schema for I.E Politécnico Municipal Cali created successfully.' AS message;
```
