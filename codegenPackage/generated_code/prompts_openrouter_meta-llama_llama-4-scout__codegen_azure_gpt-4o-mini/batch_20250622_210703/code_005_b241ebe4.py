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
-- Database schema for ENAFO's courses, instructors, and students

-- Create a table for storing information about instructors
CREATE TABLE Instructors (
    InstructorID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each instructor
    FirstName VARCHAR(50) NOT NULL,               -- Instructor's first name
    LastName VARCHAR(50) NOT NULL,                 -- Instructor's last name
    Email VARCHAR(100) UNIQUE NOT NULL,            -- Instructor's email address
    Phone VARCHAR(15)                              -- Instructor's phone number
);

-- Create a table for storing information about students
CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,               -- Student's first name
    LastName VARCHAR(50) NOT NULL,                 -- Student's last name
    Email VARCHAR(100) UNIQUE NOT NULL,            -- Student's email address
    EnrollmentDate DATE NOT NULL                    -- Date when the student enrolled
);

-- Create a table for storing information about courses
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,              -- Name of the course
    Description TEXT,                               -- Description of the course
    StartDate DATE NOT NULL,                       -- Start date of the course
    EndDate DATE NOT NULL,                         -- End date of the course
    InstructorID INT,                              -- Foreign key referencing Instructors
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID) ON DELETE SET NULL
);

-- Create a junction table for the many-to-many relationship between students and courses
CREATE TABLE StudentCourses (
    StudentID INT,                                 -- Foreign key referencing Students
    CourseID INT,                                  -- Foreign key referencing Courses
    PRIMARY KEY (StudentID, CourseID),            -- Composite primary key
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Sample query to demonstrate usage: Retrieve all courses along with their instructors
SELECT 
    c.CourseID,
    c.CourseName,
    c.Description,
    c.StartDate,
    c.EndDate,
    CONCAT(i.FirstName, ' ', i.LastName) AS InstructorName
FROM 
    Courses c
LEFT JOIN 
    Instructors i ON c.InstructorID = i.InstructorID
ORDER BY 
    c.StartDate;
```
