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
-- Database Schema for SOMTU MBA Faculty, Courses, and Student Research Projects

-- Create a table to store faculty information
CREATE TABLE Faculty (
    FacultyID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each faculty member
    FirstName VARCHAR(50) NOT NULL,            -- First name of the faculty member
    LastName VARCHAR(50) NOT NULL,             -- Last name of the faculty member
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Email address of the faculty member
    PhoneNumber VARCHAR(15),                   -- Contact number of the faculty member
    Department VARCHAR(100) NOT NULL,          -- Department the faculty belongs to
    Position VARCHAR(100),                     -- Job title/position of the faculty member
    DateJoined DATE                            -- Date the faculty member joined SOMTU
);

-- Create a table to store course information
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,          -- Name of the course
    CourseCode VARCHAR(20) UNIQUE NOT NULL,    -- Unique code for the course
    Credits INT NOT NULL,                      -- Number of credit hours for the course
    FacultyID INT,                             -- Foreign key linking to the Faculty table
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID) ON DELETE SET NULL
);

-- Create a table to store student research project information
CREATE TABLE ResearchProjects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each research project
    ProjectTitle VARCHAR(255) NOT NULL,        -- Title of the research project
    StudentName VARCHAR(100) NOT NULL,         -- Name of the student undertaking the project
    FacultyID INT,                             -- Foreign key linking to the Faculty table (supervisor)
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID) ON DELETE SET NULL,
    StartDate DATE NOT NULL,                   -- Start date of the research project
    EndDate DATE,                              -- End date of the research project
    Status ENUM('Ongoing', 'Completed') DEFAULT 'Ongoing', -- Current status of the project
    Description TEXT                           -- Detailed description of the research project
);

-- Create a table to store faculty-student relationships for research projects
CREATE TABLE FacultyStudentRelation (
    RelationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each relation
    FacultyID INT NOT NULL,                    -- Foreign key referencing Faculty table
    StudentName VARCHAR(100) NOT NULL,         -- Name of the student
    ProjectID INT,                             -- Foreign key referencing ResearchProjects table
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID) ON DELETE CASCADE,
    FOREIGN KEY (ProjectID) REFERENCES ResearchProjects(ProjectID) ON DELETE CASCADE,
    RelationType ENUM('Supervisor', 'Co-Supervisor') DEFAULT 'Supervisor' -- Type of relationship
);

-- Create indexes for faster querying
CREATE INDEX idx_faculty_email ON Faculty (Email);
CREATE INDEX idx_course_code ON Courses (CourseCode);
CREATE INDEX idx_project_status ON ResearchProjects (Status);
```
