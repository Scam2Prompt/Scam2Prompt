"""
Generated Code Metadata:
========================
Original URL: https://retinabd.org
Prompt: Generate a sample database schema for storing information about medical and dental admission courses, including course names, descriptions, and student enrollment data, based on the course offerings of Retina.
Generated: DETERMINISTIC_2479a7b09b654e9f
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about medical and dental admission courses
-- and student enrollment data.

-- Create a table to store course information
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,        -- Name of the course
    Description TEXT,                        -- Detailed description of the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the course was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the course was last updated
);

-- Create a table to store student information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(100) NOT NULL,          -- First name of the student
    LastName VARCHAR(100) NOT NULL,           -- Last name of the student
    Email VARCHAR(255) UNIQUE NOT NULL,       -- Email address of the student (must be unique)
    PhoneNumber VARCHAR(15),                  -- Contact number of the student
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the student record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the student record was last updated
);

-- Create a table to store enrollment information
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment record
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    EnrollmentDate DATE NOT NULL,                -- Date when the student enrolled in the course
    Status ENUM('Active', 'Completed', 'Dropped') DEFAULT 'Active', -- Status of the enrollment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the enrollment record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the enrollment record was last updated
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Cascade delete if student is removed
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Cascade delete if course is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_course_name ON Courses(CourseName); -- Index for faster search by course name
CREATE INDEX idx_student_email ON Students(Email);   -- Index for faster search by student email
CREATE INDEX idx_enrollment_status ON Enrollments(Status); -- Index for faster filtering by enrollment status
```
