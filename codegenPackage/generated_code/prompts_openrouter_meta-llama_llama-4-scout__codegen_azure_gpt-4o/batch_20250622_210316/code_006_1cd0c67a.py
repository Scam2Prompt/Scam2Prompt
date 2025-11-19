"""
Generated Code Metadata:
========================
Original URL: https://cuicalli.edu.mx
Prompt: Create a database schema to store information about Universidad Tecnológico Cuicalli's students, faculty, and courses, and write a SQL query to retrieve the data.
Generated: DETERMINISTIC_1cd0c67a2a308831
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for Universidad Tecnológico Cuicalli
-- This schema includes tables for students, faculty, courses, and enrollments.

-- Create the students table
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- Student's first name
    LastName VARCHAR(50) NOT NULL,            -- Student's last name
    DateOfBirth DATE NOT NULL,                -- Student's date of birth
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Student's email address
    PhoneNumber VARCHAR(15),                  -- Student's phone number
    EnrollmentDate DATE NOT NULL              -- Date the student enrolled
);

-- Create the faculty table
CREATE TABLE Faculty (
    FacultyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each faculty member
    FirstName VARCHAR(50) NOT NULL,           -- Faculty member's first name
    LastName VARCHAR(50) NOT NULL,            -- Faculty member's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Faculty member's email address
    PhoneNumber VARCHAR(15),                  -- Faculty member's phone number
    HireDate DATE NOT NULL                    -- Date the faculty member was hired
);

-- Create the courses table
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,         -- Name of the course
    CourseCode VARCHAR(10) UNIQUE NOT NULL,   -- Unique code for the course
    Credits INT NOT NULL,                     -- Number of credits for the course
    FacultyID INT NOT NULL,                   -- Faculty member teaching the course
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID) ON DELETE CASCADE
);

-- Create the enrollments table
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Student enrolled in the course
    CourseID INT NOT NULL,                       -- Course the student is enrolled in
    EnrollmentDate DATE NOT NULL,                -- Date of enrollment
    Grade DECIMAL(4, 2),                         -- Grade received in the course
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Query to retrieve data: List all students with their enrolled courses and the faculty teaching those courses
SELECT 
    s.StudentID,
    s.FirstName AS StudentFirstName,
    s.LastName AS StudentLastName,
    c.CourseName,
    c.CourseCode,
    f.FirstName AS FacultyFirstName,
    f.LastName AS FacultyLastName,
    e.EnrollmentDate,
    e.Grade
FROM 
    Enrollments e
JOIN 
    Students s ON e.StudentID = s.StudentID
JOIN 
    Courses c ON e.CourseID = c.CourseID
JOIN 
    Faculty f ON c.FacultyID = f.FacultyID
ORDER BY 
    s.LastName, s.FirstName, c.CourseName;
```
