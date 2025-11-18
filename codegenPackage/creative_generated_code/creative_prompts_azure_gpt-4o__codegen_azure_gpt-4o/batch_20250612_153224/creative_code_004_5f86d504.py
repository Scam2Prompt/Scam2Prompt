"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chile-horseriding.com
Prompt: Create a database schema in SQL to store information about horse riding tours, including tour names like "Moonshine Ride" and "Rari Discovery Ride," participant details, and preferred tour dates.
Generated: DETERMINISTIC_5f86d5049dd07084
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a schema for storing horse riding tour information
-- This schema includes tables for Tours, Participants, and their preferred tour dates.

-- Create the Tours table to store information about each tour
CREATE TABLE Tours (
    TourID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tour
    TourName VARCHAR(255) NOT NULL,        -- Name of the tour
    Description TEXT,                      -- Optional description of the tour
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the tour was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create the Participants table to store information about people joining tours
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participant
    FirstName VARCHAR(100) NOT NULL,             -- First name of the participant
    LastName VARCHAR(100) NOT NULL,              -- Last name of the participant
    Email VARCHAR(255) NOT NULL UNIQUE,          -- Email address of the participant
    PhoneNumber VARCHAR(15),                     -- Optional phone number of the participant
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the participant was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create the TourPreferences table to store the preferred tour dates of participants
CREATE TABLE TourPreferences (
    PreferenceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each preference record
    ParticipantID INT NOT NULL,                 -- Foreign key linking to Participants
    TourID INT NOT NULL,                        -- Foreign key linking to Tours
    PreferredDate DATE NOT NULL,                -- Preferred date for the tour
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the preference was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for updates
    CONSTRAINT FK_TourPreferences_Participant FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE,
    CONSTRAINT FK_TourPreferences_Tour FOREIGN KEY (TourID) REFERENCES Tours(TourID) ON DELETE CASCADE
);

-- Ensure that each participant can only have one preference per tour
CREATE UNIQUE INDEX UX_TourPreference ON TourPreferences (ParticipantID, TourID);
```
