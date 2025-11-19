"""
Generated Code Metadata:
========================
Original URL: https://darulraza.net
Prompt: Design a database schema for storing information about Islamic courses, instructors, and students for the Darul Raza online academy.
Generated: DETERMINISTIC_313d63fc86238704
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Darul Raza Online Academy

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Instructor;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Enrollment;

-- Table to store information about courses
CREATE TABLE Course (
    course_id SERIAL PRIMARY KEY, -- Unique identifier for each course
    course_name VARCHAR(255) NOT NULL, -- Name of the course
    description TEXT, -- Description of the course
    duration INT NOT NULL, -- Duration of the course in hours
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of course creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about instructors
CREATE TABLE Instructor (
    instructor_id SERIAL PRIMARY KEY, -- Unique identifier for each instructor
    first_name VARCHAR(100) NOT NULL, -- Instructor's first name
    last_name VARCHAR(100) NOT NULL, -- Instructor's last name
    email VARCHAR(255) UNIQUE NOT NULL, -- Instructor's email (must be unique)
    bio TEXT, -- Short biography of the instructor
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of instructor creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about students
CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(100) NOT NULL, -- Student's first name
    last_name VARCHAR(100) NOT NULL, -- Student's last name
    email VARCHAR(255) UNIQUE NOT NULL, -- Student's email (must be unique)
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of registration
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store enrollment information linking students to courses
CREATE TABLE Enrollment (
    enrollment_id SERIAL PRIMARY KEY, -- Unique identifier for each enrollment
    student_id INT NOT NULL, -- Foreign key referencing Student
    course_id INT NOT NULL, -- Foreign key referencing Course
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of enrollment
    status VARCHAR(50) DEFAULT 'active', -- Status of enrollment (e.g., active, completed, dropped)
    FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (course_id) REFERENCES Course(course_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_course_name ON Course(course_name);
CREATE INDEX idx_instructor_email ON Instructor(email);
CREATE INDEX idx_student_email ON Student(email);
```
