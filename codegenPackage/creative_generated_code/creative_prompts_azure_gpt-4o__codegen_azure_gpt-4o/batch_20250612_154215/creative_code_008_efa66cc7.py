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
-- Create schema for Ace Pro Sports Technologies to manage esports tournaments

-- Table to store information about tournaments
CREATE TABLE Tournaments (
    TournamentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tournament
    Name VARCHAR(255) NOT NULL, -- Name of the tournament
    Location VARCHAR(255), -- Location where the tournament is held
    StartDate DATE NOT NULL, -- Start date of the tournament
    EndDate DATE NOT NULL, -- End date of the tournament
    PrizePool DECIMAL(15, 2), -- Total prize pool for the tournament
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about participants
CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participant
    Name VARCHAR(255) NOT NULL, -- Name of the participant/team
    Type ENUM('Individual', 'Team') NOT NULL, -- Participant type (individual or team)
    Country VARCHAR(100), -- Country of origin
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about sponsors
CREATE TABLE Sponsors (
    SponsorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each sponsor
    Name VARCHAR(255) NOT NULL, -- Name of the sponsoring entity
    Industry VARCHAR(255), -- Industry the sponsor belongs to
    ContactEmail VARCHAR(255), -- Contact email for the sponsor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about apparel designs
CREATE TABLE ApparelDesigns (
    DesignID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each design
    Name VARCHAR(255) NOT NULL, -- Name of the design
    Description TEXT, -- Description of the design
    DesignerName VARCHAR(255), -- Name of the designer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to map participants to tournaments
CREATE TABLE TournamentParticipants (
    TournamentID INT NOT NULL, -- Foreign key referencing Tournaments table
    ParticipantID INT NOT NULL, -- Foreign key referencing Participants table
    FOREIGN KEY (TournamentID) REFERENCES Tournaments(TournamentID) ON DELETE CASCADE, -- Cascade delete to maintain integrity
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID) ON DELETE CASCADE, -- Cascade delete to maintain integrity
    UNIQUE(TournamentID, ParticipantID) -- Ensure a participant is mapped to a tournament only once
);

-- Table to map sponsors to tournaments
CREATE TABLE TournamentSponsors (
    TournamentID INT NOT NULL, -- Foreign key referencing Tournaments table
    SponsorID INT NOT NULL, -- Foreign key referencing Sponsors table
    FOREIGN KEY (TournamentID) REFERENCES Tournaments(TournamentID) ON DELETE CASCADE, -- Cascade delete to maintain integrity
    FOREIGN KEY (SponsorID) REFERENCES Sponsors(SponsorID) ON DELETE CASCADE, -- Cascade delete to maintain integrity
    UNIQUE(TournamentID, SponsorID) -- Ensure a sponsor is mapped to a tournament only once
);

-- Table to map apparel designs to tournaments
CREATE TABLE TournamentApparelDesigns (
    TournamentID INT NOT NULL, -- Foreign key referencing Tournaments table
    DesignID INT NOT NULL, -- Foreign key referencing ApparelDesigns table
    FOREIGN KEY (TournamentID) REFERENCES Tournaments(TournamentID) ON DELETE CASCADE, -- Cascade delete to maintain integrity
    FOREIGN KEY (DesignID) REFERENCES ApparelDesigns(DesignID) ON DELETE CASCADE, -- Cascade delete to maintain integrity
    UNIQUE(TournamentID, DesignID) -- Ensure a design is mapped to a tournament only once
);
```
