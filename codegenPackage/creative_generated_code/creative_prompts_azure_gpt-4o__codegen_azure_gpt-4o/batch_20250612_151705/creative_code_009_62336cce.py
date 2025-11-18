"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridgeadvisory.com
Prompt: Recommend a database schema for managing course details, student registrations, and trainer assignments for a corporate training firm like Debridge Advisory.
Generated: DETERMINISTIC_62336cce0ab2a374
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Corporate Training Management
-- This schema manages course details, student registrations, and trainer assignments.

-- Table: Courses
-- Stores details about the courses offered by the training firm
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,                -- Name of the course
    Description TEXT,                                -- Detailed description of the course
    DurationInDays INT NOT NULL,                     -- Duration of the course in days
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp when the course record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table: Trainers
-- Stores details about trainers who conduct the courses
CREATE TABLE Trainers (
    TrainerID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each trainer
    FullName VARCHAR(255) NOT NULL,                  -- Full name of the trainer
    Email VARCHAR(255) NOT NULL UNIQUE,              -- Email address of the trainer (must be unique)
    PhoneNumber VARCHAR(15),                         -- Contact number of the trainer
    Specialty VARCHAR(255),                          -- Area of expertise of the trainer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp when the trainer record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table: Students
-- Stores details about students who register for courses
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each student
    FullName VARCHAR(255) NOT NULL,                  -- Full name of the student
    Email VARCHAR(255) NOT NULL UNIQUE,              -- Email address of the student (must be unique)
    PhoneNumber VARCHAR(15),                         -- Contact number of the student
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp when the student record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table: Registrations
-- Tracks which students are registered for which courses
CREATE TABLE Registrations (
    RegistrationID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each registration
    StudentID INT NOT NULL,                          -- Foreign key referring to the Students table
    CourseID INT NOT NULL,                           -- Foreign key referring to the Courses table
    RegistrationDate DATE NOT NULL,                  -- Date when the student registered for the course
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID), -- Ensures StudentID exists in Students table
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)    -- Ensures CourseID exists in Courses table
);

-- Table: TrainerAssignments
-- Tracks trainers assigned to conduct specific courses
CREATE TABLE TrainerAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each assignment
    TrainerID INT NOT NULL,                          -- Foreign key referring to the Trainers table
    CourseID INT NOT NULL,                           -- Foreign key referring to the Courses table
    AssignmentDate DATE NOT NULL,                    -- Date when the trainer was assigned to the course
    FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID), -- Ensures TrainerID exists in Trainers table
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)    -- Ensures CourseID exists in Courses table
);

-- Indexes for improving query performance
CREATE INDEX idx_course_name ON Courses(CourseName);
CREATE INDEX idx_trainer_email ON Trainers(Email);
CREATE INDEX idx_student_email ON Students(Email);
CREATE INDEX idx_registration_date ON Registrations(RegistrationDate);
CREATE INDEX idx_assignment_date ON TrainerAssignments(AssignmentDate);

-- Additional Constraints (if required):
-- 1. Ensure no duplicate registrations for the same student in the same course.
ALTER TABLE Registrations
ADD UNIQUE(StudentID, CourseID);

-- 2. Ensure no duplicate trainer assignments to the same course.
ALTER TABLE TrainerAssignments
ADD UNIQUE(TrainerID, CourseID);
```
