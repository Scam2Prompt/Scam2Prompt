"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicbear.com.br
Prompt: Create a database schema for tracking student progress in a bilingual program, referencing the educational model of Magic Bear Canadian School.
Generated: DETERMINISTIC_b614263dd4b241cc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking student progress in a bilingual program
-- Inspired by the educational model of Magic Bear Canadian School

-- Create the main database
CREATE DATABASE MagicBearBilingual;

-- Use the newly created database
USE MagicBearBilingual;

-- Create a table for storing student information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,                -- First name of the student
    LastName VARCHAR(50) NOT NULL,                 -- Last name of the student
    DateOfBirth DATE NOT NULL,                     -- Birthdate of the student
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the student
    EnrollmentDate DATE NOT NULL,                  -- Date the student enrolled in the program
    BilingualLevel ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL, -- Current level in the bilingual program
    IsActive BOOLEAN DEFAULT TRUE                  -- Indicates if the student is currently active
);

-- Create a table for storing teacher information
CREATE TABLE Teachers (
    TeacherID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each teacher
    FirstName VARCHAR(50) NOT NULL,                -- First name of the teacher
    LastName VARCHAR(50) NOT NULL,                 -- Last name of the teacher
    HireDate DATE NOT NULL,                        -- Date the teacher was hired
    Specialization VARCHAR(50) NOT NULL,           -- Specialization of the teacher (e.g., French, English)
    IsActive BOOLEAN DEFAULT TRUE                  -- Indicates if the teacher is currently active
);

-- Create a table for storing course information
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,             -- Name of the course
    Language ENUM('English', 'French') NOT NULL,  -- Language of instruction
    Level ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL, -- Level of the course
    TeacherID INT NOT NULL,                       -- Reference to the teacher teaching the course
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID) ON DELETE CASCADE
);

-- Create a table for storing student progress in courses
CREATE TABLE StudentProgress (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for progress records
    StudentID INT NOT NULL,                        -- Reference to the student
    CourseID INT NOT NULL,                         -- Reference to the course
    CompletionStatus ENUM('Not Started', 'In Progress', 'Completed') NOT NULL, -- Status of the course
    Grade DECIMAL(5, 2),                           -- Grade achieved by the student (optional)
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,-- Last updated record timestamp
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Create a table for tracking attendance
CREATE TABLE Attendance (
    AttendanceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for attendance records
    StudentID INT NOT NULL,                        -- Reference to the student
    CourseID INT NOT NULL,                         -- Reference to the course
    AttendanceDate DATE NOT NULL,                  -- Date of attendance
    Status ENUM('Present', 'Absent', 'Excused') NOT NULL, -- Attendance status
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Create a table for storing bilingual assessment results
CREATE TABLE Assessments (
    AssessmentID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for assessment records
    StudentID INT NOT NULL,                        -- Reference to the student
    AssessmentDate DATE NOT NULL,                  -- Date of the assessment
    Language ENUM('English', 'French') NOT NULL,   -- Language being assessed
    Score DECIMAL(5, 2) NOT NULL,                  -- Assessment score (e.g., out of 100)
    Feedback TEXT,                                 -- Additional feedback for the student
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE
);

-- Ensure best practices with optimized indexing for commonly queried fields
CREATE INDEX idx_student_courses ON StudentProgress(StudentID, CourseID);
CREATE INDEX idx_attendance_date ON Attendance(StudentID, AttendanceDate);

-- End of database schema
```
