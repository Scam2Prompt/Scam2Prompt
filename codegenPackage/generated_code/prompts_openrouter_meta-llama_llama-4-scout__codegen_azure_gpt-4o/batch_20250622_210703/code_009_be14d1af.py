"""
Generated Code Metadata:
========================
Original URL: https://www.ahs.edu.np
Prompt: Design a database schema to store information about students, faculty, and courses at Ace Higher Secondary School.
Generated: DETERMINISTIC_be14d1af75245a6b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Ace Higher Secondary School

-- Create a table to store information about students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- First name of the student
    LastName VARCHAR(50) NOT NULL,            -- Last name of the student
    DateOfBirth DATE NOT NULL,                -- Date of birth of the student
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the student
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Email address of the student
    PhoneNumber VARCHAR(15),                  -- Contact number of the student
    Address TEXT,                             -- Address of the student
    EnrollmentDate DATE NOT NULL              -- Date the student enrolled
);

-- Create a table to store information about faculty members
CREATE TABLE Faculty (
    FacultyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each faculty member
    FirstName VARCHAR(50) NOT NULL,           -- First name of the faculty member
    LastName VARCHAR(50) NOT NULL,            -- Last name of the faculty member
    DateOfBirth DATE NOT NULL,                -- Date of birth of the faculty member
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the faculty member
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Email address of the faculty member
    PhoneNumber VARCHAR(15),                  -- Contact number of the faculty member
    Address TEXT,                             -- Address of the faculty member
    HireDate DATE NOT NULL,                   -- Date the faculty member was hired
    Department VARCHAR(100) NOT NULL          -- Department the faculty member belongs to
);

-- Create a table to store information about courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,         -- Name of the course
    CourseCode VARCHAR(10) UNIQUE NOT NULL,   -- Unique code for the course
    Description TEXT,                         -- Description of the course
    Credits INT NOT NULL,                     -- Number of credits for the course
    Department VARCHAR(100) NOT NULL          -- Department offering the course
);

-- Create a table to store the relationship between students and courses (enrollments)
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    EnrollmentDate DATE NOT NULL,                -- Date the student enrolled in the course
    Grade VARCHAR(2),                            -- Grade the student received in the course
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Create a table to store the relationship between faculty and courses (teaching assignments)
CREATE TABLE TeachingAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    FacultyID INT NOT NULL,                      -- Foreign key referencing Faculty table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    AssignmentDate DATE NOT NULL,                -- Date the faculty was assigned to the course
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Indexes for optimization
CREATE INDEX idx_students_email ON Students(Email);
CREATE INDEX idx_faculty_email ON Faculty(Email);
CREATE INDEX idx_courses_code ON Courses(CourseCode);
```
