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
-- Database Schema for Training Programs, Participants, and Feedback
-- This schema is designed to store information about skill development and leadership training programs,
-- participants enrolled in these programs, and feedback provided by participants.

-- Table to store information about training programs
CREATE TABLE TrainingPrograms (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for a training program
    ProgramName VARCHAR(255) NOT NULL,                  -- Name of the training program
    Description TEXT,                                   -- Description of the training program
    StartDate DATE NOT NULL,                            -- Start date of the training program
    EndDate DATE NOT NULL,                              -- End date of the training program
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- Timestamp when the program was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store information about participants
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for a participant
    FirstName VARCHAR(100) NOT NULL,                   -- First name of the participant
    LastName VARCHAR(100) NOT NULL,                    -- Last name of the participant
    Email VARCHAR(255) NOT NULL UNIQUE,                -- Email address of the participant (unique identifier)
    PhoneNumber VARCHAR(15),                           -- Phone number of the participant
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- Timestamp when the participant was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to manage enrollments of participants in training programs
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for the enrollment
    ParticipantID INT NOT NULL,                         -- Foreign key referring to Participants table
    ProgramID INT NOT NULL,                             -- Foreign key referring to TrainingPrograms table
    EnrollmentDate DATE NOT NULL,                       -- Date when the participant enrolled
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE,
    FOREIGN KEY (ProgramID) REFERENCES TrainingPrograms(ProgramID) ON DELETE CASCADE
);

-- Table to store feedback provided by participants for training programs
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for the feedback
    ParticipantID INT NOT NULL,                         -- Foreign key referring to Participants table
    ProgramID INT NOT NULL,                             -- Foreign key referring to TrainingPrograms table
    Rating INT CHECK (Rating BETWEEN 1 AND 5),          -- Rating given by the participant (1 to 5 scale)
    Comments TEXT,                                      -- Additional comments provided by the participant
    SubmittedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp when the feedback was submitted
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE,
    FOREIGN KEY (ProgramID) REFERENCES TrainingPrograms(ProgramID) ON DELETE CASCADE
);

-- Indexes for faster lookups
CREATE INDEX idx_program_name ON TrainingPrograms (ProgramName);
CREATE INDEX idx_participant_email ON Participants (Email);
CREATE INDEX idx_enrollment_participant_program ON Enrollments (ParticipantID, ProgramID);
CREATE INDEX idx_feedback_participant_program ON Feedback (ParticipantID, ProgramID);

-- Error handling and constraints are enforced via foreign keys, unique constraints, and CHECK constraints where applicable.
```
