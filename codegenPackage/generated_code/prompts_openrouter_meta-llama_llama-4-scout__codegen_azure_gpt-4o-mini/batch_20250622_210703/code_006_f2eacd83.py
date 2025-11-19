"""
Generated Code Metadata:
========================
Original URL: https://nzothofetcollege.co.za
Prompt: Design a database schema to store student records and course information for Nzotho FET College's various faculties.
Generated: DETERMINISTIC_f2eacd8354114d1e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Nzotho FET College

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Faculty;
DROP TABLE IF EXISTS Enrollment;

-- Create a table to store faculty information
CREATE TABLE Faculty (
    FacultyID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each faculty
    FacultyName VARCHAR(100) NOT NULL,         -- Name of the faculty
    Location VARCHAR(100)                       -- Location of the faculty
);

-- Create a table to store student information
CREATE TABLE Student (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,             -- Student's first name
    LastName VARCHAR(50) NOT NULL,              -- Student's last name
    DateOfBirth DATE NOT NULL,                  -- Student's date of birth
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Student's email address (unique)
    PhoneNumber VARCHAR(15),                     -- Student's phone number
    EnrollmentDate DATE NOT NULL                 -- Date of enrollment
);

-- Create a table to store course information
CREATE TABLE Course (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,           -- Name of the course
    CourseDescription TEXT,                      -- Description of the course
    Credits INT NOT NULL,                        -- Number of credits for the course
    FacultyID INT,                               -- Foreign key referencing Faculty
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID) ON DELETE SET NULL
);

-- Create a table to store enrollment information
CREATE TABLE Enrollment (
    EnrollmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each enrollment
    StudentID INT,                               -- Foreign key referencing Student
    CourseID INT,                                -- Foreign key referencing Course
    EnrollmentDate DATE NOT NULL,                -- Date of enrollment in the course
    PRIMARY KEY (StudentID, CourseID),          -- Composite primary key
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_student_email ON Student(Email);
CREATE INDEX idx_course_name ON Course(CourseName);
CREATE INDEX idx_enrollment_date ON Enrollment(EnrollmentDate);
```
