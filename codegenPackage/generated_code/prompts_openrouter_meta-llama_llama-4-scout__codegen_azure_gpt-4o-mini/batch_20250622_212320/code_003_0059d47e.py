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
-- Database schema for Instituto de Educación Superior Tecnológico Público "San Martín de Pangoa"

-- Create a table for storing student information
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL, -- Student's first name
    last_name VARCHAR(50) NOT NULL, -- Student's last name
    date_of_birth DATE NOT NULL, -- Student's date of birth
    email VARCHAR(100) UNIQUE NOT NULL, -- Student's email address
    enrollment_date DATE NOT NULL, -- Date of enrollment
    program_id INT NOT NULL, -- Foreign key to the Programs table
    FOREIGN KEY (program_id) REFERENCES Programs(program_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing course information
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY, -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL, -- Name of the course
    course_code VARCHAR(10) UNIQUE NOT NULL, -- Unique code for the course
    credits INT NOT NULL CHECK (credits > 0), -- Number of credits for the course
    faculty_id INT NOT NULL, -- Foreign key to the Faculty table
    FOREIGN KEY (faculty_id) REFERENCES Faculty(faculty_id) ON DELETE SET NULL -- Ensures referential integrity
);

-- Create a table for storing faculty member information
CREATE TABLE Faculty (
    faculty_id SERIAL PRIMARY KEY, -- Unique identifier for each faculty member
    first_name VARCHAR(50) NOT NULL, -- Faculty member's first name
    last_name VARCHAR(50) NOT NULL, -- Faculty member's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Faculty member's email address
    hire_date DATE NOT NULL, -- Date of hiring
    department VARCHAR(100) NOT NULL -- Department of the faculty member
);

-- Create a table for storing program information
CREATE TABLE Programs (
    program_id SERIAL PRIMARY KEY, -- Unique identifier for each program
    program_name VARCHAR(100) NOT NULL, -- Name of the program
    duration INT NOT NULL CHECK (duration > 0) -- Duration of the program in years
);

-- Create a table for storing enrollment information (many-to-many relationship)
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY, -- Unique identifier for each enrollment
    student_id INT NOT NULL, -- Foreign key to the Students table
    course_id INT NOT NULL, -- Foreign key to the Courses table
    enrollment_date DATE NOT NULL, -- Date of enrollment in the course
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_students_email ON Students(email);
CREATE INDEX idx_courses_code ON Courses(course_code);
CREATE INDEX idx_faculty_email ON Faculty(email);
CREATE INDEX idx_programs_name ON Programs(program_name);
```
