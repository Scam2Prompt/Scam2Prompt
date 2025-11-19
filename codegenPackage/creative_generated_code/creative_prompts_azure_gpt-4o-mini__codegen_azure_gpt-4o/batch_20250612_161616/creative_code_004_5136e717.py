"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jualessandraensina.com
Prompt: Design a database schema for managing student profiles and course enrollments in a makeup education platform similar to Ju Ensina, including fields for techniques learned and progress tracking.
Generated: DETERMINISTIC_5136e7179c738394
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Makeup Education Platform

-- Table to store student profiles
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(100) NOT NULL,          -- First name of the student
    LastName VARCHAR(100) NOT NULL,           -- Last name of the student
    Email VARCHAR(255) UNIQUE NOT NULL,       -- Email address of the student
    PhoneNumber VARCHAR(20),                  -- Optional phone number of the student
    DateOfBirth DATE,                         -- Date of Birth for the student
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Registration date for the student profile
    ProfilePictureURL VARCHAR(255)            -- Optional profile picture URL
);

-- Table to store courses offered
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,        -- Name of the course
    Description TEXT,                        -- Course description
    DurationHours INT NOT NULL,              -- Duration of the course in hours
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the course was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to manage student enrollments in courses
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for enrollment
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    CourseID INT NOT NULL,                       -- Foreign key referencing Courses table
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of enrollment
    ProgressPercentage DECIMAL(5,2) DEFAULT 0.00, -- Progress tracking (0.00% to 100.00%)
    CompletionDate DATE,                         -- Optional completion date
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Table to store techniques learned in a course
CREATE TABLE Techniques (
    TechniqueID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for a technique
    TechniqueName VARCHAR(255) NOT NULL,        -- Name of the technique
    CourseID INT NOT NULL,                      -- Foreign key referencing Courses table
    Description TEXT,                           -- Description of the technique
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- Table to track techniques learned by students
CREATE TABLE StudentTechniques (
    StudentTechniqueID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for a student-technique record
    StudentID INT NOT NULL,                            -- Foreign key referencing Students table
    TechniqueID INT NOT NULL,                          -- Foreign key referencing Techniques table
    LearnedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Date when the technique was learned
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (TechniqueID) REFERENCES Techniques(TechniqueID) ON DELETE CASCADE
);

-- Index to improve query performance for student progress tracking
CREATE INDEX idx_student_progress ON Enrollments (StudentID, CourseID, ProgressPercentage);

-- Index to optimize technique lookups learned by students
CREATE INDEX idx_techniques_learned ON StudentTechniques (StudentID, TechniqueID);
```
