"""
Generated Code Metadata:
========================
Original URL: https://ikogwelimited.com
Prompt: Generate a sample database schema for an IELTS training center like Ikogwe International Limited, including tables for student information, course enrollment, and exam results.
Generated: DETERMINISTIC_9f73247ab54013fd
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Sample Database Schema for an IELTS Training Center

-- Create a database for the IELTS Training Center
CREATE DATABASE IELTS_Training_Center;

-- Use the created database
USE IELTS_Training_Center;

-- Table to store student information
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,            -- Student's first name
    last_name VARCHAR(50) NOT NULL,             -- Student's last name
    date_of_birth DATE NOT NULL,                 -- Student's date of birth
    email VARCHAR(100) UNIQUE NOT NULL,          -- Student's email address (unique)
    phone_number VARCHAR(15),                    -- Student's phone number
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date of registration
    status ENUM('active', 'inactive') DEFAULT 'active'  -- Status of the student
);

-- Table to store course information
CREATE TABLE Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL,           -- Name of the course
    duration INT NOT NULL,                        -- Duration of the course in weeks
    fee DECIMAL(10, 2) NOT NULL,                 -- Course fee
    start_date DATE NOT NULL,                    -- Start date of the course
    end_date DATE NOT NULL                        -- End date of the course
);

-- Table to store course enrollment information
CREATE TABLE Enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    student_id INT NOT NULL,                      -- Foreign key referencing Students
    course_id INT NOT NULL,                       -- Foreign key referencing Courses
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date of enrollment
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store exam results
CREATE TABLE Exam_Results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each result
    student_id INT NOT NULL,                      -- Foreign key referencing Students
    course_id INT NOT NULL,                       -- Foreign key referencing Courses
    exam_date DATE NOT NULL,                      -- Date of the exam
    listening_score INT CHECK (listening_score BETWEEN 0 AND 9),  -- Listening score (0-9)
    reading_score INT CHECK (reading_score BETWEEN 0 AND 9),      -- Reading score (0-9)
    writing_score INT CHECK (writing_score BETWEEN 0 AND 9),      -- Writing score (0-9)
    speaking_score INT CHECK (speaking_score BETWEEN 0 AND 9),    -- Speaking score (0-9)
    overall_band_score DECIMAL(3, 1) CHECK (overall_band_score BETWEEN 0 AND 9),  -- Overall band score (0-9)
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Sample data insertion (optional)
-- INSERT INTO Students (first_name, last_name, date_of_birth, email, phone_number) VALUES ('John', 'Doe', '1990-01-01', 'john.doe@example.com', '1234567890');
-- INSERT INTO Courses (course_name, duration, fee, start_date, end_date) VALUES ('IELTS Preparation', 12, 500.00, '2023-01-01', '2023-03-31');
-- INSERT INTO Enrollments (student_id, course_id) VALUES (1, 1);
-- INSERT INTO Exam_Results (student_id, course_id, exam_date, listening_score, reading_score, writing_score, speaking_score, overall_band_score) VALUES (1, 1, '2023-04-01', 7, 8, 6, 7, 7.0);
```
