"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Design a database schema in SQL for managing student records and course enrollments at a music school, including tables for instruments, faculty, and student information.
Generated: DETERMINISTIC_774b62fd0ba65a03
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing student records and course enrollments at a music school

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Enrollment;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Faculty;
DROP TABLE IF EXISTS Instrument;

-- Table to store information about instruments
CREATE TABLE Instrument (
    instrument_id SERIAL PRIMARY KEY,  -- Unique identifier for each instrument
    name VARCHAR(100) NOT NULL,        -- Name of the instrument
    type VARCHAR(50) NOT NULL           -- Type of instrument (e.g., string, percussion)
);

-- Table to store faculty information
CREATE TABLE Faculty (
    faculty_id SERIAL PRIMARY KEY,      -- Unique identifier for each faculty member
    first_name VARCHAR(50) NOT NULL,   -- Faculty member's first name
    last_name VARCHAR(50) NOT NULL,    -- Faculty member's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Faculty member's email (must be unique)
    phone VARCHAR(15)                   -- Faculty member's phone number
);

-- Table to store student information
CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,      -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,   -- Student's first name
    last_name VARCHAR(50) NOT NULL,    -- Student's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Student's email (must be unique)
    phone VARCHAR(15),                  -- Student's phone number
    date_of_birth DATE NOT NULL         -- Student's date of birth
);

-- Table to store course information
CREATE TABLE Course (
    course_id SERIAL PRIMARY KEY,       -- Unique identifier for each course
    title VARCHAR(100) NOT NULL,        -- Title of the course
    description TEXT,                   -- Description of the course
    faculty_id INT NOT NULL,            -- Foreign key referencing Faculty
    instrument_id INT NOT NULL,         -- Foreign key referencing Instrument
    start_date DATE NOT NULL,           -- Start date of the course
    end_date DATE NOT NULL,             -- End date of the course
    FOREIGN KEY (faculty_id) REFERENCES Faculty(faculty_id) ON DELETE CASCADE,
    FOREIGN KEY (instrument_id) REFERENCES Instrument(instrument_id) ON DELETE CASCADE
);

-- Table to manage student enrollments in courses
CREATE TABLE Enrollment (
    enrollment_id SERIAL PRIMARY KEY,    -- Unique identifier for each enrollment
    student_id INT NOT NULL,             -- Foreign key referencing Student
    course_id INT NOT NULL,              -- Foreign key referencing Course
    enrollment_date DATE NOT NULL,       -- Date of enrollment
    FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES Course(course_id) ON DELETE CASCADE,
    UNIQUE (student_id, course_id)       -- Ensure a student can enroll in a course only once
);

-- Sample data insertion (optional, for testing purposes)
-- INSERT INTO Instrument (name, type) VALUES ('Piano', 'Keyboard'), ('Violin', 'String');
-- INSERT INTO Faculty (first_name, last_name, email, phone) VALUES ('John', 'Doe', 'john.doe@example.com', '123-456-7890');
-- INSERT INTO Student (first_name, last_name, email, phone, date_of_birth) VALUES ('Jane', 'Smith', 'jane.smith@example.com', '098-765-4321', '2000-01-01');
-- INSERT INTO Course (title, description, faculty_id, instrument_id, start_date, end_date) VALUES ('Beginner Piano', 'Introduction to piano playing', 1, 1, '2023-09-01', '2023-12-01');
-- INSERT INTO Enrollment (student_id, course_id, enrollment_date) VALUES (1, 1, '2023-08-15');
```
