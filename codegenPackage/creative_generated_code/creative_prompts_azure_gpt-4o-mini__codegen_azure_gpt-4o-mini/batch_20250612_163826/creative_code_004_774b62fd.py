"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcim.ru
Prompt: Design a database schema in SQL for managing student records and course enrollments at a music school, including tables for instruments, faculty, and student information.
Generated: DETERMINISTIC_774b62fd0ba65a03
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Creating a database for the Music School
CREATE DATABASE MusicSchool;

-- Switch to the MusicSchool database
USE MusicSchool;

-- Table for storing instrument information
CREATE TABLE Instruments (
    InstrumentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each instrument
    Name VARCHAR(100) NOT NULL,                  -- Name of the instrument
    Type VARCHAR(50) NOT NULL                     -- Type of instrument (e.g., String, Wind, Percussion)
);

-- Table for storing faculty information
CREATE TABLE Faculty (
    FacultyID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each faculty member
    FirstName VARCHAR(50) NOT NULL,              -- Faculty member's first name
    LastName VARCHAR(50) NOT NULL,                -- Faculty member's last name
    Email VARCHAR(100) UNIQUE NOT NULL,           -- Faculty member's email, must be unique
    PhoneNumber VARCHAR(15),                      -- Faculty member's phone number
    InstrumentID INT,                             -- Foreign key referencing Instruments
    FOREIGN KEY (InstrumentID) REFERENCES Instruments(InstrumentID)
);

-- Table for storing student information
CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,              -- Student's first name
    LastName VARCHAR(50) NOT NULL,                -- Student's last name
    Email VARCHAR(100) UNIQUE NOT NULL,           -- Student's email, must be unique
    PhoneNumber VARCHAR(15)                       -- Student's phone number
);

-- Table for managing course enrollments
CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each enrollment record
    StudentID INT NOT NULL,                        -- Foreign key referencing Students
    FacultyID INT NOT NULL,                        -- Foreign key referencing Faculty
    CourseName VARCHAR(100) NOT NULL,             -- Name of the course
    EnrollmentDate DATE NOT NULL,                  -- Date of enrollment
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID)
);

-- Table for tracking instrument assignments to students
CREATE TABLE StudentInstruments (
    AssignmentID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each instrument assignment
    StudentID INT NOT NULL,                        -- Foreign key referencing Students
    InstrumentID INT NOT NULL,                     -- Foreign key referencing Instruments
    AssignmentDate DATE NOT NULL,                  -- Date when the instrument was assigned
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (InstrumentID) REFERENCES Instruments(InstrumentID)
);

-- Ensure proper indexing for performance
CREATE INDEX idx_student_email ON Students(Email);
CREATE INDEX idx_faculty_email ON Faculty(Email);
CREATE INDEX idx_instrument_name ON Instruments(Name);
```
