"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kigaliinstitute.rw
Prompt: Create a database schema for tracking student progress in short-term brokerage courses, inspired by Kigali Institute's balance of theoretical and practical training.
Generated: DETERMINISTIC_1e490ff1da6a216d
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking student progress in short-term brokerage courses

-- Drop existing tables to prevent conflicts during development
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Enrollment;
DROP TABLE IF EXISTS Assessment;

-- Table to store course information
CREATE TABLE Course (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,
    CourseName VARCHAR(100) NOT NULL,
    Description TEXT,
    TheoreticalHours INT NOT NULL CHECK (TheoreticalHours >= 0),
    PracticalHours INT NOT NULL CHECK (PracticalHours >= 0),
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store student information
CREATE TABLE Student (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(15),
    EnrollmentDate DATE NOT NULL DEFAULT CURRENT_DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Join table for students enrolled in courses
CREATE TABLE Enrollment (
    EnrollmentID INT PRIMARY KEY AUTO_INCREMENT,
    StudentID INT NOT NULL,
    CourseID INT NOT NULL,
    EnrollmentDate DATE NOT NULL DEFAULT CURRENT_DATE,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID) ON DELETE CASCADE,
    UNIQUE (StudentID, CourseID)  -- Ensure a student can enroll in the same course only once
);

-- Table to track student assessments
CREATE TABLE Assessment (
    AssessmentID INT PRIMARY KEY AUTO_INCREMENT,
    EnrollmentID INT NOT NULL,
    AssessmentDate DATE NOT NULL,
    Score DECIMAL(5, 2) CHECK (Score >= 0 AND Score <= 100),  -- Score must be between 0 and 100
    Comments TEXT,
    FOREIGN KEY (EnrollmentID) REFERENCES Enrollment(EnrollmentID) ON DELETE CASCADE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Sample index for faster querying
CREATE INDEX idx_student_email ON Student(Email);
CREATE INDEX idx_course_name ON Course(CourseName);
CREATE INDEX idx_enrollment_course ON Enrollment(CourseID);
CREATE INDEX idx_assessment_date ON Assessment(AssessmentDate);
```
