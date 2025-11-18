"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aceprogaming.co.ke
Prompt: Generate a database schema to store information about esports tournaments, participants, sponsors, and apparel designs, as described by Ace Pro Sports Technologies.
Generated: DETERMINISTIC_efa66cc7498ce3bd
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about esports tournaments, participants, sponsors, and apparel designs

-- Table to store information about esports tournaments
CREATE TABLE Tournaments (
    TournamentID SERIAL PRIMARY KEY, -- Unique identifier for each tournament
    Name VARCHAR(255) NOT NULL,       -- Name of the tournament
    StartDate TIMESTAMP NOT NULL,      -- Start date and time of the tournament
    EndDate TIMESTAMP NOT NULL,        -- End date and time of the tournament
    Location VARCHAR(255),             -- Location where the tournament is held
    PrizePool DECIMAL(10, 2),          -- Total prize pool for the tournament
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about participants
CREATE TABLE Participants (
    ParticipantID SERIAL PRIMARY KEY, -- Unique identifier for each participant
    Name VARCHAR(255) NOT NULL,       -- Name of the participant
    Team VARCHAR(255),                 -- Name of the team the participant belongs to
    TournamentID INT REFERENCES Tournaments(TournamentID) ON DELETE CASCADE, -- Foreign key referencing tournaments
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about sponsors
CREATE TABLE Sponsors (
    SponsorID SERIAL PRIMARY KEY,      -- Unique identifier for each sponsor
    Name VARCHAR(255) NOT NULL,       -- Name of the sponsor
    Website VARCHAR(255),              -- Website of the sponsor
    ContactEmail VARCHAR(255),         -- Contact email for the sponsor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about apparel designs
CREATE TABLE ApparelDesigns (
    ApparelID SERIAL PRIMARY KEY,      -- Unique identifier for each apparel design
    DesignName VARCHAR(255) NOT NULL,  -- Name of the apparel design
    Description TEXT,                   -- Description of the apparel design
    SponsorID INT REFERENCES Sponsors(SponsorID) ON DELETE SET NULL, -- Foreign key referencing sponsors
    TournamentID INT REFERENCES Tournaments(TournamentID) ON DELETE SET NULL, -- Foreign key referencing tournaments
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store the relationship between participants and apparel designs
CREATE TABLE ParticipantApparel (
    ParticipantID INT REFERENCES Participants(ParticipantID) ON DELETE CASCADE, -- Foreign key referencing participants
    ApparelID INT REFERENCES ApparelDesigns(ApparelID) ON DELETE CASCADE,      -- Foreign key referencing apparel designs
    PRIMARY KEY (ParticipantID, ApparelID) -- Composite primary key
);
```
