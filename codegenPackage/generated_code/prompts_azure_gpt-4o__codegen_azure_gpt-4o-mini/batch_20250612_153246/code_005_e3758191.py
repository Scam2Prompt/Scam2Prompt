"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Write code to design a database schema for storing information about training programs, participants, and feedback, based on the association's focus on skill development and leadership training.
Generated: DETERMINISTIC_e375819184730d4f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about training programs, participants, and feedback

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Feedback;
DROP TABLE IF EXISTS Participants;
DROP TABLE IF EXISTS TrainingPrograms;

-- Table to store information about training programs
CREATE TABLE TrainingPrograms (
    ProgramID SERIAL PRIMARY KEY,          -- Unique identifier for each training program
    ProgramName VARCHAR(255) NOT NULL,    -- Name of the training program
    Description TEXT,                      -- Description of the training program
    StartDate DATE NOT NULL,               -- Start date of the training program
    EndDate DATE NOT NULL,                 -- End date of the training program
    SkillFocus VARCHAR(255),                -- Focus area of the training program (e.g., skill development, leadership)
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
    ProgramID INT NOT NULL,                 -- Foreign key referencing the training program
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of registration
    FOREIGN KEY (ProgramID) REFERENCES TrainingPrograms(ProgramID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store feedback from participants
CREATE TABLE Feedback (
    FeedbackID SERIAL PRIMARY KEY,          -- Unique identifier for each feedback entry
    ParticipantID INT NOT NULL,             -- Foreign key referencing the participant
    ProgramID INT NOT NULL,                 -- Foreign key referencing the training program
    Rating INT CHECK (Rating >= 1 AND Rating <= 5), -- Rating given by the participant (1 to 5 scale)
    Comments TEXT,                          -- Additional comments from the participant
    FeedbackDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the feedback was submitted
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProgramID) REFERENCES TrainingPrograms(ProgramID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_program_name ON TrainingPrograms(ProgramName);
CREATE INDEX idx_participant_email ON Participants(Email);
CREATE INDEX idx_feedback_rating ON Feedback(Rating);
```
