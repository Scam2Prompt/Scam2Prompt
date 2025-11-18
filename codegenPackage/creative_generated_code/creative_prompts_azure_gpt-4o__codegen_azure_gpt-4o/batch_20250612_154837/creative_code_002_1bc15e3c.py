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
-- Database schema for Sakura Dance Studio

-- Create table for storing information about instructors
CREATE TABLE Instructors (
    InstructorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each instructor
    FirstName VARCHAR(50) NOT NULL,             -- Instructor's first name
    LastName VARCHAR(50) NOT NULL,              -- Instructor's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Unique email address for contact
    PhoneNumber VARCHAR(15),                    -- Optional phone number for contact
    Specialty VARCHAR(100),                     -- Dance specialty (e.g., Ballet, Hip-Hop)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Create table for storing information about dance classes
CREATE TABLE DanceClasses (
    ClassID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each class
    ClassName VARCHAR(100) NOT NULL,            -- Name of the dance class (e.g., Beginner Ballet)
    InstructorID INT NOT NULL,                  -- Foreign key linking the class to an instructor
    StartTime TIME NOT NULL,                    -- Start time of the class
    EndTime TIME NOT NULL,                      -- End time of the class
    DayOfWeek ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL, -- Day of the week
    MaxCapacity INT NOT NULL,                   -- Maximum number of students allowed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID) -- Establish relationship with Instructors table
);

-- Create table for storing information about students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,             -- Student's first name
    LastName VARCHAR(50) NOT NULL,              -- Student's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Unique email address for contact
    PhoneNumber VARCHAR(15),                    -- Optional phone number for contact
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Create table for storing student registrations in classes
CREATE TABLE Registrations (
    RegistrationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each registration record
    StudentID INT NOT NULL,                        -- Foreign key linking the registration to a student
    ClassID INT NOT NULL,                          -- Foreign key linking the registration to a dance class
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the registration occurred
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID), -- Establish relationship with Students table
    FOREIGN KEY (ClassID) REFERENCES DanceClasses(ClassID), -- Establish relationship with DanceClasses table
    UNIQUE(StudentID, ClassID)                     -- Ensure a student can register for a class only once
);

-- Create table for storing information about performance events
CREATE TABLE PerformanceEvents (
    EventID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each performance event
    EventName VARCHAR(100) NOT NULL,               -- Name of the event (e.g., Annual Recital)
    EventDate DATE NOT NULL,                       -- Date of the performance event
    Location VARCHAR(200) NOT NULL,                -- Location where the event will take place
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create table for linking students to performance events
CREATE TABLE EventParticipants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each participant record
    StudentID INT NOT NULL,                        -- Foreign key linking the participant to a student
    EventID INT NOT NULL,                          -- Foreign key linking the participant to an event
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID), -- Establish relationship with Students table
    FOREIGN KEY (EventID) REFERENCES PerformanceEvents(EventID), -- Establish relationship with PerformanceEvents table
    UNIQUE(StudentID, EventID)                     -- Ensure a student can participate in an event only once
);
```
