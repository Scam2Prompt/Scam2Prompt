"""
Generated Code Metadata:
========================
Original URL: https://cnu.university
Prompt: "Design a database schema to store information about students, courses, and programs at an online university like CNU."
Generated: DETERMINISTIC_bcbdbf25ccc9143a
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online university system

-- Table to store information about students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- First name of the student
    LastName VARCHAR(50) NOT NULL,            -- Last name of the student
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Email address of the student
    DateOfBirth DATE NOT NULL,                -- Date of birth of the student
    EnrollmentDate DATE NOT NULL,             -- Date the student enrolled
    ProgramID INT,                            -- Foreign key to the Programs table
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE SET NULL
);

-- Table to store information about programs
CREATE TABLE Programs (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    ProgramName VARCHAR(100) NOT NULL,        -- Name of the program
    Description TEXT,                         -- Description of the program
    DurationYears INT NOT NULL,               -- Duration of the program in years
    TuitionFee DECIMAL(10, 2) NOT NULL        -- Tuition fee for the program
);

-- Table to store information about courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,         -- Name of the course
    Description TEXT,                         -- Description of the course
    Credits INT NOT NULL,                     -- Number of credits for the course
    ProgramID INT,                            -- Foreign key to the Programs table
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE
);

-- Table to store the relationship between students and courses (enrollments)
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key to the Students table
    CourseID INT NOT NULL,                       -- Foreign key to the Courses table
    EnrollmentDate DATE NOT NULL,                -- Date the student enrolled in the course
    Grade VARCHAR(5),                            -- Grade received by the student (optional)
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_student_email ON Students(Email); -- Index for quick lookup by email
CREATE INDEX idx_program_name ON Programs(ProgramName); -- Index for quick lookup by program name
CREATE INDEX idx_course_name ON Courses(CourseName); -- Index for quick lookup by course name
CREATE INDEX idx_enrollment_student_course ON Enrollments(StudentID, CourseID); -- Composite index for enrollments
```
