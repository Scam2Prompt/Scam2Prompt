"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aceprogaming.co.ke
Prompt: Create a sample database schema for managing esports tournaments, including tables for participants, sponsors, and event details as utilized by Ace Pro.
Generated: DETERMINISTIC_480799cc53d43ba7
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing esports tournaments

-- Table for storing participant information
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each participant
    Name VARCHAR(255) NOT NULL, -- Name of the participant
    TeamName VARCHAR(255), -- Name of the team (null if solo participant)
    Email VARCHAR(320) UNIQUE, -- Contact email (must be unique)
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the participant registered
    Rank INT NULL, -- Rank of the participant (null if unranked)
    Country VARCHAR(100) -- Country of origin
);

-- Table for storing sponsor information
CREATE TABLE Sponsors (
    SponsorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each sponsor
    Name VARCHAR(255) NOT NULL, -- Name of the sponsor
    Website VARCHAR(2083), -- Sponsor's website URL
    ContactEmail VARCHAR(320), -- Contact email for the sponsor
    PhoneNumber VARCHAR(15), -- Contact phone number
    SponsorshipAmount DECIMAL(10, 2) NOT NULL DEFAULT 0, -- Amount sponsored in USD
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table for storing event details
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each event
    Name VARCHAR(255) NOT NULL, -- Name of the event
    StartDate DATE NOT NULL, -- Start date of the event
    EndDate DATE NOT NULL, -- End date of the event
    Location VARCHAR(255), -- Physical or virtual location
    PrizePool DECIMAL(10, 2) NOT NULL DEFAULT 0, -- Total prize pool in USD
    SponsorID INT, -- Foreign key to the Sponsors table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (SponsorID) REFERENCES Sponsors(SponsorID) ON DELETE SET NULL -- Sponsor details reference
);

-- Junction table for linking participants to events (many-to-many relationship)
CREATE TABLE EventParticipants (
    EventParticipantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each record
    EventID INT NOT NULL, -- Foreign key to the Events table
    ParticipantID INT NOT NULL, -- Foreign key to the Participants table
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the participant registered for the event
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Cascade delete on event removal
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE -- Cascade delete on participant removal
);

-- Ensure proper indexing for faster queries
CREATE INDEX idx_participants_email ON Participants(Email);
CREATE INDEX idx_sponsors_email ON Sponsors(ContactEmail);
CREATE INDEX idx_event_startdate ON Events(StartDate);
CREATE INDEX idx_eventparticipants_event_participant ON EventParticipants(EventID, ParticipantID);

-- Example error handling: Ensure valid data inputs in the database
-- Note: Input validation should be handled at the application level before inserting data into these tables.
```
