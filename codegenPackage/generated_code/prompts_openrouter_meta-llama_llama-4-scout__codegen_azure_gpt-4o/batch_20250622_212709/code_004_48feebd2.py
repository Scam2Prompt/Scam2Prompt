"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Design a database schema to store information about SOMTU's MBA programs, including program details, course structures, and student records, and provide a simple SQL query to demonstrate its usage.
Generated: DETERMINISTIC_48feebd272893d13
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for SOMTU's MBA Programs

-- Table to store program details
CREATE TABLE Programs (
    ProgramID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL,        -- Name of the MBA program
    DurationYears INT NOT NULL,               -- Duration of the program in years
    Description TEXT                          -- Description of the program
);

-- Table to store course structures
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each course
    ProgramID INT NOT NULL,                   -- Foreign key linking to Programs table
    CourseName VARCHAR(255) NOT NULL,         -- Name of the course
    Credits INT NOT NULL,                     -- Number of credits for the course
    Semester INT NOT NULL,                    -- Semester in which the course is offered
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE
);

-- Table to store student records
CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each student
    FullName VARCHAR(255) NOT NULL,           -- Full name of the student
    Email VARCHAR(255) UNIQUE NOT NULL,       -- Email address of the student
    ProgramID INT NOT NULL,                   -- Foreign key linking to Programs table
    EnrollmentDate DATE NOT NULL,             -- Date of enrollment
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE
);

-- Table to store student-course enrollment
CREATE TABLE StudentCourses (
    EnrollmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key linking to Students table
    CourseID INT NOT NULL,                       -- Foreign key linking to Courses table
    Grade VARCHAR(5),                            -- Grade received by the student
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Example SQL query to demonstrate usage: Fetch all students enrolled in a specific program along with their courses and grades
SELECT 
    s.StudentID,
    s.FullName,
    s.Email,
    p.ProgramName,
    c.CourseName,
    sc.Grade
FROM 
    Students s
JOIN 
    Programs p ON s.ProgramID = p.ProgramID
JOIN 
    StudentCourses sc ON s.StudentID = sc.StudentID
JOIN 
    Courses c ON sc.CourseID = c.CourseID
WHERE 
    p.ProgramName = 'MBA in Finance'; -- Replace with the desired program name
```
