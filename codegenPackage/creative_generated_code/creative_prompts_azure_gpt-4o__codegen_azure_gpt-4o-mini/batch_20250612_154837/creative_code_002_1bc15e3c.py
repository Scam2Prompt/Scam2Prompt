"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mujeresautistas.com
Prompt: Create a database schema for storing information about dance classes, instructors, student registrations, and performance events, inspired by the structure of Sakura Dance Studio.
Generated: DETERMINISTIC_1bc15e3c2dd7bf31
Batch ID: 20250612_154837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about dance classes, instructors,
-- student registrations, and performance events for Sakura Dance Studio.

-- Drop existing tables if they exist to start fresh
DROP TABLE IF EXISTS PerformanceEvents;
DROP TABLE IF EXISTS StudentRegistrations;
DROP TABLE IF EXISTS DanceClasses;
DROP TABLE IF EXISTS Instructors;

-- Table to store information about instructors
CREATE TABLE Instructors (
    InstructorID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each instructor
    FirstName VARCHAR(50) NOT NULL,               -- Instructor's first name
    LastName VARCHAR(50) NOT NULL,                 -- Instructor's last name
    Email VARCHAR(100) UNIQUE NOT NULL,            -- Instructor's email (must be unique)
    Phone VARCHAR(15),                             -- Instructor's contact number
    Bio TEXT,                                      -- Brief biography of the instructor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store information about dance classes
CREATE TABLE DanceClasses (
    ClassID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each class
    ClassName VARCHAR(100) NOT NULL,               -- Name of the dance class
    Description TEXT,                               -- Description of the class
    InstructorID INT,                              -- Foreign key referencing the instructor
    Schedule VARCHAR(100) NOT NULL,                -- Schedule for the class
    MaxParticipants INT NOT NULL,                  -- Maximum number of participants allowed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID) ON DELETE SET NULL -- Ensure referential integrity
);

-- Table to store information about student registrations
CREATE TABLE StudentRegistrations (
    RegistrationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each registration
    StudentName VARCHAR(100) NOT NULL,              -- Name of the student
    Email VARCHAR(100) NOT NULL,                     -- Student's email
    Phone VARCHAR(15),                               -- Student's contact number
    ClassID INT,                                    -- Foreign key referencing the dance class
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of registration
    FOREIGN KEY (ClassID) REFERENCES DanceClasses(ClassID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store information about performance events
CREATE TABLE PerformanceEvents (
    EventID INT PRIMARY KEY AUTO_INCREMENT,          -- Unique identifier for each event
    EventName VARCHAR(100) NOT NULL,                -- Name of the performance event
    EventDate DATETIME NOT NULL,                     -- Date and time of the event
    Location VARCHAR(150) NOT NULL,                  -- Location of the event
    Description TEXT,                                -- Description of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Ensure proper indexing for faster queries (optional but recommended)
CREATE INDEX idx_instructor_email ON Instructors(Email);
CREATE INDEX idx_class_name ON DanceClasses(ClassName);
CREATE INDEX idx_student_email ON StudentRegistrations(Email);
CREATE INDEX idx_event_date ON PerformanceEvents(EventDate);
```
