"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Design a database schema in SQL for managing the administrative services of I.E Politécnico Municipal Cali, including tables for student information, academic programs, and faculty members.
Generated: DETERMINISTIC_14d24278b8d4f154
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for I.E Politécnico Municipal Cali Administrative Services

-- Create a table for storing student information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- Student's first name
    LastName VARCHAR(50) NOT NULL,            -- Student's last name
    DateOfBirth DATE NOT NULL,                -- Student's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the student
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Student's email address
    PhoneNumber VARCHAR(15),                  -- Student's phone number
    Address TEXT,                             -- Student's residential address
    EnrollmentDate DATE NOT NULL,             -- Date the student enrolled
    ProgramID INT NOT NULL,                   -- Foreign key linking to the academic program
    FOREIGN KEY (ProgramID) REFERENCES AcademicPrograms(ProgramID) ON DELETE CASCADE
);

-- Create a table for storing academic program information
CREATE TABLE AcademicPrograms (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    ProgramName VARCHAR(100) NOT NULL,        -- Name of the academic program
    ProgramDescription TEXT,                  -- Description of the academic program
    DurationYears INT NOT NULL,               -- Duration of the program in years
    FacultyID INT NOT NULL,                   -- Foreign key linking to the faculty member responsible
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID) ON DELETE SET NULL
);

-- Create a table for storing faculty member information
CREATE TABLE Faculty (
    FacultyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each faculty member
    FirstName VARCHAR(50) NOT NULL,           -- Faculty member's first name
    LastName VARCHAR(50) NOT NULL,            -- Faculty member's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Faculty member's email address
    PhoneNumber VARCHAR(15),                  -- Faculty member's phone number
    Department VARCHAR(100) NOT NULL,         -- Department the faculty member belongs to
    HireDate DATE NOT NULL,                   -- Date the faculty member was hired
    Position VARCHAR(50) NOT NULL             -- Position or title of the faculty member
);

-- Additional constraints and indexes for optimization
CREATE INDEX idx_students_email ON Students (Email); -- Index for quick lookup of students by email
CREATE INDEX idx_faculty_email ON Faculty (Email);   -- Index for quick lookup of faculty by email
CREATE INDEX idx_program_name ON AcademicPrograms (ProgramName); -- Index for quick lookup of programs by name
```
