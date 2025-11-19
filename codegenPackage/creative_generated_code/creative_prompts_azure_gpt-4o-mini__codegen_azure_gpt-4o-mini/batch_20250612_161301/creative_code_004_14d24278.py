"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Design a database schema in SQL for managing the administrative services of I.E Politécnico Municipal Cali, including tables for student information, academic programs, and faculty members.
Generated: DETERMINISTIC_14d24278b8d4f154
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for I.E Politécnico Municipal Cali
-- This schema includes tables for students, academic programs, and faculty members.

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS FacultyMembers;
DROP TABLE IF EXISTS AcademicPrograms;
DROP TABLE IF EXISTS Students;

-- Table for storing student information
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL, -- Student's first name
    last_name VARCHAR(50) NOT NULL, -- Student's last name
    date_of_birth DATE NOT NULL, -- Student's date of birth
    enrollment_date DATE NOT NULL, -- Date the student enrolled
    academic_program_id INT, -- Foreign key to link to AcademicPrograms
    email VARCHAR(100), -- Student's email address
    phone_number VARCHAR(15), -- Student's phone number
    FOREIGN KEY (academic_program_id) REFERENCES AcademicPrograms(program_id) ON DELETE SET NULL -- Relation to AcademicPrograms
);

-- Table for storing academic programs
CREATE TABLE AcademicPrograms (
    program_id SERIAL PRIMARY KEY, -- Unique identifier for each academic program
    program_name VARCHAR(100) NOT NULL, -- Name of the academic program
    description TEXT, -- Description of the academic program
    start_date DATE NOT NULL, -- Start date of the program
    end_date DATE NOT NULL -- End date of the program
);

-- Table for storing faculty member information
CREATE TABLE FacultyMembers (
    faculty_id SERIAL PRIMARY KEY, -- Unique identifier for each faculty member
    first_name VARCHAR(50) NOT NULL, -- Faculty member's first name
    last_name VARCHAR(50) NOT NULL, -- Faculty member's last name
    hire_date DATE NOT NULL, -- Date the faculty member was hired
    department VARCHAR(50) NOT NULL, -- Department the faculty member belongs to
    email VARCHAR(100), -- Faculty member's email address
    phone_number VARCHAR(15) -- Faculty member's phone number
);

-- Add constraints for data integrity
ALTER TABLE Students
ADD CONSTRAINT chk_email CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}$'); -- Email format check

-- Sample data insertion with error handling
BEGIN;

-- Inserting sample academic programs
INSERT INTO AcademicPrograms (program_name, description, start_date, end_date) VALUES
('Computer Science', 'Bachelor program in Computer Science', '2023-01-15', '2027-01-15'),
('Mechanical Engineering', 'Bachelor program in Mechanical Engineering', '2023-01-15', '2027-01-15')
ON CONFLICT DO NOTHING; -- Avoid duplicate entries

-- Inserting sample faculty members
INSERT INTO FacultyMembers (first_name, last_name, hire_date, department, email, phone_number) VALUES
('John', 'Doe', '2021-05-01', 'Engineering', 'john.doe@politecnico.edu', '1234567890'),
('Jane', 'Smith', '2019-08-15', 'Computer Science', 'jane.smith@politecnico.edu', '0987654321')
ON CONFLICT DO NOTHING; -- Avoid duplicate entries

-- Inserting sample students
INSERT INTO Students (first_name, last_name, date_of_birth, enrollment_date, academic_program_id, email, phone_number) VALUES
('Michael', 'Johnson', '2000-02-20', '2023-01-10', 1, 'michael.johnson@politecnico.edu', '5432167890'),
('Emily', 'Davis', '2001-03-15', '2023-01-11', 2, 'emily.davis@politecnico.edu', '6789054321')
ON CONFLICT DO NOTHING; -- Avoid duplicate entries

COMMIT;
```
