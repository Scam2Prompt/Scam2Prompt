"""
Generated Code Metadata:
========================
Original URL: https://ydmc.edu.np
Prompt: Generate a sample database schema for storing information about students, faculty members, and programs at YDMC using MySQL.
Generated: DETERMINISTIC_b0c463aeaa05482d
Batch ID: 20250622_205217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for YDMC to store information about students, faculty members, and programs

-- Create the database
CREATE DATABASE IF NOT EXISTS YDMC;
USE YDMC;

-- Table to store program information
CREATE TABLE Programs (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    ProgramName VARCHAR(100) NOT NULL,        -- Name of the program
    ProgramDescription TEXT,                 -- Description of the program
    DurationYears INT NOT NULL,              -- Duration of the program in years
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store student information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- First name of the student
    LastName VARCHAR(50) NOT NULL,            -- Last name of the student
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Email address of the student
    PhoneNumber VARCHAR(15),                  -- Contact number of the student
    DateOfBirth DATE NOT NULL,                -- Date of birth of the student
    ProgramID INT NOT NULL,                   -- Foreign key referencing the program the student is enrolled in
    EnrollmentDate DATE NOT NULL,             -- Date of enrollment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store faculty member information
CREATE TABLE FacultyMembers (
    FacultyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each faculty member
    FirstName VARCHAR(50) NOT NULL,           -- First name of the faculty member
    LastName VARCHAR(50) NOT NULL,            -- Last name of the faculty member
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Email address of the faculty member
    PhoneNumber VARCHAR(15),                  -- Contact number of the faculty member
    HireDate DATE NOT NULL,                   -- Date of hire
    Department VARCHAR(100) NOT NULL,         -- Department the faculty member belongs to
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store relationships between faculty members and programs
CREATE TABLE FacultyPrograms (
    FacultyProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the relationship
    FacultyID INT NOT NULL,                          -- Foreign key referencing the faculty member
    ProgramID INT NOT NULL,                          -- Foreign key referencing the program
    AssignedDate DATE NOT NULL,                      -- Date the faculty member was assigned to the program
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (FacultyID) REFERENCES FacultyMembers(FacultyID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_students_programid ON Students(ProgramID);
CREATE INDEX idx_facultyprograms_facultyid ON FacultyPrograms(FacultyID);
CREATE INDEX idx_facultyprograms_programid ON FacultyPrograms(ProgramID);
```
