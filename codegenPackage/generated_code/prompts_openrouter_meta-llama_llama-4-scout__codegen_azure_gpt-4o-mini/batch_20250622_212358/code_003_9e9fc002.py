"""
Generated Code Metadata:
========================
Original URL: https://esofa.edu.pe
Prompt: Design a database schema for storing information about ESOFA students, including their personal details, academic records, and training progress.
Generated: DETERMINISTIC_9e9fc002ccea65e0
Batch ID: 20250622_212358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about ESOFA students

-- Create a table for storing personal details of students
CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,            -- Student's first name
    LastName VARCHAR(50) NOT NULL,             -- Student's last name
    DateOfBirth DATE NOT NULL,                  -- Student's date of birth
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Student's email address (unique)
    PhoneNumber VARCHAR(15),                    -- Student's phone number
    Address VARCHAR(255),                        -- Student's residential address
    EnrollmentDate DATE NOT NULL,                -- Date when the student enrolled
    Status ENUM('Active', 'Inactive', 'Graduated') DEFAULT 'Active'  -- Current status of the student
);

-- Create a table for storing academic records of students
CREATE TABLE AcademicRecords (
    RecordID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each academic record
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    CourseName VARCHAR(100) NOT NULL,           -- Name of the course
    Grade CHAR(2),                              -- Grade received in the course
    Semester ENUM('Fall', 'Spring', 'Summer') NOT NULL,  -- Semester in which the course was taken
    Year INT NOT NULL,                          -- Year in which the course was taken
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table for tracking training progress of students
CREATE TABLE TrainingProgress (
    ProgressID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each training progress record
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    TrainingModule VARCHAR(100) NOT NULL,       -- Name of the training module
    CompletionStatus ENUM('Not Started', 'In Progress', 'Completed') DEFAULT 'Not Started',  -- Status of the training module
    CompletionDate DATE,                         -- Date when the training module was completed
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create an index on the Email column in the Students table for faster lookups
CREATE INDEX idx_email ON Students(Email);

-- Create an index on the StudentID column in the AcademicRecords table for faster lookups
CREATE INDEX idx_student_academic ON AcademicRecords(StudentID);

-- Create an index on the StudentID column in the TrainingProgress table for faster lookups
CREATE INDEX idx_student_training ON TrainingProgress(StudentID);
```
