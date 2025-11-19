"""
Generated Code Metadata:
========================
Original URL: https://aceprogaming.co.ke
Prompt: Generate a database schema to store information about esports tournaments, participants, sponsors, and apparel designs, as described by Ace Pro Sports Technologies.
Generated: DETERMINISTIC_efa66cc7498ce3bd
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about esports tournaments, participants, sponsors, and apparel designs

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ApparelDesigns;
DROP TABLE IF EXISTS Sponsors;
DROP TABLE IF EXISTS Participants;
DROP TABLE IF EXISTS Tournaments;

-- Table to store information about esports tournaments
CREATE TABLE Tournaments (
    TournamentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each tournament
    Name VARCHAR(255) NOT NULL,                   -- Name of the tournament
    StartDate DATETIME NOT NULL,                   -- Start date and time of the tournament
    EndDate DATETIME NOT NULL,                     -- End date and time of the tournament
    Location VARCHAR(255),                         -- Location of the tournament
    PrizePool DECIMAL(10, 2),                      -- Total prize pool for the tournament
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the tournament was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the tournament was last updated
);

-- Table to store information about participants in tournaments
CREATE TABLE Participants (
    ParticipantID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each participant
    TournamentID INT NOT NULL,                      -- Foreign key referencing the tournament
    Name VARCHAR(255) NOT NULL,                     -- Name of the participant
    Team VARCHAR(255),                              -- Team name of the participant
    Score INT DEFAULT 0,                            -- Score of the participant in the tournament
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the participant was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the participant was last updated
    FOREIGN KEY (TournamentID) REFERENCES Tournaments(TournamentID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about sponsors of tournaments
CREATE TABLE Sponsors (
    SponsorID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each sponsor
    Name VARCHAR(255) NOT NULL,                     -- Name of the sponsor
    Contribution DECIMAL(10, 2) NOT NULL,          -- Amount contributed by the sponsor
    TournamentID INT NOT NULL,                      -- Foreign key referencing the tournament
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the sponsor was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the sponsor was last updated
    FOREIGN KEY (TournamentID) REFERENCES Tournaments(TournamentID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about apparel designs related to tournaments
CREATE TABLE ApparelDesigns (
    ApparelDesignID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each apparel design
    TournamentID INT NOT NULL,                      -- Foreign key referencing the tournament
    DesignName VARCHAR(255) NOT NULL,              -- Name of the apparel design
    DesignURL VARCHAR(255),                         -- URL to the design image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the design was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the design was last updated
    FOREIGN KEY (TournamentID) REFERENCES Tournaments(TournamentID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes can be added for performance optimization if necessary
-- Example: CREATE INDEX idx_tournament_name ON Tournaments(Name);
```
