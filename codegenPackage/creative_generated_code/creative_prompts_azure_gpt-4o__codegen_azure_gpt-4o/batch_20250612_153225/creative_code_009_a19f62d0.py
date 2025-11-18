"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openmindsinstituto.com.br
Prompt: Create a database schema for storing participant information and session details for study groups focused on respiratory disorders and neonatal dysphagia, as described on Open Minds Instituto's website.
Generated: DETERMINISTIC_a19f62d085bd4859
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Study Groups on Respiratory Disorders and Neonatal Dysphagia

-- Create a table to store participant information
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each participant
    FirstName VARCHAR(50) NOT NULL,                   -- First name of the participant
    LastName VARCHAR(50) NOT NULL,                    -- Last name of the participant
    Email VARCHAR(100) UNIQUE NOT NULL,               -- Email address of the participant (must be unique)
    PhoneNumber VARCHAR(20),                          -- Contact number for the participant
    DateOfBirth DATE,                                 -- Participant's date of birth
    MedicalHistory TEXT,                              -- Brief medical history or notes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store session details
CREATE TABLE StudySessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each session
    SessionName VARCHAR(100) NOT NULL,                -- Name or title of the session
    SessionDate DATE NOT NULL,                        -- Date of the session
    StartTime TIME NOT NULL,                          -- Start time of the session
    EndTime TIME NOT NULL,                            -- End time of the session
    FocusArea ENUM('Respiratory Disorders', 'Neonatal Dysphagia') NOT NULL, -- Focus area of the session
    Description TEXT,                                 -- Detailed description of the session
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a junction table to link participants with study sessions
CREATE TABLE ParticipantSessions (
    ParticipantSessionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each entry
    ParticipantID INT NOT NULL,                          -- Foreign key referencing Participants table
    SessionID INT NOT NULL,                              -- Foreign key referencing StudySessions table
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the participant registered for the session
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE, -- Cascade delete for participant
    FOREIGN KEY (SessionID) REFERENCES StudySessions(SessionID) ON DELETE CASCADE         -- Cascade delete for session
);

-- Indexing for faster lookups
CREATE INDEX idx_participant_email ON Participants (Email);
CREATE INDEX idx_session_date ON StudySessions (SessionDate);
CREATE INDEX idx_participant_session ON ParticipantSessions (ParticipantID, SessionID);
```
