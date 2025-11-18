"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lzero.us
Prompt: Create a database schema for storing information about basketball league participants, including fields for skill level, schedule preferences, and coach assignments, inspired by L-Zero's league structure.
Generated: DETERMINISTIC_2d3f4ebf132cd2f9
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for Basketball League Participants

-- Table to store participants' basic information
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each participant
    FirstName VARCHAR(50) NOT NULL,              -- First name of the participant
    LastName VARCHAR(50) NOT NULL,               -- Last name of the participant
    Email VARCHAR(100) NOT NULL UNIQUE,          -- Contact email for the participant
    PhoneNumber VARCHAR(15),                     -- Contact phone number (optional)
    SkillLevel ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL, -- Skill level classification
    DateJoined DATE DEFAULT CURRENT_DATE,        -- Date participant joined the league
    CONSTRAINT chk_SkillLevel CHECK (SkillLevel IN ('Beginner', 'Intermediate', 'Advanced'))
);

-- Table to store schedule preferences for participants
CREATE TABLE SchedulePreferences (
    PreferenceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each schedule preference
    ParticipantID INT NOT NULL,                  -- Foreign key linking to Participants table
    PreferredDay ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL, -- Preferred day of the week
    PreferredTime TIME NOT NULL,                 -- Preferred time of day
    IsFlexible BOOLEAN DEFAULT FALSE,            -- Whether the participant is flexible with their schedule
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE
);

-- Table to store coach information
CREATE TABLE Coaches (
    CoachID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique ID for each coach
    FirstName VARCHAR(50) NOT NULL,              -- Coach's first name
    LastName VARCHAR(50) NOT NULL,               -- Coach's last name
    Email VARCHAR(100) NOT NULL UNIQUE,          -- Contact email for the coach
    PhoneNumber VARCHAR(15),                     -- Contact phone number
    Expertise ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL, -- Expertise level of the coach
    YearsOfExperience INT DEFAULT 0 CHECK (YearsOfExperience >= 0) -- Total years of coaching experience
);

-- Table to store participant-coach assignments
CREATE TABLE CoachAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each assignment
    ParticipantID INT NOT NULL,                  -- Foreign key linking to Participants table
    CoachID INT NOT NULL,                        -- Foreign key linking to Coaches table
    AssignmentDate DATE DEFAULT CURRENT_DATE,    -- Date the assignment was made
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE,
    FOREIGN KEY (CoachID) REFERENCES Coaches(CoachID) ON DELETE SET NULL
);

-- Indexes to optimize lookups
CREATE INDEX idx_participant_skill_level ON Participants(SkillLevel);
CREATE INDEX idx_schedule_preference_participant ON SchedulePreferences(ParticipantID);
CREATE INDEX idx_coach_expertise ON Coaches(Expertise);
```
