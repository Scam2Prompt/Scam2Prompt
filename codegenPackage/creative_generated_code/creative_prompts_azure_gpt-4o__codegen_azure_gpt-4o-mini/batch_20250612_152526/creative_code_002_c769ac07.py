"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Create a database schema in SQL to organize data for an educational institution, including tables for student records, teacher assignments, institutional achievements, and administrative processes, inspired by the structure of the Politécnico Municipal de Cali.
Generated: DETERMINISTIC_c769ac07c51818fa
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for an educational institution

-- Create the database
CREATE DATABASE IF NOT EXISTS EducationalInstitution;

-- Use the created database
USE EducationalInstitution;

-- Table for storing student records
CREATE TABLE IF NOT EXISTS Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,           -- Student's first name
    last_name VARCHAR(50) NOT NULL,            -- Student's last name
    date_of_birth DATE NOT NULL,                -- Student's date of birth
    enrollment_date DATE NOT NULL,              -- Date of enrollment
    email VARCHAR(100) UNIQUE NOT NULL,         -- Student's email, must be unique
    phone_number VARCHAR(15),                   -- Optional: Student's phone number
    address VARCHAR(255)                        -- Optional: Student's address
);

-- Table for storing teacher assignments
CREATE TABLE IF NOT EXISTS Teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each teacher
    first_name VARCHAR(50) NOT NULL,             -- Teacher's first name
    last_name VARCHAR(50) NOT NULL,              -- Teacher's last name
    email VARCHAR(100) UNIQUE NOT NULL,           -- Teacher's email, must be unique
    phone_number VARCHAR(15),                     -- Optional: Teacher's phone number
    subject VARCHAR(50) NOT NULL                  -- Subject taught by the teacher
);

-- Table for storing courses offered by the institution
CREATE TABLE IF NOT EXISTS Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL,            -- Name of the course
    course_description TEXT,                       -- Description of the course
    credits INT NOT NULL                           -- Number of credits for the course
);

-- Table for assigning teachers to courses
CREATE TABLE IF NOT EXISTS TeacherAssignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique assignment identifier
    teacher_id INT NOT NULL,                       -- Foreign key referencing Teachers table
    course_id INT NOT NULL,                        -- Foreign key referencing Courses table
    semester VARCHAR(10) NOT NULL,                -- Semester of the assignment
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
        ON DELETE CASCADE,                        -- Delete assignments if the teacher is deleted
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
        ON DELETE CASCADE                         -- Delete assignments if the course is deleted
);

-- Table for recording institutional achievements
CREATE TABLE IF NOT EXISTS Achievements (
    achievement_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each achievement
    title VARCHAR(100) NOT NULL,                   -- Title of the achievement
    description TEXT,                              -- Description of the achievement
    date_awarded DATE NOT NULL                     -- Date the achievement was awarded
);

-- Table for managing administrative processes
CREATE TABLE IF NOT EXISTS AdministrativeProcesses (
    process_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each process
    process_name VARCHAR(100) NOT NULL,            -- Name of the process
    description TEXT,                               -- Description of the process
    status ENUM('Pending', 'In Progress', 'Completed') NOT NULL DEFAULT 'Pending' -- Status of the process
);

-- Insert sample data into Students table
INSERT INTO Students (first_name, last_name, date_of_birth, enrollment_date, email)
VALUES 
    ('John', 'Doe', '2000-01-15', '2022-08-01', 'john.doe@example.com'),
    ('Jane', 'Smith', '2001-02-20', '2022-08-01', 'jane.smith@example.com');

-- Insert sample data into Teachers table
INSERT INTO Teachers (first_name, last_name, email, subject)
VALUES
    ('Alice', 'Johnson', 'alice.johnson@example.com', 'Mathematics'),
    ('Bob', 'Brown', 'bob.brown@example.com', 'Physics');

-- Insert sample data into Courses table
INSERT INTO Courses (course_name, course_description, credits)
VALUES
    ('Calculus I', 'Introduction to Calculus', 3),
    ('Physics I', 'Introduction to Physics', 4);

-- Insert sample data into Achievements table
INSERT INTO Achievements (title, description, date_awarded)
VALUES
    ('Top Institution in STEM', 'Recognized as the top institution in STEM education.', '2023-05-01');

-- Insert sample data into AdministrativeProcesses table
INSERT INTO AdministrativeProcesses (process_name, description)
VALUES
    ('Enrollment Process', 'Process for enrolling new students.'),
    ('Course Registration', 'Process for students to register for courses each semester.');
```
