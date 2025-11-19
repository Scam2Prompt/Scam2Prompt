"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Generate a sample database schema for storing information about vocational education and training programs, including courses like the Graduate Diploma of Management (Learning) (BSB80120) and Diploma of Community Services (CHC52021).
Generated: DETERMINISTIC_341ff88c935e4eb9
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about vocational education and training programs

-- Create a table for storing information about programs
CREATE TABLE Programs (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL,        -- Name of the program
    ProgramCode VARCHAR(50) NOT NULL UNIQUE,  -- Unique code for the program (e.g., BSB80120, CHC52021)
    Description TEXT,                         -- Detailed description of the program
    DurationMonths INT NOT NULL,              -- Duration of the program in months
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the program was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the program was last updated
);

-- Create a table for storing information about courses within programs
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each course
    ProgramID INT NOT NULL,                   -- Foreign key linking to the Programs table
    CourseName VARCHAR(255) NOT NULL,         -- Name of the course
    CourseCode VARCHAR(50) NOT NULL UNIQUE,   -- Unique code for the course
    Description TEXT,                         -- Detailed description of the course
    HoursRequired INT NOT NULL,               -- Number of hours required to complete the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the course was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the course was last updated
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for storing information about students enrolled in programs
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(100) NOT NULL,          -- First name of the student
    LastName VARCHAR(100) NOT NULL,           -- Last name of the student
    Email VARCHAR(255) NOT NULL UNIQUE,       -- Email address of the student
    PhoneNumber VARCHAR(20),                  -- Contact number of the student
    DateOfBirth DATE NOT NULL,                -- Date of birth of the student
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the student record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the student record was last updated
);

-- Create a table for storing enrollment information
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key linking to the Students table
    ProgramID INT NOT NULL,                      -- Foreign key linking to the Programs table
    EnrollmentDate DATE NOT NULL,                -- Date of enrollment
    CompletionDate DATE,                         -- Date of completion (nullable if not completed yet)
    Status ENUM('Enrolled', 'Completed', 'Withdrawn') NOT NULL DEFAULT 'Enrolled', -- Status of the enrollment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the enrollment record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the enrollment record was last updated
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for storing course completion records
CREATE TABLE CourseCompletions (
    CompletionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course completion record
    EnrollmentID INT NOT NULL,                   -- Foreign key linking to the Enrollments table
    CourseID INT NOT NULL,                       -- Foreign key linking to the Courses table
    CompletionDate DATE NOT NULL,                -- Date of course completion
    Grade VARCHAR(10),                           -- Grade achieved in the course (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the completion record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the completion record was last updated
    FOREIGN KEY (EnrollmentID) REFERENCES Enrollments(EnrollmentID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_program_name ON Programs(ProgramName);
CREATE INDEX idx_course_name ON Courses(CourseName);
CREATE INDEX idx_student_name ON Students(LastName, FirstName);
CREATE INDEX idx_enrollment_status ON Enrollments(Status);
```
