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
-- Database schema for managing course details, student registrations, and trainer assignments

-- Create a table to store information about courses
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,         -- Name of the course
    Description TEXT,                          -- Detailed description of the course
    Duration INT NOT NULL,                     -- Duration of the course in hours
    StartDate DATE NOT NULL,                   -- Start date of the course
    EndDate DATE NOT NULL,                     -- End date of the course
    TrainerID INT,                             -- Foreign key reference to the Trainer
    FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID) ON DELETE SET NULL
);

-- Create a table to store information about trainers
CREATE TABLE Trainers (
    TrainerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each trainer
    TrainerName VARCHAR(255) NOT NULL,        -- Name of the trainer
    Specialization VARCHAR(255),               -- Trainer's area of expertise
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Trainer's email
    Phone VARCHAR(15)                          -- Trainer's phone number
);

-- Create a table to store information about students
CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each student
    StudentName VARCHAR(255) NOT NULL,         -- Name of the student
    Email VARCHAR(255) UNIQUE NOT NULL,         -- Student's email
    Phone VARCHAR(15),                          -- Student's phone number
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date of registration
);

-- Create a table to manage student registrations for courses
CREATE TABLE Registrations (
    RegistrationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each registration
    CourseID INT NOT NULL,                          -- Foreign key reference to the Course
    StudentID INT NOT NULL,                         -- Foreign key reference to the Student
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of registration
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    UNIQUE (CourseID, StudentID)                   -- Prevent duplicate registrations
);

-- Create an index to improve query performance on Courses table by TrainerID
CREATE INDEX idx_trainer ON Courses(TrainerID);

-- Create an index for quicker lookups in the Registrations table
CREATE INDEX idx_course_student ON Registrations(CourseID, StudentID);
```
