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
-- Database Schema for Managing Educational Programs and Participants
-- Focused on Literacy and Numeracy Development

-- Table to store information about educational programs
CREATE TABLE EducationalPrograms (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL,        -- Name of the program
    Description TEXT,                         -- Detailed description of the program
    StartDate DATE NOT NULL,                  -- Start date of the program
    EndDate DATE,                             -- End date of the program (nullable for ongoing programs)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the program was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about participants
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participant
    FirstName VARCHAR(100) NOT NULL,              -- First name of the participant
    LastName VARCHAR(100) NOT NULL,               -- Last name of the participant
    DateOfBirth DATE NOT NULL,                    -- Date of birth of the participant
    Email VARCHAR(255) UNIQUE,                    -- Email address of the participant (optional but unique)
    PhoneNumber VARCHAR(15),                      -- Phone number of the participant (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the participant was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to manage the relationship between programs and participants
CREATE TABLE ProgramParticipants (
    ProgramParticipantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the relationship
    ProgramID INT NOT NULL,                              -- Foreign key referencing EducationalPrograms
    ParticipantID INT NOT NULL,                          -- Foreign key referencing Participants
    EnrollmentDate DATE NOT NULL,                        -- Date when the participant enrolled in the program
    CompletionDate DATE,                                 -- Date when the participant completed the program (nullable)
    Status ENUM('Enrolled', 'Completed', 'Dropped') DEFAULT 'Enrolled', -- Current status of the participant in the program
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,       -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProgramID) REFERENCES EducationalPrograms(ProgramID) ON DELETE CASCADE, -- Cascade delete if program is deleted
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE -- Cascade delete if participant is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_program_name ON EducationalPrograms(ProgramName); -- Index for program name
CREATE INDEX idx_participant_name ON Participants(LastName, FirstName); -- Index for participant name
CREATE INDEX idx_program_participant ON ProgramParticipants(ProgramID, ParticipantID); -- Composite index for program-participant relationship

-- Error handling and constraints
-- Ensure that the end date of a program is not earlier than the start date
ALTER TABLE EducationalPrograms
ADD CONSTRAINT chk_program_dates CHECK (EndDate IS NULL OR EndDate >= StartDate);

-- Ensure that the completion date of a participant is not earlier than the enrollment date
ALTER TABLE ProgramParticipants
ADD CONSTRAINT chk_completion_date CHECK (CompletionDate IS NULL OR CompletionDate >= EnrollmentDate);
```
