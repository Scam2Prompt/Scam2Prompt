"""
Generated Code Metadata:
========================
Original URL: https://aceprogaming.co.ke
Prompt: Create a sample database schema for managing esports tournaments, including tables for participants, sponsors, and event details as utilized by Ace Pro.
Generated: DETERMINISTIC_480799cc53d43ba7
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing esports tournaments

-- Table: Participants
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participant
    Name VARCHAR(100) NOT NULL,                   -- Name of the participant
    TeamName VARCHAR(100),                        -- Name of the team (if applicable)
    Country VARCHAR(50),                          -- Country of the participant
    Email VARCHAR(100) UNIQUE,                    -- Contact email
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the participant was added
);

-- Table: Sponsors
CREATE TABLE Sponsors (
    SponsorID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each sponsor
    Name VARCHAR(100) NOT NULL,                   -- Name of the sponsor
    ContactPerson VARCHAR(100),                   -- Name of the contact person
    Email VARCHAR(100) UNIQUE,                    -- Contact email
    PhoneNumber VARCHAR(15),                      -- Contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the sponsor was added
);

-- Table: Events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each event
    Name VARCHAR(100) NOT NULL,                   -- Name of the event
    Location VARCHAR(100),                        -- Location of the event
    StartDate DATE NOT NULL,                      -- Start date of the event
    EndDate DATE NOT NULL,                        -- End date of the event
    PrizePool DECIMAL(10, 2),                     -- Total prize pool for the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the event was added
);

-- Table: EventParticipants (Many-to-Many relationship between Events and Participants)
CREATE TABLE EventParticipants (
    EventID INT NOT NULL,                         -- Foreign key referencing Events table
    ParticipantID INT NOT NULL,                   -- Foreign key referencing Participants table
    PRIMARY KEY (EventID, ParticipantID),         -- Composite primary key
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE,
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE
);

-- Table: EventSponsors (Many-to-Many relationship between Events and Sponsors)
CREATE TABLE EventSponsors (
    EventID INT NOT NULL,                         -- Foreign key referencing Events table
    SponsorID INT NOT NULL,                       -- Foreign key referencing Sponsors table
    PRIMARY KEY (EventID, SponsorID),             -- Composite primary key
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE,
    FOREIGN KEY (SponsorID) REFERENCES Sponsors(SponsorID) ON DELETE CASCADE
);

-- Indexes for optimization
CREATE INDEX idx_participant_email ON Participants(Email); -- Index for quick lookup by email
CREATE INDEX idx_sponsor_email ON Sponsors(Email);         -- Index for quick lookup by email
CREATE INDEX idx_event_dates ON Events(StartDate, EndDate);-- Index for quick lookup by event dates
```
