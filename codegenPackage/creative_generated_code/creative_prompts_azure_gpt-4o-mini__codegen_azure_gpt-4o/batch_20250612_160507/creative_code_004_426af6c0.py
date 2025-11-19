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
-- Database Schema for Managing Educational Programs and Participants

-- Create table for storing information about educational programs
CREATE TABLE EducationalPrograms (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL,         -- Name of the program
    Description TEXT,                          -- Detailed description of the program
    StartDate DATE NOT NULL,                   -- Start date of the program
    EndDate DATE,                              -- End date of the program (nullable for ongoing programs)
    FocusArea ENUM('Literacy', 'Numeracy') NOT NULL, -- Focus area (restricted to literacy or numeracy)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Create table for storing information about participants
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participant
    FirstName VARCHAR(100) NOT NULL,              -- First name of the participant
    LastName VARCHAR(100) NOT NULL,               -- Last name of the participant
    Email VARCHAR(255) UNIQUE NOT NULL,           -- Email address for communication (must be unique)
    PhoneNumber VARCHAR(20),                      -- Contact phone number (optional)
    DateOfBirth DATE,                             -- Date of birth of the participant
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Create table for associating participants with educational programs
CREATE TABLE ProgramParticipants (
    ProgramParticipantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for record
    ProgramID INT NOT NULL,                              -- Foreign key referencing EducationalPrograms
    ParticipantID INT NOT NULL,                          -- Foreign key referencing Participants
    EnrollmentDate DATE NOT NULL,                        -- Date when the participant enrolled in the program
    Status ENUM('Enrolled', 'Completed', 'Withdrawn') NOT NULL, -- Status of the participant in the program
    Feedback TEXT,                                       -- Optional feedback provided by the participant
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,       -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (ProgramID) REFERENCES EducationalPrograms(ProgramID) ON DELETE CASCADE, -- Cascade on delete
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE -- Cascade on delete
);

-- Indexes to improve query performance
CREATE INDEX idx_program_focus_area ON EducationalPrograms(FocusArea); -- Index on focus area for quick filtering
CREATE INDEX idx_participants_email ON Participants(Email);            -- Index on email for quick lookup
CREATE INDEX idx_program_participant ON ProgramParticipants(ProgramID, ParticipantID); -- Composite index for associations
```
