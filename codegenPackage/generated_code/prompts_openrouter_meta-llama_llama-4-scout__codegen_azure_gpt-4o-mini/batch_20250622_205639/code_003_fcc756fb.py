"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Design a database schema to store information about students, courses (IELTS, PTE, Spoken English), and study abroad programs (e.g., USA, UK, Canada, Australia, Singapore) for a platform like Red & White International.
Generated: DETERMINISTIC_fcc756fb65f9a569
Batch ID: 20250622_205639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Red & White International platform

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS StudyAbroadPrograms;
DROP TABLE IF EXISTS Enrollments;

-- Table to store student information
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL, -- Student's first name
    last_name VARCHAR(50) NOT NULL, -- Student's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Student's email address
    phone_number VARCHAR(15), -- Student's phone number
    date_of_birth DATE, -- Student's date of birth
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store course information
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY, -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL, -- Name of the course (IELTS, PTE, Spoken English)
    duration INT NOT NULL, -- Duration of the course in weeks
    fee DECIMAL(10, 2) NOT NULL, -- Course fee
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store study abroad program information
CREATE TABLE StudyAbroadPrograms (
    program_id SERIAL PRIMARY KEY, -- Unique identifier for each program
    country VARCHAR(50) NOT NULL, -- Country of the study abroad program (USA, UK, etc.)
    program_name VARCHAR(100) NOT NULL, -- Name of the program
    duration INT NOT NULL, -- Duration of the program in months
    fee DECIMAL(10, 2) NOT NULL, -- Program fee
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store enrollments of students in courses
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY, -- Unique identifier for each enrollment
    student_id INT NOT NULL, -- Foreign key referencing Students
    course_id INT NOT NULL, -- Foreign key referencing Courses
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of enrollment
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE, -- Cascade delete on student removal
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Cascade delete on course removal
);

-- Indexes for faster querying
CREATE INDEX idx_student_email ON Students(email);
CREATE INDEX idx_course_name ON Courses(course_name);
CREATE INDEX idx_program_country ON StudyAbroadPrograms(country);
```
