"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcim.ru
Prompt: Design a database schema in SQL for managing student records and course enrollments at a music school, including tables for instruments, faculty, and student information.
Generated: DETERMINISTIC_774b62fd0ba65a03
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Student Records and Course Enrollments at a Music School

-- Table: Students
-- Stores information about students enrolled in the music school.
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,          -- First name of the student
    LastName VARCHAR(50) NOT NULL,           -- Last name of the student
    DateOfBirth DATE NOT NULL,               -- Date of birth of the student
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Email address of the student
    PhoneNumber VARCHAR(15),                 -- Contact number of the student
    EnrollmentDate DATE NOT NULL,            -- Date the student enrolled in the school
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: Faculty
-- Stores information about the instructors at the music school.
CREATE TABLE Faculty (
    FacultyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each instructor
    FirstName VARCHAR(50) NOT NULL,           -- First name of the instructor
    LastName VARCHAR(50) NOT NULL,            -- Last name of the instructor
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Email address of the instructor
    PhoneNumber VARCHAR(15),                  -- Contact number of the instructor
    HireDate DATE NOT NULL,                   -- Date the instructor was hired
    Specialization VARCHAR(100) NOT NULL,     -- Area of expertise (e.g., piano, guitar)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: Instruments
-- Stores information about musical instruments used in courses.
CREATE TABLE Instruments (
    InstrumentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each instrument
    InstrumentName VARCHAR(50) NOT NULL,        -- Name of the instrument (e.g., piano, guitar)
    Description TEXT,                           -- Brief description of the instrument
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: Courses
-- Stores information about courses offered at the music school.
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,           -- Name of the course (e.g., Beginner Piano)
    Description TEXT,                           -- Brief description of the course
    InstrumentID INT NOT NULL,                  -- Instrument associated with the course
    FacultyID INT NOT NULL,                     -- Faculty assigned to the course
    StartDate DATE NOT NULL,                    -- Course start date
    EndDate DATE NOT NULL,                      -- Course end date
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (InstrumentID) REFERENCES Instruments(InstrumentID) ON DELETE CASCADE, -- Foreign key to Instruments table
    FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID) ON DELETE CASCADE -- Foreign key to Faculty table
);

-- Table: Enrollments
-- Stores information about student enrollments in courses.
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Reference to the student
    CourseID INT NOT NULL,                       -- Reference to the course
    EnrollmentDate DATE NOT NULL,                -- Date the student enrolled in the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Foreign key to Students table
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Foreign key to Courses table
);

-- Ensure the database schema is well-indexed for performance.
-- Add indexes for frequently searched fields.
CREATE INDEX idx_Students_Email ON Students(Email);
CREATE INDEX idx_Faculty_Email ON Faculty(Email);
CREATE INDEX idx_Courses_InstrumentID ON Courses(InstrumentID);
CREATE INDEX idx_Courses_FacultyID ON Courses(FacultyID);
```
