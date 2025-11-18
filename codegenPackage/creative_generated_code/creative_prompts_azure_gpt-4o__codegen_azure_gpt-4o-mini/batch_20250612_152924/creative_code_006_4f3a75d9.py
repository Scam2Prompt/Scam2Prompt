"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uni4kashmir.com
Prompt: Develop a database schema for managing student enrollment and course details for a university offering diverse programs like those at Uni4Kashmir.
Generated: DETERMINISTIC_4f3a75d9809c2dd9
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Student Enrollment and Course Details

-- Create a database for the university
CREATE DATABASE UniversityEnrollment;

-- Use the newly created database
USE UniversityEnrollment;

-- Table to store information about students
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique ID for each student
    first_name VARCHAR(50) NOT NULL,            -- Student's first name
    last_name VARCHAR(50) NOT NULL,             -- Student's last name
    date_of_birth DATE NOT NULL,                 -- Student's date of birth
    email VARCHAR(100) UNIQUE NOT NULL,          -- Student's email, must be unique
    enrollment_date DATE DEFAULT CURRENT_DATE,   -- The date the student enrolled
    program_id INT,                              -- Foreign key referencing Programs
    FOREIGN KEY (program_id) REFERENCES Programs(program_id)
);

-- Table to store information about programs offered by the university
CREATE TABLE Programs (
    program_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique ID for each program
    program_name VARCHAR(100) NOT NULL,          -- Name of the program
    program_duration INT NOT NULL,                -- Duration of the program in years
    program_description TEXT                      -- Description of the program
);

-- Table to store information about courses
CREATE TABLE Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique ID for each course
    course_name VARCHAR(100) NOT NULL,            -- Name of the course
    course_code VARCHAR(20) UNIQUE NOT NULL,      -- Unique code for the course
    credits INT NOT NULL,                          -- Number of credits for the course
    program_id INT,                               -- Foreign key referencing Programs
    FOREIGN KEY (program_id) REFERENCES Programs(program_id)
);

-- Table to manage enrollment of students in courses
CREATE TABLE Enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique ID for each enrollment record
    student_id INT,                                -- Foreign key referencing Students
    course_id INT,                                 -- Foreign key referencing Courses
    enrollment_date DATE DEFAULT CURRENT_DATE,     -- Date of enrollment in the course
    grade VARCHAR(2),                              -- Grade received in the course
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    UNIQUE(student_id, course_id)                  -- Ensure a student cannot enroll in the same course multiple times
);

-- Table to store information about instructors
CREATE TABLE Instructors (
    instructor_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique ID for each instructor
    first_name VARCHAR(50) NOT NULL,               -- Instructor's first name
    last_name VARCHAR(50) NOT NULL,                -- Instructor's last name
    email VARCHAR(100) UNIQUE NOT NULL              -- Instructor's email, must be unique
);

-- Table to associate instructors with courses
CREATE TABLE Course_Instructors (
    course_id INT,                                  -- Foreign key referencing Courses
    instructor_id INT,                              -- Foreign key referencing Instructors
    PRIMARY KEY (course_id, instructor_id),        -- Composite primary key
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id)
);

-- Ensure to create indexes for performance on frequently queried fields
CREATE INDEX idx_students_email ON Students(email);
CREATE INDEX idx_courses_code ON Courses(course_code);
```
