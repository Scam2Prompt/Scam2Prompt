"""
Generated Code Metadata:
========================
Original URL: https://enafo.cl
Prompt: "Design a database schema for storing information about ENAFO's courses, instructors, and students, and write a simple query to demonstrate its usage."
Generated: DETERMINISTIC_b241ebe40a3922f4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for ENAFO's Courses, Instructors, and Students

-- Table: Instructors
CREATE TABLE Instructors (
    InstructorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each instructor
    FirstName VARCHAR(50) NOT NULL,              -- Instructor's first name
    LastName VARCHAR(50) NOT NULL,               -- Instructor's last name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Instructor's email address
    HireDate DATE NOT NULL                       -- Date the instructor was hired
);

-- Table: Courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,            -- Name of the course
    Description TEXT,                            -- Description of the course
    StartDate DATE NOT NULL,                     -- Start date of the course
    EndDate DATE NOT NULL,                       -- End date of the course
    InstructorID INT NOT NULL,                   -- Foreign key referencing the instructor teaching the course
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID) ON DELETE CASCADE
);

-- Table: Students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,              -- Student's first name
    LastName VARCHAR(50) NOT NULL,               -- Student's last name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Student's email address
    EnrollmentDate DATE NOT NULL                 -- Date the student enrolled
);

-- Table: Enrollments
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key referencing the student
    CourseID INT NOT NULL,                       -- Foreign key referencing the course
    EnrollmentDate DATE NOT NULL,                -- Date the student enrolled in the course
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Example Query: Retrieve all students enrolled in a specific course along with the instructor's name
SELECT 
    Students.FirstName AS StudentFirstName,
    Students.LastName AS StudentLastName,
    Courses.CourseName,
    Instructors.FirstName AS InstructorFirstName,
    Instructors.LastName AS InstructorLastName
FROM 
    Enrollments
JOIN 
    Students ON Enrollments.StudentID = Students.StudentID
JOIN 
    Courses ON Enrollments.CourseID = Courses.CourseID
JOIN 
    Instructors ON Courses.InstructorID = Instructors.InstructorID
WHERE 
    Courses.CourseName = 'Introduction to Programming'; -- Replace with the desired course name
```
