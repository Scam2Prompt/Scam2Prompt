"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: "Design a simple database schema to store information about students, instructors, and courses for a school offering programs in hospitality management and culinary arts."
Generated: DETERMINISTIC_0ae0402b92416027
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for a School Offering Programs in Hospitality Management and Culinary Arts

-- Table to store information about students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- First name of the student
    LastName VARCHAR(50) NOT NULL,            -- Last name of the student
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Email address of the student
    PhoneNumber VARCHAR(15),                  -- Contact number of the student
    EnrollmentDate DATE NOT NULL,             -- Date the student enrolled
    Program VARCHAR(50) NOT NULL,             -- Program the student is enrolled in (e.g., Hospitality Management, Culinary Arts)
    DateOfBirth DATE,                         -- Date of birth of the student
    Gender ENUM('Male', 'Female', 'Other')    -- Gender of the student
);

-- Table to store information about instructors
CREATE TABLE Instructors (
    InstructorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each instructor
    FirstName VARCHAR(50) NOT NULL,              -- First name of the instructor
    LastName VARCHAR(50) NOT NULL,               -- Last name of the instructor
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Email address of the instructor
    PhoneNumber VARCHAR(15),                     -- Contact number of the instructor
    HireDate DATE NOT NULL,                      -- Date the instructor was hired
    Department VARCHAR(50) NOT NULL              -- Department the instructor belongs to (e.g., Hospitality, Culinary Arts)
);

-- Table to store information about courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,        -- Name of the course
    Description TEXT,                        -- Description of the course
    Credits INT NOT NULL,                    -- Number of credits for the course
    Department VARCHAR(50) NOT NULL          -- Department offering the course (e.g., Hospitality, Culinary Arts)
);

-- Table to store the relationship between students and courses (enrollments)
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    EnrollmentDate DATE NOT NULL,                -- Date the student enrolled in the course
    Grade CHAR(2),                               -- Grade the student received in the course
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Table to store the relationship between instructors and courses (teaching assignments)
CREATE TABLE TeachingAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each teaching assignment
    InstructorID INT NOT NULL,                   -- Foreign key referencing Instructors table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    AssignmentDate DATE NOT NULL,                -- Date the instructor was assigned to the course
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_student_program ON Students(Program);
CREATE INDEX idx_instructor_department ON Instructors(Department);
CREATE INDEX idx_course_department ON Courses(Department);
```
