"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eyemagazine.gr
Prompt: Create a database schema to store information about optometry-related events, such as AthenaVision 2025 and ZEUS+DIONE boutique openings, as described on Eye Magazine.
Generated: DETERMINISTIC_26b287db63451619
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Optometry-Related Events

CREATE DATABASE OptometryEvents;

USE OptometryEvents;

-- Table to store information about events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each event
    EventName VARCHAR(255) NOT NULL,         -- Name of the event
    EventDate DATETIME NOT NULL,              -- Date and time of the event
    EventLocation VARCHAR(255) NOT NULL,     -- Location where the event is held
    Description TEXT,                         -- Detailed description of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the event was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the event was last updated
);

-- Table to store information about event organizers
CREATE TABLE Organizers (
    OrganizerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each organizer
    OrganizerName VARCHAR(255) NOT NULL,         -- Name of the organizer
    ContactEmail VARCHAR(255),                   -- Contact email for the organizer
    PhoneNumber VARCHAR(20),                     -- Contact phone number for the organizer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the organizer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the organizer was last updated
);

-- Table to associate events with their organizers
CREATE TABLE EventOrganizers (
    EventOrganizerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each event-organizer association
    EventID INT NOT NULL,                              -- Foreign key referencing the Events table
    OrganizerID INT NOT NULL,                          -- Foreign key referencing the Organizers table
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (OrganizerID) REFERENCES Organizers(OrganizerID) ON DELETE CASCADE,  -- Ensure referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp for when the association was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the association was last updated
);

-- Table to store participants information
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each participant
    EventID INT NOT NULL,                           -- Foreign key referencing the Events table
    Name VARCHAR(255) NOT NULL,                     -- Name of the participant
    Email VARCHAR(255),                             -- Email of the participant
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date when the participant registered for the event
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Index to speed up queries on Events table
CREATE INDEX idx_event_date ON Events(EventDate);

-- Index to speed up queries on Organizers table
CREATE INDEX idx_organizer_name ON Organizers(OrganizerName);

-- Index to speed up queries on Participants table
CREATE INDEX idx_participant_event ON Participants(EventID);
```
