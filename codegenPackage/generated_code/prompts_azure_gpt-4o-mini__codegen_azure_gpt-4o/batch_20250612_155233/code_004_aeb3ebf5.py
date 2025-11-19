"""
Generated Code Metadata:
========================
Original URL: https://welwitschia-aviation.com
Prompt: Design a database schema for managing student enrollments in aviation security training courses, specifically for Welwitschia Aviation's offerings.
Generated: DETERMINISTIC_aeb3ebf55758e4ef
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing student enrollments in aviation security training courses
-- Welwitschia Aviation's offerings

-- Table to store information about students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- First name of the student
    LastName VARCHAR(50) NOT NULL,            -- Last name of the student
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Email address of the student (must be unique)
    PhoneNumber VARCHAR(15),                  -- Contact number of the student
    DateOfBirth DATE,                         -- Date of birth of the student
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,         -- Name of the course
    Description TEXT,                         -- Detailed description of the course
    DurationInDays INT NOT NULL,              -- Duration of the course in days
    StartDate DATE NOT NULL,                  -- Start date of the course
    EndDate DATE NOT NULL,                    -- End date of the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store enrollment information
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of enrollment
    Status ENUM('Pending', 'Active', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Enrollment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Cascade delete for student
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Cascade delete for course
);

-- Table to store instructors for courses
CREATE TABLE Instructors (
    InstructorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each instructor
    FirstName VARCHAR(50) NOT NULL,              -- First name of the instructor
    LastName VARCHAR(50) NOT NULL,               -- Last name of the instructor
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Email address of the instructor (must be unique)
    PhoneNumber VARCHAR(15),                     -- Contact number of the instructor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to associate instructors with courses
CREATE TABLE CourseInstructors (
    CourseInstructorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each association
    CourseID INT NOT NULL,                             -- Foreign key referencing Courses table
    InstructorID INT NOT NULL,                         -- Foreign key referencing Instructors table
    AssignedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time the instructor was assigned
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE, -- Cascade delete for course
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID) ON DELETE CASCADE -- Cascade delete for instructor
);

-- Indexes for optimizing queries
CREATE INDEX idx_student_email ON Students(Email); -- Index for quick lookup of students by email
CREATE INDEX idx_course_name ON Courses(CourseName); -- Index for quick lookup of courses by name
CREATE INDEX idx_enrollment_status ON Enrollments(Status); -- Index for filtering enrollments by status
CREATE INDEX idx_instructor_email ON Instructors(Email); -- Index for quick lookup of instructors by email
```
