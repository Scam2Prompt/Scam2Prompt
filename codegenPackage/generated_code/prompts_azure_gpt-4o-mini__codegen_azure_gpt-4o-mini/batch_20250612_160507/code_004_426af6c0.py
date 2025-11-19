"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Design a database schema for managing educational programs and participants, based on the NICER Foundation's focus on literacy and numeracy development.
Generated: DETERMINISTIC_426af6c09d8b203d
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing educational programs and participants
-- Focused on literacy and numeracy development for the NICER Foundation

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Participants;
DROP TABLE IF EXISTS Programs;
DROP TABLE IF EXISTS Enrollments;

-- Table to store information about educational programs
CREATE TABLE Programs (
    ProgramID SERIAL PRIMARY KEY,          -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL,    -- Name of the program
    Description TEXT,                      -- Description of the program
    StartDate DATE NOT NULL,               -- Start date of the program
    EndDate DATE NOT NULL,                 -- End date of the program
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the program was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about participants
CREATE TABLE Participants (
    ParticipantID SERIAL PRIMARY KEY,      -- Unique identifier for each participant
    FirstName VARCHAR(100) NOT NULL,       -- First name of the participant
    LastName VARCHAR(100) NOT NULL,        -- Last name of the participant
    Email VARCHAR(255) UNIQUE NOT NULL,    -- Email of the participant (must be unique)
    PhoneNumber VARCHAR(15),                -- Phone number of the participant
    DateOfBirth DATE,                       -- Date of birth of the participant
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the participant was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to manage enrollments of participants in programs
CREATE TABLE Enrollments (
    EnrollmentID SERIAL PRIMARY KEY,        -- Unique identifier for each enrollment
    ParticipantID INT NOT NULL,             -- Foreign key referencing Participants
    ProgramID INT NOT NULL,                 -- Foreign key referencing Programs
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of enrollment
    Status VARCHAR(50) DEFAULT 'active',    -- Status of the enrollment (e.g., active, completed, dropped)
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_participant_email ON Participants(Email);
CREATE INDEX idx_program_name ON Programs(ProgramName);
CREATE INDEX idx_enrollment_status ON Enrollments(Status);
```
