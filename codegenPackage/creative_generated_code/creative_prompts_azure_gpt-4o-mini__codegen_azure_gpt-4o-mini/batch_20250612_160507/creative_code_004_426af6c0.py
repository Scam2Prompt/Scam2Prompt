"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nicerfoundation.org.ng
Prompt: Design a database schema for managing educational programs and participants, based on the NICER Foundation's focus on literacy and numeracy development.
Generated: DETERMINISTIC_426af6c09d8b203d
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing educational programs and participants
-- This schema is designed for the NICER Foundation's focus on literacy and numeracy development.

-- Create a table for storing information about educational programs
CREATE TABLE EducationalPrograms (
    ProgramID SERIAL PRIMARY KEY,         -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL,   -- Name of the educational program
    Description TEXT,                     -- Detailed description of the program
    StartDate DATE NOT NULL,              -- Start date of the program
    EndDate DATE NOT NULL,                -- End date of the program
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the program was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for storing participant information
CREATE TABLE Participants (
    ParticipantID SERIAL PRIMARY KEY,     -- Unique identifier for each participant
    FirstName VARCHAR(100) NOT NULL,      -- Participant's first name
    LastName VARCHAR(100) NOT NULL,       -- Participant's last name
    DateOfBirth DATE NOT NULL,            -- Participant's date of birth
    Email VARCHAR(255) UNIQUE NOT NULL,   -- Participant's email (must be unique)
    Phone VARCHAR(20),                    -- Participant's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the participant was registered
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to link participants to the educational programs they are enrolled in
CREATE TABLE ProgramEnrollments (
    EnrollmentID SERIAL PRIMARY KEY,       -- Unique identifier for each enrollment
    ProgramID INT NOT NULL,                -- Foreign key referencing the educational program
    ParticipantID INT NOT NULL,            -- Foreign key referencing the participant
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the participant enrolled
    Status VARCHAR(50) DEFAULT 'Active',   -- Status of enrollment (Active, Completed, Dropped)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the enrollment was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProgramID) REFERENCES EducationalPrograms(ProgramID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create an index on the email field of participants for faster lookups
CREATE INDEX idx_participant_email ON Participants(Email);

-- Create an index on the program name for faster searches
CREATE INDEX idx_program_name ON EducationalPrograms(ProgramName);

-- Create an index on enrollment status for easy filtering
CREATE INDEX idx_enrollment_status ON ProgramEnrollments(Status);
```
