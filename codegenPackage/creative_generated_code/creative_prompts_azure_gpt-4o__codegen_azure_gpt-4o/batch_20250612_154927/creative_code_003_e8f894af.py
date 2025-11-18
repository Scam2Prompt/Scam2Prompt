"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://institutopangoa.edu.pe
Prompt: Create a database schema for managing technical education programs, including "Enfermería Técnica" and "Producción Agropecuaria," based on the programs listed on the Instituto Pangoa website.
Generated: DETERMINISTIC_e8f894af6fb335d6
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Technical Education Programs

-- Create a new database for technical education programs
CREATE DATABASE IF NOT EXISTS TechnicalEducation;
USE TechnicalEducation;

-- Table for storing information about programs
CREATE TABLE IF NOT EXISTS Programs (
    program_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    program_name VARCHAR(255) NOT NULL,       -- Name of the program
    description TEXT,                         -- Description of the program
    duration_months INT NOT NULL,             -- Duration of the program in months
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the program was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for storing information about instructors
CREATE TABLE IF NOT EXISTS Instructors (
    instructor_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each instructor
    first_name VARCHAR(100) NOT NULL,            -- First name of the instructor
    last_name VARCHAR(100) NOT NULL,             -- Last name of the instructor
    email VARCHAR(255) UNIQUE NOT NULL,          -- Contact email of the instructor
    phone_number VARCHAR(20),                    -- Contact phone number of the instructor
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the instructor was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for storing information about students
CREATE TABLE IF NOT EXISTS Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(100) NOT NULL,          -- First name of the student
    last_name VARCHAR(100) NOT NULL,           -- Last name of the student
    email VARCHAR(255) UNIQUE NOT NULL,        -- Contact email of the student
    phone_number VARCHAR(20),                  -- Contact phone number of the student
    birth_date DATE,                           -- Birth date of the student
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the student was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for managing enrollment (students enrolled in programs)
CREATE TABLE IF NOT EXISTS Enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment record
    student_id INT NOT NULL,                      -- Foreign key referencing Students table
    program_id INT NOT NULL,                      -- Foreign key referencing Programs table
    enrollment_date DATE NOT NULL,                -- Date of enrollment
    status ENUM('Active', 'Completed', 'Dropped') DEFAULT 'Active', -- Status of enrollment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the enrollment was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE, -- On student deletion, cascade
    FOREIGN KEY (program_id) REFERENCES Programs(program_id) ON DELETE CASCADE  -- On program deletion, cascade
);

-- Insert pre-defined programs ("Enfermería Técnica" and "Producción Agropecuaria")
INSERT INTO Programs (program_name, description, duration_months)
VALUES 
    ('Enfermería Técnica', 'Focused on providing technical education in nursing practices.', 24),
    ('Producción Agropecuaria', 'Specialized in agricultural production and rural development.', 18);

-- Add indexes to improve query performance
CREATE INDEX idx_program_name ON Programs(program_name);
CREATE INDEX idx_instructor_email ON Instructors(email);
CREATE INDEX idx_student_email ON Students(email);
CREATE INDEX idx_enrollment_status ON Enrollments(status);

-- Error handling notes:
-- Ensure foreign key constraints are enforced correctly, and indexes are optimized for efficient queries.
-- Implement application-level validation to prevent duplicate or invalid entries into the database.
```
