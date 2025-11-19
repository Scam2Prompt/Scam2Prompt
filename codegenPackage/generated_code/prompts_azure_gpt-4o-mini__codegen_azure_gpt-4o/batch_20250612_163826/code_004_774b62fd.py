"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Design a database schema in SQL for managing student records and course enrollments at a music school, including tables for instruments, faculty, and student information.
Generated: DETERMINISTIC_774b62fd0ba65a03
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing student records and course enrollments at a music school

-- Table for storing student information
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- Student's first name
    LastName VARCHAR(50) NOT NULL,            -- Student's last name
    DateOfBirth DATE NOT NULL,                -- Student's date of birth
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Student's email address
    PhoneNumber VARCHAR(15),                  -- Student's phone number
    RegistrationDate DATE NOT NULL DEFAULT CURRENT_DATE -- Date of registration
);

-- Table for storing faculty information
CREATE TABLE Faculty (
    FacultyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each faculty member
    FirstName VARCHAR(50) NOT NULL,           -- Faculty member's first name
    LastName VARCHAR(50) NOT NULL,            -- Faculty member's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Faculty member's email address
    PhoneNumber VARCHAR(15),                  -- Faculty member's phone number
    HireDate DATE NOT NULL DEFAULT CURRENT_DATE -- Date of hire
);

-- Table for storing instruments offered by the music school
CREATE TABLE Instruments (
    InstrumentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each instrument
    Name VARCHAR(50) NOT NULL,                   -- Name of the instrument
    Description TEXT,                            -- Description of the instrument
    IsAvailable BOOLEAN NOT NULL DEFAULT TRUE    -- Availability status of the instrument
);

-- Table for storing courses offered by the music school
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    Name VARCHAR(100) NOT NULL,              -- Name of the course
    Description TEXT,                        -- Description of the course
    InstrumentID INT NOT NULL,               -- Instrument associated with the course
    FacultyID INT NOT NULL,                  -- Faculty member teaching the course
    StartDate DATE NOT NULL,                 -- Start date of the course
    EndDate DATE NOT NULL,                   -- End date of the course
    FOREIGN KEY (InstrumentID) REFERENCES Instruments(InstrumentID) ON DELETE CASCADE,
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID) ON DELETE CASCADE
);

-- Table for storing student enrollments in courses
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Student enrolled in the course
    CourseID INT NOT NULL,                       -- Course the student is enrolled in
    EnrollmentDate DATE NOT NULL DEFAULT CURRENT_DATE, -- Date of enrollment
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_students_email ON Students(Email);
CREATE INDEX idx_faculty_email ON Faculty(Email);
CREATE INDEX idx_courses_instrument ON Courses(InstrumentID);
CREATE INDEX idx_enrollments_student_course ON Enrollments(StudentID, CourseID);

-- End of schema
```
