"""
Generated Code Metadata:
========================
Original URL: https://cnu.university
Prompt: Generate code to create a database schema for managing degree programs such as "PhD in Environmental Science" and "Diploma in Graphic Design," based on the program structure provided by CNU.
Generated: DETERMINISTIC_6779accf52fae642
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for managing degree programs

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Programs;
DROP TABLE IF EXISTS Departments;

-- Create a table to store departments
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each department
    DepartmentName VARCHAR(100) NOT NULL,         -- Name of the department
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to store degree programs
CREATE TABLE Programs (
    ProgramID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each program
    ProgramName VARCHAR(100) NOT NULL,             -- Name of the degree program
    DepartmentID INT,                               -- Foreign key referencing Departments
    ProgramType ENUM('Degree', 'Diploma') NOT NULL, -- Type of program (Degree or Diploma)
    Duration INT NOT NULL,                          -- Duration of the program in years
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID) -- Foreign key constraint
);

-- Create a table to store courses associated with each program
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,              -- Name of the course
    ProgramID INT,                                  -- Foreign key referencing Programs
    Credits INT NOT NULL,                           -- Number of credits for the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) -- Foreign key constraint
);

-- Sample data insertion for Departments
INSERT INTO Departments (DepartmentName) VALUES 
('Environmental Science'),
('Graphic Design');

-- Sample data insertion for Programs
INSERT INTO Programs (ProgramName, DepartmentID, ProgramType, Duration) VALUES 
('PhD in Environmental Science', 1, 'Degree', 4),
('Diploma in Graphic Design', 2, 'Diploma', 1);

-- Sample data insertion for Courses
INSERT INTO Courses (CourseName, ProgramID, Credits) VALUES 
('Advanced Environmental Policy', 1, 3),
('Graphic Design Fundamentals', 2, 3);
```
