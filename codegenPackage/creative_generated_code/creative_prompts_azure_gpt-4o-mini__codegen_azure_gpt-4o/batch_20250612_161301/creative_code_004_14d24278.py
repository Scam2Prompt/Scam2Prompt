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
-- Database Schema for Managing Administrative Services at I.E Politécnico Municipal Cali

-- Create a table for storing student information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- Student's first name
    LastName VARCHAR(50) NOT NULL,            -- Student's last name
    DateOfBirth DATE NOT NULL,                -- Student's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Student's gender
    Email VARCHAR(100) NOT NULL UNIQUE,       -- Student's email address
    PhoneNumber VARCHAR(15),                  -- Optional phone number
    Address TEXT NOT NULL,                    -- Student's residential address
    ProgramID INT NOT NULL,                   -- Foreign key reference to the academic program
    EnrollmentDate DATE NOT NULL,             -- Date of enrollment
    Status ENUM('Active', 'Inactive') NOT NULL DEFAULT 'Active', -- Student status in the institution
    FOREIGN KEY (ProgramID) REFERENCES AcademicPrograms(ProgramID) -- Relationship to AcademicPrograms
);

-- Create a table for storing academic program information
CREATE TABLE AcademicPrograms (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each academic program
    ProgramName VARCHAR(100) NOT NULL,        -- Name of the academic program
    Description TEXT,                         -- Program description
    DurationYears INT NOT NULL,               -- Duration of the program in years
    Credits INT NOT NULL,                     -- Total number of credits for the program
    ActiveStatus ENUM('Active', 'Inactive') NOT NULL DEFAULT 'Active' -- Status of the program
);

-- Create a table for storing faculty member information
CREATE TABLE FacultyMembers (
    FacultyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each faculty member
    FirstName VARCHAR(50) NOT NULL,           -- Faculty member's first name
    LastName VARCHAR(50) NOT NULL,            -- Faculty member's last name
    Email VARCHAR(100) NOT NULL UNIQUE,       -- Faculty member's email address
    PhoneNumber VARCHAR(15),                  -- Optional phone number
    Address TEXT NOT NULL,                    -- Faculty member's residential address
    HireDate DATE NOT NULL,                   -- Date of hiring
    Department VARCHAR(100) NOT NULL,         -- Department the faculty member belongs to
    Title VARCHAR(50) NOT NULL,               -- Job title (e.g., Professor, Lecturer)
    Status ENUM('Active', 'Inactive') NOT NULL DEFAULT 'Active' -- Faculty member's employment status
);

-- Add proper indexing for faster query performance
CREATE INDEX idx_students_email ON Students(Email);
CREATE INDEX idx_academicprograms_programname ON AcademicPrograms(ProgramName);
CREATE INDEX idx_facultymembers_email ON FacultyMembers(Email);

-- Error handling is implemented at the application level for validations and constraints
-- Ensure the schema follows best practices for relational database design
```
