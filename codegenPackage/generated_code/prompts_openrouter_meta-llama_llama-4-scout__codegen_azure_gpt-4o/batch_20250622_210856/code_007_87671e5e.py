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

-- Table to store information about schools and their locations
CREATE TABLE Schools (
    SchoolID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each school
    SchoolName VARCHAR(255) NOT NULL,        -- Name of the school
    Address VARCHAR(255) NOT NULL,           -- Address of the school
    City VARCHAR(100) NOT NULL,              -- City where the school is located
    State VARCHAR(100) NOT NULL,             -- State where the school is located
    ZipCode VARCHAR(20) NOT NULL,            -- Zip code of the school
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about programs
CREATE TABLE Programs (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL,        -- Name of the program
    Description TEXT,                         -- Description of the program
    SchoolID INT NOT NULL,                    -- Foreign key referencing Schools table
    StartDate DATE NOT NULL,                  -- Start date of the program
    EndDate DATE NOT NULL,                    -- End date of the program
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (SchoolID) REFERENCES Schools(SchoolID) ON DELETE CASCADE -- Cascade delete if school is removed
);

-- Table to store information about students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(100) NOT NULL,          -- First name of the student
    LastName VARCHAR(100) NOT NULL,           -- Last name of the student
    Email VARCHAR(255) NOT NULL UNIQUE,       -- Email address of the student
    PhoneNumber VARCHAR(20),                  -- Phone number of the student
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store student registrations for programs
CREATE TABLE Registrations (
    RegistrationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each registration
    StudentID INT NOT NULL,                        -- Foreign key referencing Students table
    ProgramID INT NOT NULL,                        -- Foreign key referencing Programs table
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of registration
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Cascade delete if student is removed
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE -- Cascade delete if program is removed
);

-- Table to store program schedules
CREATE TABLE ProgramSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each schedule
    ProgramID INT NOT NULL,                    -- Foreign key referencing Programs table
    DayOfWeek ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL, -- Day of the week
    StartTime TIME NOT NULL,                   -- Start time of the program session
    EndTime TIME NOT NULL,                     -- End time of the program session
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE -- Cascade delete if program is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_school_city ON Schools (City);
CREATE INDEX idx_program_dates ON Programs (StartDate, EndDate);
CREATE INDEX idx_student_email ON Students (Email);
CREATE INDEX idx_registration_program ON Registrations (ProgramID);
CREATE INDEX idx_schedule_day ON ProgramSchedules (DayOfWeek);
```
