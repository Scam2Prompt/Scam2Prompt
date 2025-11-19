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

-- Create a table to store information about events
CREATE TABLE EducationalEvents (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    EventName VARCHAR(255) NOT NULL,        -- Name of the event
    EventType ENUM('Jornada', 'Simposio') NOT NULL, -- Type of the event (e.g., Jornada or Simposio)
    Description TEXT,                       -- Detailed description of the event
    StartDate DATE NOT NULL,                -- Start date of the event
    EndDate DATE NOT NULL,                  -- End date of the event
    Location VARCHAR(255),                  -- Location where the event is held
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the event record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Create a table to store information about participants
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participant
    FullName VARCHAR(255) NOT NULL,               -- Full name of the participant
    Email VARCHAR(255) NOT NULL UNIQUE,           -- Email address of the participant
    PhoneNumber VARCHAR(20),                      -- Phone number of the participant
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the participant record was created
);

-- Create a table to store event registrations (many-to-many relationship between events and participants)
CREATE TABLE EventRegistrations (
    RegistrationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each registration
    EventID INT NOT NULL,                          -- Foreign key referencing EducationalEvents(EventID)
    ParticipantID INT NOT NULL,                    -- Foreign key referencing Participants(ParticipantID)
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the registration was made
    FOREIGN KEY (EventID) REFERENCES EducationalEvents(EventID) ON DELETE CASCADE,
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE
);

-- Create a table to store event organizers
CREATE TABLE Organizers (
    OrganizerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each organizer
    FullName VARCHAR(255) NOT NULL,             -- Full name of the organizer
    Email VARCHAR(255) NOT NULL UNIQUE,         -- Email address of the organizer
    PhoneNumber VARCHAR(20),                    -- Phone number of the organizer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the organizer record was created
);

-- Create a table to associate organizers with events (many-to-many relationship)
CREATE TABLE EventOrganizers (
    EventOrganizerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each association
    EventID INT NOT NULL,                            -- Foreign key referencing EducationalEvents(EventID)
    OrganizerID INT NOT NULL,                        -- Foreign key referencing Organizers(OrganizerID)
    FOREIGN KEY (EventID) REFERENCES EducationalEvents(EventID) ON DELETE CASCADE,
    FOREIGN KEY (OrganizerID) REFERENCES Organizers(OrganizerID) ON DELETE CASCADE
);

-- Ensure proper indexing for efficient queries
CREATE INDEX idx_event_type ON EducationalEvents(EventType);
CREATE INDEX idx_event_start_date ON EducationalEvents(StartDate);
CREATE INDEX idx_participant_email ON Participants(Email);
CREATE INDEX idx_organizer_email ON Organizers(Email);
```
