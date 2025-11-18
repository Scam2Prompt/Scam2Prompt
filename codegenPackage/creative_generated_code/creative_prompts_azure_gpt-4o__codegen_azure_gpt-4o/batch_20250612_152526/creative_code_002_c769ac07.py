"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Create a database schema in SQL to organize data for an educational institution, including tables for student records, teacher assignments, institutional achievements, and administrative processes, inspired by the structure of the Politécnico Municipal de Cali.
Generated: DETERMINISTIC_c769ac07c51818fa
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for an educational institution

-- Create a table for Students
CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- First name of the student
    LastName VARCHAR(50) NOT NULL,            -- Last name of the student
    DateOfBirth DATE NOT NULL,                -- Date of birth of the student
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the student
    Address VARCHAR(255),                     -- Address of the student
    PhoneNumber VARCHAR(15),                  -- Contact number of the student
    Email VARCHAR(100) UNIQUE,                -- Email of the student
    EnrollmentDate DATE NOT NULL,             -- Date when the student enrolled
    GradeLevel INT NOT NULL                   -- Current grade level of the student
);

-- Create a table for Teachers
CREATE TABLE Teachers (
    TeacherID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each teacher
    FirstName VARCHAR(50) NOT NULL,           -- First name of the teacher
    LastName VARCHAR(50) NOT NULL,            -- Last name of the teacher
    DateOfBirth DATE NOT NULL,                -- Date of birth of the teacher
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the teacher
    Address VARCHAR(255),                     -- Address of the teacher
    PhoneNumber VARCHAR(15),                  -- Contact number of the teacher
    Email VARCHAR(100) UNIQUE,                -- Email of the teacher
    HireDate DATE NOT NULL,                   -- Date when the teacher was hired
    Department VARCHAR(100) NOT NULL,         -- Department the teacher belongs to
    Specialization VARCHAR(100)               -- Teacher's area of expertise
);

-- Create a table for Courses
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,        -- Name of the course
    Credits INT NOT NULL,                    -- Credit hours for the course
    Department VARCHAR(100) NOT NULL,        -- Department offering the course
    TeacherID INT NOT NULL,                  -- Teacher responsible for the course
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID) -- Foreign key referencing Teachers table
);

-- Create a table for Enrollments (linking Students to Courses)
CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                     -- Student enrolled in the course
    CourseID INT NOT NULL,                      -- Course the student is enrolled in
    EnrollmentDate DATE NOT NULL,               -- Date of enrollment
    Grade DECIMAL(5, 2),                        -- Grade achieved in the course
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID), -- Foreign key referencing Students table
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)     -- Foreign key referencing Courses table
);

-- Create a table for Achievements (awards and institutional recognitions)
CREATE TABLE Achievements (
    AchievementID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each achievement
    Title VARCHAR(100) NOT NULL,                  -- Title of the achievement
    Description TEXT,                             -- Detailed description of the achievement
    AwardDate DATE NOT NULL,                      -- Date the achievement was awarded
    RecipientType ENUM('Student', 'Teacher', 'Institution') NOT NULL, -- Type of recipient
    RecipientID INT,                              -- ID of the recipient (can be NULL for Institution)
    FOREIGN KEY (RecipientID) REFERENCES Students(StudentID) ON DELETE SET NULL, -- Student recipient (if applicable)
    FOREIGN KEY (RecipientID) REFERENCES Teachers(TeacherID) ON DELETE SET NULL  -- Teacher recipient (if applicable)
);

-- Create a table for Administrative Processes (e.g., events, budgets)
CREATE TABLE AdministrativeProcesses (
    ProcessID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each process
    ProcessName VARCHAR(100) NOT NULL,        -- Name of the administrative process
    Description TEXT,                         -- Detailed description of the process
    StartDate DATE NOT NULL,                  -- Start date of the process
    EndDate DATE,                             -- End date of the process (nullable if ongoing)
    Budget DECIMAL(10, 2),                    -- Budget allocated for the process
    Status ENUM('Planned', 'Ongoing', 'Completed') NOT NULL -- Current status of the process
);

-- Ensure that the schema is production-ready and scalable.
-- Use appropriate data types, constraints, and relationships.
```
