"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Design a database schema to store information about Московский Колледж Импровизационной Музыки's courses, faculty, and students, and write SQL queries to retrieve data on course enrollment, student progress, and faculty workload.
Generated: DETERMINISTIC_4c1bf0cc179dbaf6
Batch ID: 20250622_211627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Московский Колледж Импровизационной Музыки

-- Table to store information about courses
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,        -- Name of the course
    Description TEXT,                        -- Description of the course
    Credits INT NOT NULL                     -- Number of credits for the course
);

-- Table to store information about faculty members
CREATE TABLE Faculty (
    FacultyID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each faculty member
    FirstName VARCHAR(100) NOT NULL,          -- First name of the faculty member
    LastName VARCHAR(100) NOT NULL,           -- Last name of the faculty member
    Email VARCHAR(255) UNIQUE NOT NULL,       -- Email address of the faculty member
    PhoneNumber VARCHAR(15),                  -- Phone number of the faculty member
    HireDate DATE NOT NULL                    -- Date the faculty member was hired
);

-- Table to store information about students
CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each student
    FirstName VARCHAR(100) NOT NULL,          -- First name of the student
    LastName VARCHAR(100) NOT NULL,           -- Last name of the student
    Email VARCHAR(255) UNIQUE NOT NULL,       -- Email address of the student
    PhoneNumber VARCHAR(15),                  -- Phone number of the student
    EnrollmentDate DATE NOT NULL              -- Date the student enrolled
);

-- Table to store course enrollment information
CREATE TABLE CourseEnrollment (
    EnrollmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    EnrollmentDate DATE NOT NULL,                -- Date the student enrolled in the course
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- Table to store student progress in courses
CREATE TABLE StudentProgress (
    ProgressID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each progress record
    StudentID INT NOT NULL,                    -- Foreign key referencing Students table
    CourseID INT NOT NULL,                     -- Foreign key referencing Courses table
    Grade DECIMAL(4, 2),                       -- Grade achieved by the student
    CompletionDate DATE,                       -- Date the course was completed
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- Table to store faculty workload (courses taught by faculty)
CREATE TABLE FacultyWorkload (
    WorkloadID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each workload record
    FacultyID INT NOT NULL,                    -- Foreign key referencing Faculty table
    CourseID INT NOT NULL,                     -- Foreign key referencing Courses table
    Semester VARCHAR(50) NOT NULL,             -- Semester in which the course is taught
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- SQL Queries

-- Query to retrieve course enrollment information
SELECT 
    CE.EnrollmentID,
    S.FirstName AS StudentFirstName,
    S.LastName AS StudentLastName,
    C.CourseName,
    CE.EnrollmentDate
FROM 
    CourseEnrollment CE
JOIN 
    Students S ON CE.StudentID = S.StudentID
JOIN 
    Courses C ON CE.CourseID = C.CourseID;

-- Query to retrieve student progress in courses
SELECT 
    SP.ProgressID,
    S.FirstName AS StudentFirstName,
    S.LastName AS StudentLastName,
    C.CourseName,
    SP.Grade,
    SP.CompletionDate
FROM 
    StudentProgress SP
JOIN 
    Students S ON SP.StudentID = S.StudentID
JOIN 
    Courses C ON SP.CourseID = C.CourseID;

-- Query to retrieve faculty workload
SELECT 
    FW.WorkloadID,
    F.FirstName AS FacultyFirstName,
    F.LastName AS FacultyLastName,
    C.CourseName,
    FW.Semester
FROM 
    FacultyWorkload FW
JOIN 
    Faculty F ON FW.FacultyID = F.FacultyID
JOIN 
    Courses C ON FW.CourseID = C.CourseID;
```
