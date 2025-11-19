"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghmc.edu.au
Prompt: Create a sample database schema in SQL for storing information about the Advanced Diploma of Civil Construction Design offered by Global Healthcare Management College.
Generated: DETERMINISTIC_f95da7ad29dfdac4
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL schema for storing information about the Advanced Diploma of Civil Construction Design
-- offered by Global Healthcare Management College

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Enrollments;
DROP TABLE IF EXISTS Instructors;

-- Table to store student information
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY,         -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,      -- Student's first name
    last_name VARCHAR(50) NOT NULL,       -- Student's last name
    email VARCHAR(100) UNIQUE NOT NULL,   -- Student's email (must be unique)
    phone VARCHAR(15),                     -- Student's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Last update timestamp
);

-- Table to store course information
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,          -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL,    -- Name of the course
    course_description TEXT,               -- Description of the course
    credits INT NOT NULL CHECK (credits > 0),  -- Number of credits for the course
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Last update timestamp
);

-- Table to store instructor information
CREATE TABLE Instructors (
    instructor_id SERIAL PRIMARY KEY,      -- Unique identifier for each instructor
    first_name VARCHAR(50) NOT NULL,      -- Instructor's first name
    last_name VARCHAR(50) NOT NULL,       -- Instructor's last name
    email VARCHAR(100) UNIQUE NOT NULL,   -- Instructor's email (must be unique)
    phone VARCHAR(15),                     -- Instructor's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Last update timestamp
);

-- Table to store enrollment information (relationship between students and courses)
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY,      -- Unique identifier for each enrollment
    student_id INT NOT NULL,               -- ID of the enrolled student
    course_id INT NOT NULL,                -- ID of the enrolled course
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date of enrollment
    grade DECIMAL(3, 2),                   -- Grade received in the course
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,  -- Foreign key constraint
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE  -- Foreign key constraint
);

-- Sample data insertion can be performed after this schema is created
-- Ensure proper error handling during data manipulation in application code
```
