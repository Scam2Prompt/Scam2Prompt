"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: "Design a database schema for storing student records, faculty information, and course details for an educational institution with multiple centers like Potencia Academy."
Generated: DETERMINISTIC_9161122e4ebcbb71
Batch ID: 20250622_211127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Potencia Academy

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Faculty;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Enrollment;
DROP TABLE IF EXISTS Center;

-- Table to store information about educational centers
CREATE TABLE Center (
    center_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each center
    center_name VARCHAR(100) NOT NULL,         -- Name of the center
    location VARCHAR(255) NOT NULL              -- Location of the center
);

-- Table to store student records
CREATE TABLE Student (
    student_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,            -- Student's first name
    last_name VARCHAR(50) NOT NULL,             -- Student's last name
    email VARCHAR(100) UNIQUE NOT NULL,         -- Student's email (must be unique)
    date_of_birth DATE NOT NULL,                 -- Student's date of birth
    center_id INT,                               -- Foreign key referencing Center
    FOREIGN KEY (center_id) REFERENCES Center(center_id) ON DELETE SET NULL
);

-- Table to store faculty information
CREATE TABLE Faculty (
    faculty_id INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each faculty member
    first_name VARCHAR(50) NOT NULL,            -- Faculty member's first name
    last_name VARCHAR(50) NOT NULL,             -- Faculty member's last name
    email VARCHAR(100) UNIQUE NOT NULL,         -- Faculty member's email (must be unique)
    hire_date DATE NOT NULL,                     -- Date when the faculty member was hired
    center_id INT,                               -- Foreign key referencing Center
    FOREIGN KEY (center_id) REFERENCES Center(center_id) ON DELETE SET NULL
);

-- Table to store course details
CREATE TABLE Course (
    course_id INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL,           -- Name of the course
    course_description TEXT,                      -- Description of the course
    credits INT NOT NULL,                         -- Number of credits for the course
    center_id INT,                               -- Foreign key referencing Center
    FOREIGN KEY (center_id) REFERENCES Center(center_id) ON DELETE SET NULL
);

-- Table to store enrollment records linking students to courses
CREATE TABLE Enrollment (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each enrollment
    student_id INT,                               -- Foreign key referencing Student
    course_id INT,                                -- Foreign key referencing Course
    enrollment_date DATE NOT NULL,                -- Date of enrollment
    grade DECIMAL(3, 2),                         -- Grade received in the course
    FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES Course(course_id) ON DELETE CASCADE,
    UNIQUE (student_id, course_id)               -- Ensure a student can enroll in a course only once
);

-- Indexes for performance optimization
CREATE INDEX idx_student_email ON Student(email);
CREATE INDEX idx_faculty_email ON Faculty(email);
CREATE INDEX idx_course_name ON Course(course_name);
```
