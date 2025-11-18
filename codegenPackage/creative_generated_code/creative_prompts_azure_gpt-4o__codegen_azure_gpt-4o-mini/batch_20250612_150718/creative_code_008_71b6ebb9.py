"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somtu.edu.np
Prompt: Develop a database schema to store information about SOMTU's MBA faculty, courses, and student research projects as described on the website.
Generated: DETERMINISTIC_71b6ebb9222c16b7
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for SOMTU's MBA Faculty, Courses, and Student Research Projects

-- Create a database for SOMTU
CREATE DATABASE somtu_mba;

-- Use the newly created database
USE somtu_mba;

-- Table to store faculty information
CREATE TABLE Faculty (
    FacultyID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each faculty member
    FirstName VARCHAR(50) NOT NULL,            -- First name of the faculty member
    LastName VARCHAR(50) NOT NULL,             -- Last name of the faculty member
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Email address of the faculty member
    PhoneNumber VARCHAR(15),                    -- Optional phone number
    Department VARCHAR(50),                     -- Department the faculty belongs to
    HireDate DATE NOT NULL                      -- Date the faculty was hired
);

-- Table to store course information
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,           -- Name of the course
    CourseCode VARCHAR(10) NOT NULL UNIQUE,     -- Unique code for the course
    Credits INT NOT NULL CHECK (Credits > 0),   -- Number of credits for the course
    FacultyID INT,                               -- Foreign key referencing Faculty
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID) ON DELETE SET NULL -- Relationship with Faculty
);

-- Table to store student research projects
CREATE TABLE ResearchProjects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each research project
    ProjectTitle VARCHAR(255) NOT NULL,          -- Title of the research project
    StudentName VARCHAR(100) NOT NULL,           -- Name of the student working on the project
    FacultyAdvisorID INT,                         -- Faculty advisor for the project
    CourseID INT,                                 -- Course associated with the research project
    StartDate DATE NOT NULL,                      -- Start date of the project
    EndDate DATE,                                 -- End date of the project (optional)
    FOREIGN KEY (FacultyAdvisorID) REFERENCES Faculty(FacultyID) ON DELETE SET NULL, -- Relationship with Faculty
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE SET NULL -- Relationship with Courses
);

-- Example of inserting a faculty member
INSERT INTO Faculty (FirstName, LastName, Email, PhoneNumber, Department, HireDate)
VALUES ('John', 'Doe', 'johndoe@somtu.edu', '123-456-7890', 'Marketing', '2022-01-15');

-- Example of inserting a course
INSERT INTO Courses (CourseName, CourseCode, Credits, FacultyID)
VALUES ('Digital Marketing', 'MKT101', 3, 1);

-- Example of inserting a research project
INSERT INTO ResearchProjects (ProjectTitle, StudentName, FacultyAdvisorID, CourseID, StartDate)
VALUES ('Impact of Social Media on Consumer Behavior', 'Jane Smith', 1, 1, '2023-09-01');

-- Ensure that data integrity is maintained with proper error handling
-- Note: Error handling would be implemented in the application layer using prepared statements or ORM to avoid SQL injection.
```
