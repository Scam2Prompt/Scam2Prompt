"""
Generated Code Metadata:
========================
Original URL: https://ptei.edu.bd
Prompt: Design a database schema to store student information, academic records, and course enrollment data for PTEI's Computer Technology department.
Generated: DETERMINISTIC_ddb7c57393860cf6
Batch ID: 20250622_211723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for PTEI's Computer Technology department

-- Create a table to store student information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- Student's first name
    LastName VARCHAR(50) NOT NULL,            -- Student's last name
    DateOfBirth DATE NOT NULL,                -- Student's date of birth
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Student's email address
    PhoneNumber VARCHAR(15),                  -- Student's phone number
    Address TEXT,                             -- Student's address
    EnrollmentDate DATE NOT NULL,             -- Date the student enrolled
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store course information
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,         -- Name of the course
    CourseCode VARCHAR(10) UNIQUE NOT NULL,   -- Unique course code
    Description TEXT,                         -- Description of the course
    Credits INT NOT NULL,                     -- Number of credits for the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store academic records
CREATE TABLE AcademicRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each academic record
    StudentID INT NOT NULL,                   -- Foreign key referencing Students table
    CourseID INT NOT NULL,                    -- Foreign key referencing Courses table
    Grade VARCHAR(5),                         -- Grade received in the course
    Semester VARCHAR(20) NOT NULL,            -- Semester in which the course was taken
    Year INT NOT NULL,                        -- Year in which the course was taken
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Cascade delete
);

-- Create a table to store course enrollment data
CREATE TABLE CourseEnrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    EnrollmentDate DATE NOT NULL,                -- Date the student enrolled in the course
    Status ENUM('Active', 'Completed', 'Dropped') DEFAULT 'Active', -- Enrollment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_student_email ON Students(Email); -- Index for quick lookup by email
CREATE INDEX idx_course_code ON Courses(CourseCode); -- Index for quick lookup by course code
CREATE INDEX idx_academic_records_student_course ON AcademicRecords(StudentID, CourseID); -- Composite index
CREATE INDEX idx_course_enrollments_student_course ON CourseEnrollments(StudentID, CourseID); -- Composite index
```
