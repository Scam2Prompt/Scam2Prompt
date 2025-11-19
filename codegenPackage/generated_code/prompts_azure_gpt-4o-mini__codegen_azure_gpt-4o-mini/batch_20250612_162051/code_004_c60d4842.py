"""
Generated Code Metadata:
========================
Original URL: https://crestagile.com
Prompt: Design a database schema for storing information about Agile certifications and course offerings, reflecting the structure used by CrestAgile.
Generated: DETERMINISTIC_c60d4842104cd79d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about Agile certifications and course offerings

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS CourseOffering;
DROP TABLE IF EXISTS Certification;
DROP TABLE IF EXISTS Instructor;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Enrollment;

-- Table to store information about Agile certifications
CREATE TABLE Certification (
    CertificationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each certification
    Name VARCHAR(255) NOT NULL,                     -- Name of the certification
    Description TEXT,                                -- Description of the certification
    IssuingOrganization VARCHAR(255) NOT NULL,      -- Organization that issues the certification
    ValidityPeriod INT,                              -- Validity period in months
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of when the certification was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about course offerings
CREATE TABLE CourseOffering (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each course
    CertificationID INT,                             -- Foreign key referencing Certification
    Title VARCHAR(255) NOT NULL,                     -- Title of the course
    Description TEXT,                                -- Description of the course
    StartDate DATE NOT NULL,                         -- Start date of the course
    EndDate DATE NOT NULL,                           -- End date of the course
    Location VARCHAR(255),                           -- Location of the course
    InstructorID INT,                                -- Foreign key referencing Instructor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of when the course was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CertificationID) REFERENCES Certification(CertificationID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID) ON DELETE SET NULL -- Ensure referential integrity
);

-- Table to store information about instructors
CREATE TABLE Instructor (
    InstructorID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each instructor
    FirstName VARCHAR(100) NOT NULL,                -- First name of the instructor
    LastName VARCHAR(100) NOT NULL,                  -- Last name of the instructor
    Email VARCHAR(255) UNIQUE NOT NULL,              -- Email of the instructor
    Bio TEXT,                                        -- Short biography of the instructor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of when the instructor was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about students
CREATE TABLE Student (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each student
    FirstName VARCHAR(100) NOT NULL,                 -- First name of the student
    LastName VARCHAR(100) NOT NULL,                  -- Last name of the student
    Email VARCHAR(255) UNIQUE NOT NULL,              -- Email of the student
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of when the student was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store enrollment information linking students to course offerings
CREATE TABLE Enrollment (
    EnrollmentID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each enrollment
    StudentID INT,                                   -- Foreign key referencing Student
    CourseID INT,                                    -- Foreign key referencing CourseOffering
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of enrollment
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (CourseID) REFERENCES CourseOffering(CourseID) ON DELETE CASCADE -- Ensure referential integrity
);
```
