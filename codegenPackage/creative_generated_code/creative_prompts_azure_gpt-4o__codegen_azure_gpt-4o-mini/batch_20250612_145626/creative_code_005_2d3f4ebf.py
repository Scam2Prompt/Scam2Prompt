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
-- Database schema for storing information about basketball league participants

CREATE DATABASE BasketballLeague;

USE BasketballLeague;

-- Table to store participants' information
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participant
    FirstName VARCHAR(50) NOT NULL,              -- Participant's first name
    LastName VARCHAR(50) NOT NULL,                -- Participant's last name
    SkillLevel ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL, -- Skill level of the participant
    SchedulePreference VARCHAR(100),               -- Preferred schedule (optional)
    CoachID INT,                                   -- Foreign key to Coaches table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record is created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for updates
    FOREIGN KEY (CoachID) REFERENCES Coaches(CoachID) -- Reference to Coaches table
);

-- Table to store coaches' information
CREATE TABLE Coaches (
    CoachID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each coach
    FirstName VARCHAR(50) NOT NULL,                -- Coach's first name
    LastName VARCHAR(50) NOT NULL,                 -- Coach's last name
    ExperienceLevel ENUM('Novice', 'Intermediate', 'Expert') NOT NULL, -- Experience level of the coach
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the record is created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Table to store games/schedule information
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each game
    ScheduledDate DATETIME NOT NULL,                -- Date and time of the game
    Location VARCHAR(100) NOT NULL,                 -- Location of the game
    ParticipantID INT,                              -- Foreign key to Participants table
    CoachID INT,                                   -- Foreign key to Coaches table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the record is created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for updates
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID), -- Reference to Participants table
    FOREIGN KEY (CoachID) REFERENCES Coaches(CoachID) -- Reference to Coaches table
);

-- Index for quick search on skill level
CREATE INDEX idx_skill_level ON Participants(SkillLevel);

-- Sample data insertion with error handling (using a stored procedure)
DELIMITER //

CREATE PROCEDURE AddParticipant(
    IN p_FirstName VARCHAR(50), 
    IN p_LastName VARCHAR(50), 
    IN p_SkillLevel ENUM('Beginner', 'Intermediate', 'Advanced'),
    IN p_SchedulePreference VARCHAR(100),
    IN p_CoachID INT
)
BEGIN
    -- Error handling
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Log error message or handle it as needed
        SELECT 'Error occurred while inserting participant.' AS ErrorMessage;
    END;

    INSERT INTO Participants (FirstName, LastName, SkillLevel, SchedulePreference, CoachID)
    VALUES (p_FirstName, p_LastName, p_SkillLevel, p_SchedulePreference, p_CoachID);
END //

DELIMITER ;
```
