"""
Generated Code Metadata:
========================
Original URL: https://isbgames.isbeventteam.com
Prompt: Design a database schema to store information about participants, events, and sponsors for the ISB Games 2024.
Generated: DETERMINISTIC_2eae9dd16c164e7a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for ISB Games 2024

-- Table to store participant information
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participant
    FirstName VARCHAR(50) NOT NULL,               -- First name of the participant
    LastName VARCHAR(50) NOT NULL,                -- Last name of the participant
    Email VARCHAR(100) UNIQUE NOT NULL,           -- Email address of the participant
    PhoneNumber VARCHAR(15),                      -- Contact number of the participant
    Age INT CHECK (Age >= 0),                     -- Age of the participant (must be non-negative)
    Gender ENUM('Male', 'Female', 'Other'),       -- Gender of the participant
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date and time of registration
);

-- Table to store event information
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each event
    EventName VARCHAR(100) NOT NULL,              -- Name of the event
    EventDate DATE NOT NULL,                      -- Date of the event
    EventTime TIME NOT NULL,                      -- Time of the event
    Location VARCHAR(100) NOT NULL,               -- Location where the event will take place
    MaxParticipants INT CHECK (MaxParticipants > 0), -- Maximum number of participants allowed
    Description TEXT                              -- Description of the event
);

-- Table to store sponsor information
CREATE TABLE Sponsors (
    SponsorID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each sponsor
    SponsorName VARCHAR(100) NOT NULL,            -- Name of the sponsor
    ContactPerson VARCHAR(100),                   -- Name of the contact person
    Email VARCHAR(100) UNIQUE NOT NULL,           -- Email address of the sponsor
    PhoneNumber VARCHAR(15),                      -- Contact number of the sponsor
    SponsorshipAmount DECIMAL(10, 2) NOT NULL,    -- Amount sponsored by the sponsor
    SponsorshipDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date and time of sponsorship
);

-- Table to store participant-event relationships
CREATE TABLE ParticipantEvents (
    ParticipantEventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the relationship
    ParticipantID INT NOT NULL,                        -- Foreign key referencing Participants table
    EventID INT NOT NULL,                              -- Foreign key referencing Events table
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of event registration
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE,
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE
);

-- Table to store event-sponsor relationships
CREATE TABLE EventSponsors (
    EventSponsorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the relationship
    EventID INT NOT NULL,                          -- Foreign key referencing Events table
    SponsorID INT NOT NULL,                        -- Foreign key referencing Sponsors table
    ContributionAmount DECIMAL(10, 2) NOT NULL,    -- Amount contributed by the sponsor for the event
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE,
    FOREIGN KEY (SponsorID) REFERENCES Sponsors(SponsorID) ON DELETE CASCADE
);

-- Indexes for optimization
CREATE INDEX idx_participant_email ON Participants(Email); -- Index for quick lookup of participants by email
CREATE INDEX idx_event_date ON Events(EventDate);          -- Index for quick lookup of events by date
CREATE INDEX idx_sponsor_email ON Sponsors(Email);         -- Index for quick lookup of sponsors by email
```
