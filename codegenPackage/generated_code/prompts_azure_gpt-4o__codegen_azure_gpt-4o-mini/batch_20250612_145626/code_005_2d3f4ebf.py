"""
Generated Code Metadata:
========================
Original URL: https://lzero.us
Prompt: Create a database schema for storing information about basketball league participants, including fields for skill level, schedule preferences, and coach assignments, inspired by L-Zero's league structure.
Generated: DETERMINISTIC_2d3f4ebf132cd2f9
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for a basketball league

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Participants;
DROP TABLE IF EXISTS Coaches;
DROP TABLE IF EXISTS Skills;
DROP TABLE IF EXISTS Schedules;

-- Table to store skill levels
CREATE TABLE Skills (
    skill_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each skill level
    skill_level VARCHAR(50) NOT NULL UNIQUE    -- Skill level description (e.g., Beginner, Intermediate, Advanced)
);

-- Table to store coaches
CREATE TABLE Coaches (
    coach_id INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each coach
    name VARCHAR(100) NOT NULL,                 -- Coach's name
    experience_years INT NOT NULL CHECK (experience_years >= 0)  -- Years of coaching experience
);

-- Table to store participants
CREATE TABLE Participants (
    participant_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each participant
    name VARCHAR(100) NOT NULL,                     -- Participant's name
    skill_id INT,                                   -- Foreign key referencing skill level
    coach_id INT,                                   -- Foreign key referencing assigned coach
    FOREIGN KEY (skill_id) REFERENCES Skills(skill_id) ON DELETE SET NULL,  -- Link to Skills table
    FOREIGN KEY (coach_id) REFERENCES Coaches(coach_id) ON DELETE SET NULL   -- Link to Coaches table
);

-- Table to store schedule preferences
CREATE TABLE Schedules (
    schedule_id INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each schedule entry
    participant_id INT,                              -- Foreign key referencing participant
    preferred_days VARCHAR(100),                     -- Preferred days for games (e.g., "Monday, Wednesday")
    preferred_time TIME,                             -- Preferred time for games
    FOREIGN KEY (participant_id) REFERENCES Participants(participant_id) ON DELETE CASCADE  -- Link to Participants table
);

-- Insert sample data into Skills table
INSERT INTO Skills (skill_level) VALUES 
('Beginner'), 
('Intermediate'), 
('Advanced');

-- Insert sample data into Coaches table
INSERT INTO Coaches (name, experience_years) VALUES 
('John Doe', 5), 
('Jane Smith', 10);

-- Insert sample data into Participants table
INSERT INTO Participants (name, skill_id, coach_id) VALUES 
('Alice Johnson', 1, 1), 
('Bob Brown', 2, 2);

-- Insert sample data into Schedules table
INSERT INTO Schedules (participant_id, preferred_days, preferred_time) VALUES 
(1, 'Monday, Wednesday', '18:00:00'), 
(2, 'Tuesday, Thursday', '19:00:00');

-- Note: Ensure to handle any potential errors during data insertion in your application logic.
```
