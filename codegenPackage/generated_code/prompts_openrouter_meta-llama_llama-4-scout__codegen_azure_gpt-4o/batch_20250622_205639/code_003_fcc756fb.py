"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Design a database schema to store information about students, courses (IELTS, PTE, Spoken English), and study abroad programs (e.g., USA, UK, Canada, Australia, Singapore) for a platform like Red & White International.
Generated: DETERMINISTIC_fcc756fb65f9a569
Batch ID: 20250622_205639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Red & White International Platform

-- Table to store information about students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- First name of the student
    LastName VARCHAR(50) NOT NULL,            -- Last name of the student
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Email address of the student
    PhoneNumber VARCHAR(15),                  -- Contact number of the student
    DateOfBirth DATE,                         -- Date of birth of the student
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of registration
    Address TEXT                              -- Address of the student
);

-- Table to store information about courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each course
    CourseName VARCHAR(50) NOT NULL,          -- Name of the course (e.g., IELTS, PTE, Spoken English)
    Description TEXT,                         -- Description of the course
    DurationWeeks INT NOT NULL,               -- Duration of the course in weeks
    Fee DECIMAL(10, 2) NOT NULL               -- Fee for the course
);

-- Table to store information about study abroad programs
CREATE TABLE StudyAbroadPrograms (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    Country VARCHAR(50) NOT NULL,             -- Country of the program (e.g., USA, UK, Canada, etc.)
    UniversityName VARCHAR(100) NOT NULL,     -- Name of the university
    ProgramName VARCHAR(100) NOT NULL,        -- Name of the program
    DurationYears INT NOT NULL,               -- Duration of the program in years
    Fee DECIMAL(10, 2) NOT NULL               -- Fee for the program
);

-- Table to store student enrollments in courses
CREATE TABLE StudentCourses (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of enrollment
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Table to store student applications for study abroad programs
CREATE TABLE StudentStudyAbroadApplications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each application
    StudentID INT NOT NULL,                       -- Foreign key referencing Students table
    ProgramID INT NOT NULL,                       -- Foreign key referencing StudyAbroadPrograms table
    ApplicationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of application
    Status ENUM('Pending', 'Approved', 'Rejected') DEFAULT 'Pending', -- Application status
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (ProgramID) REFERENCES StudyAbroadPrograms(ProgramID) ON DELETE CASCADE
);

-- Indexes for faster lookups
CREATE INDEX idx_student_email ON Students(Email);
CREATE INDEX idx_course_name ON Courses(CourseName);
CREATE INDEX idx_program_country ON StudyAbroadPrograms(Country);
```
