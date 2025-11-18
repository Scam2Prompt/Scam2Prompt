"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tda.org.sa
Prompt: Write code to design a database schema for storing information about training programs, participants, and feedback, based on the association's focus on skill development and leadership training.
Generated: DETERMINISTIC_e375819184730d4f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about training programs, participants, and feedback

-- Create a table for storing training programs
CREATE TABLE TrainingPrograms (
    ProgramID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each training program
    ProgramName VARCHAR(255) NOT NULL,           -- Name of the training program
    Description TEXT,                             -- Description of the training program
    StartDate DATE NOT NULL,                      -- Start date of the training program
    EndDate DATE NOT NULL,                        -- End date of the training program
    Location VARCHAR(255),                        -- Location of the training program
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the program was created
);

-- Create a table for storing participants
CREATE TABLE Participants (
    ParticipantID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each participant
    FirstName VARCHAR(100) NOT NULL,             -- First name of the participant
    LastName VARCHAR(100) NOT NULL,               -- Last name of the participant
    Email VARCHAR(255) UNIQUE NOT NULL,           -- Unique email address of the participant
    PhoneNumber VARCHAR(15),                      -- Phone number of the participant
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for when the participant was added
);

-- Create a table for storing feedback regarding training programs
CREATE TABLE Feedback (
    FeedbackID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each feedback entry
    ProgramID INT NOT NULL,                       -- ID of the training program for which feedback is given
    ParticipantID INT NOT NULL,                   -- ID of the participant giving feedback
    Rating INT CHECK (Rating >= 1 AND Rating <= 5), -- Rating given by the participant (1-5 scale)
    Comments TEXT,                                -- Additional comments from the participant
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the feedback was provided
    
    -- Foreign key constraints to ensure referential integrity
    FOREIGN KEY (ProgramID) REFERENCES TrainingPrograms(ProgramID) ON DELETE CASCADE,
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE
);

-- Indexes to improve query performance
CREATE INDEX idx_program_name ON TrainingPrograms(ProgramName);
CREATE INDEX idx_participant_email ON Participants(Email);
CREATE INDEX idx_feedback_rating ON Feedback(Rating);
```
