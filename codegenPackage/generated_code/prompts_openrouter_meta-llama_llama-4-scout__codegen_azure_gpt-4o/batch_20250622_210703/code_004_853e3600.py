"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: "Design a database schema to store information about ENEM preparation courses, including details about professors, lessons, and student progress, inspired by the Maratona do ENEM platform."
Generated: DETERMINISTIC_853e3600f2a64e74
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for ENEM preparation courses

-- Table to store information about professors
CREATE TABLE Professors (
    ProfessorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each professor
    FullName VARCHAR(100) NOT NULL,             -- Full name of the professor
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Email address of the professor
    Bio TEXT,                                   -- Short biography of the professor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store information about courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,          -- Name of the course
    Description TEXT,                          -- Description of the course
    StartDate DATE NOT NULL,                   -- Start date of the course
    EndDate DATE NOT NULL,                     -- End date of the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store information about lessons
CREATE TABLE Lessons (
    LessonID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each lesson
    CourseID INT NOT NULL,                     -- Foreign key referencing the Courses table
    Title VARCHAR(100) NOT NULL,               -- Title of the lesson
    Content TEXT,                              -- Content of the lesson
    Duration INT NOT NULL,                     -- Duration of the lesson in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Ensures lessons are deleted if the course is deleted
);

-- Table to store information about student progress
CREATE TABLE StudentProgress (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each progress record
    StudentID INT NOT NULL,                    -- Unique identifier for the student
    LessonID INT NOT NULL,                     -- Foreign key referencing the Lessons table
    CompletionStatus ENUM('Not Started', 'In Progress', 'Completed') NOT NULL, -- Status of the lesson completion
    CompletionDate DATE,                       -- Date when the lesson was completed
    FOREIGN KEY (LessonID) REFERENCES Lessons(LessonID) ON DELETE CASCADE -- Ensures progress is deleted if the lesson is deleted
);

-- Table to store information about students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each student
    FullName VARCHAR(100) NOT NULL,            -- Full name of the student
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Email address of the student
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to associate professors with courses
CREATE TABLE CourseProfessors (
    CourseProfessorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each association
    CourseID INT NOT NULL,                            -- Foreign key referencing the Courses table
    ProfessorID INT NOT NULL,                         -- Foreign key referencing the Professors table
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE, -- Ensures association is deleted if the course is deleted
    FOREIGN KEY (ProfessorID) REFERENCES Professors(ProfessorID) ON DELETE CASCADE -- Ensures association is deleted if the professor is deleted
);
```
