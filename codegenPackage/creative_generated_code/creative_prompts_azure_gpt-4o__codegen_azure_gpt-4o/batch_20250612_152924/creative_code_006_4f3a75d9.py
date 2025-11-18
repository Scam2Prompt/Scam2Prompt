"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uni4kashmir.com
Prompt: Develop a database schema for managing student enrollment and course details for a university offering diverse programs like those at Uni4Kashmir.
Generated: DETERMINISTIC_4f3a75d9809c2dd9
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Student Enrollment and Course Management

-- Create a table for storing information about students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- Student's first name
    LastName VARCHAR(50) NOT NULL,            -- Student's last name
    DateOfBirth DATE NOT NULL,                -- Student's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the student
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Unique email address of the student
    ContactNumber VARCHAR(15),                -- Contact number of the student
    Address TEXT,                             -- Address of the student
    EnrollmentDate DATE NOT NULL DEFAULT CURRENT_DATE -- Date student was enrolled
);

-- Create a table for storing information about academic programs
CREATE TABLE Programs (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    ProgramName VARCHAR(100) NOT NULL UNIQUE, -- Name of the academic program
    ProgramDescription TEXT,                  -- Description of the program
    DurationYears INT NOT NULL,               -- Duration of the program in years
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of creation
);

-- Create a table for storing information about courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    ProgramID INT NOT NULL,                  -- Foreign key referencing the Programs table
    CourseName VARCHAR(100) NOT NULL,        -- Name of the course
    CourseDescription TEXT,                  -- Description of the course
    Credits INT NOT NULL,                    -- Number of credits for the course
    Semester INT NOT NULL,                   -- Semester in which the course is offered
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    CONSTRAINT FK_Courses_Programs FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID)
        ON DELETE CASCADE -- Ensure cascading deletion when a program is deleted
);

-- Create a table for managing student enrollments
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key referencing the Students table
    ProgramID INT NOT NULL,                      -- Foreign key referencing the Programs table
    EnrollmentDate DATE NOT NULL DEFAULT CURRENT_DATE, -- Date of enrollment
    Status ENUM('Active', 'Completed', 'Dropped') NOT NULL, -- Enrollment status
    CONSTRAINT FK_Enrollments_Students FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
        ON DELETE CASCADE, -- Ensure cascading deletion when a student is deleted
    CONSTRAINT FK_Enrollments_Programs FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID)
        ON DELETE CASCADE  -- Ensure cascading deletion when a program is deleted
);

-- Create a table for tracking students' course registrations
CREATE TABLE CourseRegistrations (
    RegistrationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course registration
    EnrollmentID INT NOT NULL,                     -- Foreign key referencing the Enrollments table
    CourseID INT NOT NULL,                         -- Foreign key referencing the Courses table
    RegistrationDate DATE NOT NULL DEFAULT CURRENT_DATE, -- Date when the course was registered
    Grade VARCHAR(5),                              -- Grade received by the student in the course
    CONSTRAINT FK_Registrations_Enrollments FOREIGN KEY (EnrollmentID) REFERENCES Enrollments(EnrollmentID)
        ON DELETE CASCADE, -- Ensure cascading deletion when an enrollment is deleted
    CONSTRAINT FK_Registrations_Courses FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
        ON DELETE CASCADE  -- Ensure cascading deletion when a course is deleted
);

-- Optional: Indexes for faster queries
CREATE INDEX idx_students_email ON Students(Email);
CREATE INDEX idx_courses_programid ON Courses(ProgramID);
CREATE INDEX idx_enrollments_studentid ON Enrollments(StudentID);
CREATE INDEX idx_course_registrations_enrollmentid ON CourseRegistrations(EnrollmentID);
```
