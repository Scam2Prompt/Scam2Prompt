"""
Generated Code Metadata:
========================
Original URL: https://ikogwelimited.com
Prompt: Generate a sample database schema for an IELTS training center like Ikogwe International Limited, including tables for student information, course enrollment, and exam results.
Generated: DETERMINISTIC_9f73247ab54013fd
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for an IELTS Training Center

-- Create a table for storing student information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- Student's first name
    LastName VARCHAR(50) NOT NULL,            -- Student's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Student's email address (must be unique)
    PhoneNumber VARCHAR(15),                  -- Student's phone number
    DateOfBirth DATE,                         -- Student's date of birth
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of registration
    Address TEXT                              -- Student's address
);

-- Create a table for storing course information
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,         -- Name of the course
    Description TEXT,                         -- Description of the course
    DurationWeeks INT NOT NULL,               -- Duration of the course in weeks
    Fee DECIMAL(10, 2) NOT NULL               -- Fee for the course
);

-- Create a table for storing course enrollment information
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of enrollment
    Status ENUM('Active', 'Completed', 'Cancelled') DEFAULT 'Active', -- Enrollment status
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE     -- Cascade delete
);

-- Create a table for storing exam results
CREATE TABLE ExamResults (
    ResultID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each exam result
    StudentID INT NOT NULL,                    -- Foreign key referencing Students table
    CourseID INT NOT NULL,                     -- Foreign key referencing Courses table
    ExamDate DATE NOT NULL,                    -- Date of the exam
    ListeningScore DECIMAL(4, 1) NOT NULL,     -- Listening score (e.g., 7.5)
    ReadingScore DECIMAL(4, 1) NOT NULL,       -- Reading score (e.g., 8.0)
    WritingScore DECIMAL(4, 1) NOT NULL,       -- Writing score (e.g., 6.5)
    SpeakingScore DECIMAL(4, 1) NOT NULL,      -- Speaking score (e.g., 7.0)
    OverallScore DECIMAL(4, 1) NOT NULL,       -- Overall score (e.g., 7.5)
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE     -- Cascade delete
);

-- Optional: Create indexes for faster queries
CREATE INDEX idx_student_email ON Students(Email); -- Index for quick lookup by email
CREATE INDEX idx_course_name ON Courses(CourseName); -- Index for quick lookup by course name
CREATE INDEX idx_enrollment_status ON Enrollments(Status); -- Index for quick lookup by enrollment status
```
