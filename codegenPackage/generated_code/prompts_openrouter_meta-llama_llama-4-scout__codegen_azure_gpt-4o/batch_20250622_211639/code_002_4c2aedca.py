"""
Generated Code Metadata:
========================
Original URL: https://gksschool.edu.bd
Prompt: Generate a sample database schema for storing student information, attendance records, and exam results for a school with a similar setup to জি. কে. মাধ্যমিক বিদ্যালয়.
Generated: DETERMINISTIC_4c2aedcaf8646aca
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing student information, attendance records, and exam results

-- Create a database for the school
CREATE DATABASE SchoolDB;

-- Use the created database
USE SchoolDB;

-- Table for storing student information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- First name of the student
    LastName VARCHAR(50) NOT NULL,            -- Last name of the student
    DateOfBirth DATE NOT NULL,                -- Date of birth of the student
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the student
    Address TEXT,                             -- Address of the student
    ContactNumber VARCHAR(15),                -- Contact number of the student
    Email VARCHAR(100),                       -- Email address of the student
    EnrollmentDate DATE NOT NULL              -- Date the student enrolled in the school
);

-- Table for storing attendance records
CREATE TABLE Attendance (
    AttendanceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attendance record
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    AttendanceDate DATE NOT NULL,                -- Date of attendance
    Status ENUM('Present', 'Absent', 'Late') NOT NULL, -- Attendance status
    Remarks TEXT,                                -- Additional remarks (optional)
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) -- Establish relationship with Students table
);

-- Table for storing exam results
CREATE TABLE ExamResults (
    ResultID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each exam result
    StudentID INT NOT NULL,                     -- Foreign key referencing Students table
    ExamName VARCHAR(100) NOT NULL,             -- Name of the exam
    Subject VARCHAR(50) NOT NULL,               -- Subject of the exam
    MarksObtained DECIMAL(5,2) NOT NULL,        -- Marks obtained by the student
    TotalMarks DECIMAL(5,2) NOT NULL,           -- Total marks for the exam
    ExamDate DATE NOT NULL,                     -- Date of the exam
    Grade VARCHAR(10),                          -- Grade achieved (optional)
    Remarks TEXT,                               -- Additional remarks (optional)
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) -- Establish relationship with Students table
);

-- Indexes for optimizing queries
CREATE INDEX idx_student_name ON Students (FirstName, LastName); -- Index for student name
CREATE INDEX idx_attendance_date ON Attendance (AttendanceDate); -- Index for attendance date
CREATE INDEX idx_exam_date ON ExamResults (ExamDate);            -- Index for exam date

-- Error handling: Ensure foreign key constraints are enforced
SET FOREIGN_KEY_CHECKS = 1;

-- The schema is now ready for production use.
```
