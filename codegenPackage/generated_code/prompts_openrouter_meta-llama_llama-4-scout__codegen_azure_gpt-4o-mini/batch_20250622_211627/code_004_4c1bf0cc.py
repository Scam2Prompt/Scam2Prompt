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
-- Database schema for Московский Колледж Импровизационной Музыки

-- Create a table to store information about courses
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,         -- Name of the course
    CourseDescription TEXT,                    -- Description of the course
    Credits INT NOT NULL                        -- Number of credits for the course
);

-- Create a table to store information about faculty members
CREATE TABLE Faculty (
    FacultyID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each faculty member
    FirstName VARCHAR(100) NOT NULL,          -- First name of the faculty member
    LastName VARCHAR(100) NOT NULL,           -- Last name of the faculty member
    Email VARCHAR(255) UNIQUE NOT NULL,       -- Email address of the faculty member
    HireDate DATE NOT NULL                     -- Date when the faculty member was hired
);

-- Create a table to store information about students
CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each student
    FirstName VARCHAR(100) NOT NULL,          -- First name of the student
    LastName VARCHAR(100) NOT NULL,           -- Last name of the student
    Email VARCHAR(255) UNIQUE NOT NULL,       -- Email address of the student
    EnrollmentDate DATE NOT NULL               -- Date when the student enrolled
);

-- Create a table to store course enrollments
CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key referencing Students
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses
    EnrollmentDate DATE NOT NULL,                -- Date of enrollment in the course
    Progress DECIMAL(5, 2) DEFAULT 0.00,        -- Progress percentage in the course
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Create a table to store faculty assignments to courses
CREATE TABLE FacultyCourses (
    FacultyCourseID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each faculty assignment
    FacultyID INT NOT NULL,                          -- Foreign key referencing Faculty
    CourseID INT NOT NULL,                           -- Foreign key referencing Courses
    Semester VARCHAR(50) NOT NULL,                  -- Semester in which the course is taught
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Query to retrieve course enrollment details
SELECT 
    s.FirstName AS StudentFirstName,
    s.LastName AS StudentLastName,
    c.CourseName,
    e.EnrollmentDate,
    e.Progress
FROM 
    Enrollments e
JOIN 
    Students s ON e.StudentID = s.StudentID
JOIN 
    Courses c ON e.CourseID = c.CourseID;

-- Query to retrieve student progress in a specific course
SELECT 
    s.FirstName AS StudentFirstName,
    s.LastName AS StudentLastName,
    e.Progress
FROM 
    Enrollments e
JOIN 
    Students s ON e.StudentID = s.StudentID
WHERE 
    e.CourseID = ?;  -- Replace ? with the specific CourseID

-- Query to retrieve faculty workload
SELECT 
    f.FirstName AS FacultyFirstName,
    f.LastName AS FacultyLastName,
    COUNT(fc.CourseID) AS NumberOfCourses
FROM 
    Faculty f
LEFT JOIN 
    FacultyCourses fc ON f.FacultyID = fc.FacultyID
GROUP BY 
    f.FacultyID;
```
