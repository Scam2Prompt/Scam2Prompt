"""
Generated Code Metadata:
========================
Original URL: https://plus.endeavorschools.com
Prompt: "Design a database schema to store information about Endeavor Plus programs, including student registrations, program schedules, and school locations."
Generated: DETERMINISTIC_87671e5e92020e3f
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Endeavor Plus programs

-- Table to store information about schools
CREATE TABLE Schools (
    SchoolID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each school
    SchoolName VARCHAR(255) NOT NULL,         -- Name of the school
    Address VARCHAR(255),                      -- Address of the school
    City VARCHAR(100),                         -- City where the school is located
    State VARCHAR(100),                        -- State where the school is located
    ZipCode VARCHAR(10)                        -- Zip code of the school
);

-- Table to store information about programs
CREATE TABLE Programs (
    ProgramID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL,        -- Name of the program
    Description TEXT,                          -- Description of the program
    StartDate DATE NOT NULL,                   -- Start date of the program
    EndDate DATE NOT NULL,                     -- End date of the program
    SchoolID INT,                              -- Foreign key referencing Schools
    FOREIGN KEY (SchoolID) REFERENCES Schools(SchoolID) ON DELETE CASCADE
);

-- Table to store student information
CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each student
    FirstName VARCHAR(100) NOT NULL,           -- First name of the student
    LastName VARCHAR(100) NOT NULL,            -- Last name of the student
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Email address of the student
    PhoneNumber VARCHAR(15)                     -- Phone number of the student
);

-- Table to store student registrations for programs
CREATE TABLE Registrations (
    RegistrationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each registration
    StudentID INT,                                  -- Foreign key referencing Students
    ProgramID INT,                                  -- Foreign key referencing Programs
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date of registration
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending',  -- Registration status
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE,
    UNIQUE (StudentID, ProgramID)                  -- Ensure a student can register for a program only once
);

-- Table to store program schedules
CREATE TABLE ProgramSchedules (
    ScheduleID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each schedule
    ProgramID INT,                               -- Foreign key referencing Programs
    ScheduleDate DATE NOT NULL,                  -- Date of the scheduled program
    StartTime TIME NOT NULL,                     -- Start time of the program
    EndTime TIME NOT NULL,                       -- End time of the program
    Location VARCHAR(255),                       -- Location of the program
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE
);
```
