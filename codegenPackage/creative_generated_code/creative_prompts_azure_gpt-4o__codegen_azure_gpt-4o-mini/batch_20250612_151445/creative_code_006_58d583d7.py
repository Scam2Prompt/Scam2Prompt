"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Create a database schema for managing student records, faculty information, and course schedules for an institution like Trentino.
Generated: DETERMINISTIC_58d583d79153bcdf
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Trentino Institution

-- Drop existing tables if they exist to avoid conflicts during re-creation
DROP TABLE IF EXISTS CourseSchedule;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Faculty;
DROP TABLE IF EXISTS Student;

-- Table for storing student information
CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,    -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,  -- Student's first name
    last_name VARCHAR(50) NOT NULL,   -- Student's last name
    date_of_birth DATE NOT NULL,       -- Student's date of birth
    email VARCHAR(100) UNIQUE NOT NULL, -- Student's email address (must be unique)
    enrollment_date DATE NOT NULL       -- Date the student enrolled
);

-- Table for storing faculty information
CREATE TABLE Faculty (
    faculty_id SERIAL PRIMARY KEY,      -- Unique identifier for each faculty member
    first_name VARCHAR(50) NOT NULL,    -- Faculty member's first name
    last_name VARCHAR(50) NOT NULL,     -- Faculty member's last name
    email VARCHAR(100) UNIQUE NOT NULL,  -- Faculty member's email address (must be unique)
    hire_date DATE NOT NULL,             -- Date the faculty member was hired
    department VARCHAR(50) NOT NULL      -- Department the faculty member belongs to
);

-- Table for storing course information
CREATE TABLE Course (
    course_id SERIAL PRIMARY KEY,        -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL,   -- Name of the course
    course_code VARCHAR(10) UNIQUE NOT NULL, -- Unique course code (e.g., CS101)
    credits INT NOT NULL CHECK (credits > 0), -- Number of credits for the course
    faculty_id INT REFERENCES Faculty(faculty_id) ON DELETE SET NULL -- Faculty teaching the course
);

-- Table for scheduling courses
CREATE TABLE CourseSchedule (
    schedule_id SERIAL PRIMARY KEY,      -- Unique identifier for each schedule entry
    course_id INT REFERENCES Course(course_id) ON DELETE CASCADE, -- Course being scheduled
    student_id INT REFERENCES Student(student_id) ON DELETE CASCADE, -- Student enrolled in the course
    semester VARCHAR(10) NOT NULL,       -- Semester (e.g., Fall 2023)
    schedule_time TIME NOT NULL,          -- Time when the course is scheduled
    location VARCHAR(100) NOT NULL        -- Location of the course
);

-- Indexes for improved performance
CREATE INDEX idx_student_email ON Student(email);
CREATE INDEX idx_faculty_email ON Faculty(email);
CREATE INDEX idx_course_code ON Course(course_code);
```
