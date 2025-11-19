"""
Generated Code Metadata:
========================
Original URL: https://cimedweb.org
Prompt: "Develop a data model for storing information about educational events, such as CIMEd's jornadas and simposios, and provide a SQL code snippet for creating the database schema."
Generated: DETERMINISTIC_ce143a1a0ac9c54a
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for storing information about educational events

-- Create a database for educational events
CREATE DATABASE EducationalEvents;

-- Use the created database
USE EducationalEvents;

-- Table to store information about events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each event
    Title VARCHAR(255) NOT NULL,              -- Title of the event
    Description TEXT,                          -- Detailed description of the event
    EventType ENUM('Jornada', 'Simposio') NOT NULL,  -- Type of the event
    StartDate DATETIME NOT NULL,               -- Start date and time of the event
    EndDate DATETIME NOT NULL,                 -- End date and time of the event
    Location VARCHAR(255),                     -- Location of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the event was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Table to store information about participants
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each participant
    EventID INT NOT NULL,                          -- Foreign key referencing the Events table
    Name VARCHAR(255) NOT NULL,                    -- Name of the participant
    Email VARCHAR(255) NOT NULL UNIQUE,            -- Email of the participant
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of registration
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store information about speakers
CREATE TABLE Speakers (
    SpeakerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each speaker
    EventID INT NOT NULL,                       -- Foreign key referencing the Events table
    Name VARCHAR(255) NOT NULL,                 -- Name of the speaker
    Bio TEXT,                                   -- Biography of the speaker
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store feedback for events
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each feedback entry
    EventID INT NOT NULL,                       -- Foreign key referencing the Events table
    ParticipantID INT NOT NULL,                 -- Foreign key referencing the Participants table
    Rating INT CHECK (Rating BETWEEN 1 AND 5),  -- Rating given by the participant (1 to 5)
    Comments TEXT,                              -- Additional comments from the participant
    FeedbackDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when feedback was given
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes can be added for performance optimization as needed
```
