"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Create a database schema for managing student records, faculty information, and course schedules for an institution like Trentino.
Generated: DETERMINISTIC_58d583d79153bcdf
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Student Records, Faculty Information, and Course Schedules

-- Create a table to store student records
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- Student's first name
    LastName VARCHAR(50) NOT NULL,            -- Student's last name
    DateOfBirth DATE,                         -- Date of birth of the student
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Student's email address
    PhoneNumber VARCHAR(15),                  -- Contact number of the student
    EnrollmentDate DATE NOT NULL,             -- Date when the student enrolled
    Status ENUM('Active', 'Inactive') DEFAULT 'Active' -- Current status of the student
);

-- Create a table to store faculty information
CREATE TABLE Faculty (
    FacultyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each faculty member
    FirstName VARCHAR(50) NOT NULL,           -- Faculty's first name
    LastName VARCHAR(50) NOT NULL,            -- Faculty's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Faculty's email address
    PhoneNumber VARCHAR(15),                  -- Contact number of the faculty
    HireDate DATE NOT NULL,                   -- Date when the faculty member was hired
    Department VARCHAR(100) NOT NULL          -- Department the faculty belongs to
);

-- Create a table to store course information
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,        -- Name of the course
    CourseCode VARCHAR(10) UNIQUE NOT NULL,  -- Unique code for the course
    Credits INT NOT NULL,                    -- Number of credits for the course
    Department VARCHAR(100) NOT NULL         -- Department offering the course
);

-- Create a table to store course schedules
CREATE TABLE CourseSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each schedule
    CourseID INT NOT NULL,                      -- Foreign key referencing Courses table
    FacultyID INT NOT NULL,                     -- Foreign key referencing Faculty table
    Semester ENUM('Spring', 'Summer', 'Fall') NOT NULL, -- Semester when the course is offered
    Year INT NOT NULL,                          -- Year when the course is offered
    DaysOfWeek VARCHAR(50) NOT NULL,            -- Days of the week the course is held (e.g., "Monday, Wednesday")
    StartTime TIME NOT NULL,                    -- Start time of the course
    EndTime TIME NOT NULL,                      -- End time of the course
    Classroom VARCHAR(50) NOT NULL,             -- Classroom where the course is held
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE,
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID) ON DELETE SET NULL
);

-- Create a table to store student enrollments in courses
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    Semester ENUM('Spring', 'Summer', 'Fall') NOT NULL, -- Semester of the enrollment
    Year INT NOT NULL,                           -- Year of the enrollment
    Grade CHAR(1),                               -- Grade earned by the student (e.g., 'A', 'B', etc.)
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_student_email ON Students(Email);
CREATE INDEX idx_faculty_email ON Faculty(Email);
CREATE INDEX idx_course_code ON Courses(CourseCode);
CREATE INDEX idx_enrollment_student_course ON Enrollments(StudentID, CourseID);
```
