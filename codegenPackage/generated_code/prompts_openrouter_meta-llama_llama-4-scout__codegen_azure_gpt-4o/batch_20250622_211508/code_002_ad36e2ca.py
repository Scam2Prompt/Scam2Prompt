"""
Generated Code Metadata:
========================
Original URL: https://aceprogaming.co.ke
Prompt: Design a database schema for an esports management firm like Ace Pro Sports Technologies, including tables for teams, players, tournaments, and apparel orders.
Generated: DETERMINISTIC_ad36e2caa453dcca
Batch ID: 20250622_211508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an esports management firm

-- Table: Teams
CREATE TABLE Teams (
    TeamID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each team
    TeamName VARCHAR(100) NOT NULL,        -- Name of the team
    FoundedYear INT,                       -- Year the team was founded
    Region VARCHAR(50),                    -- Region the team belongs to
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: Players
CREATE TABLE Players (
    PlayerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each player
    PlayerName VARCHAR(100) NOT NULL,        -- Name of the player
    Nickname VARCHAR(50),                    -- Player's in-game nickname
    TeamID INT,                              -- Foreign key referencing Teams table
    Age INT,                                 -- Age of the player
    Role VARCHAR(50),                        -- Role of the player (e.g., Support, Carry)
    Country VARCHAR(50),                     -- Country of the player
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE SET NULL ON UPDATE CASCADE
);

-- Table: Tournaments
CREATE TABLE Tournaments (
    TournamentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tournament
    TournamentName VARCHAR(100) NOT NULL,        -- Name of the tournament
    PrizePool DECIMAL(10, 2),                    -- Total prize pool for the tournament
    StartDate DATE,                              -- Start date of the tournament
    EndDate DATE,                                -- End date of the tournament
    Location VARCHAR(100),                      -- Location of the tournament
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: ApparelOrders
CREATE TABLE ApparelOrders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order
    CustomerName VARCHAR(100) NOT NULL,     -- Name of the customer
    Email VARCHAR(100) NOT NULL,            -- Email of the customer
    TeamID INT,                             -- Foreign key referencing Teams table (optional, for team-specific apparel)
    ProductName VARCHAR(100) NOT NULL,      -- Name of the product ordered
    Quantity INT NOT NULL,                  -- Quantity of the product ordered
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the order
    Status VARCHAR(50) DEFAULT 'Pending',  -- Status of the order (e.g., Pending, Shipped, Delivered)
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE SET NULL ON UPDATE CASCADE
);

-- Table: TeamTournamentParticipation
CREATE TABLE TeamTournamentParticipation (
    ParticipationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participation record
    TeamID INT NOT NULL,                            -- Foreign key referencing Teams table
    TournamentID INT NOT NULL,                      -- Foreign key referencing Tournaments table
    Placement INT,                                  -- Placement of the team in the tournament (e.g., 1 for winner)
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (TournamentID) REFERENCES Tournaments(TournamentID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table: PlayerStatistics
CREATE TABLE PlayerStatistics (
    StatisticID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each statistic record
    PlayerID INT NOT NULL,                      -- Foreign key referencing Players table
    TournamentID INT NOT NULL,                  -- Foreign key referencing Tournaments table
    MatchesPlayed INT NOT NULL,                 -- Number of matches played in the tournament
    Kills INT NOT NULL,                         -- Number of kills in the tournament
    Deaths INT NOT NULL,                        -- Number of deaths in the tournament
    Assists INT NOT NULL,                       -- Number of assists in the tournament
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (TournamentID) REFERENCES Tournaments(TournamentID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Ensure proper indexing for efficient queries
CREATE INDEX idx_TeamName ON Teams(TeamName);
CREATE INDEX idx_PlayerName ON Players(PlayerName);
CREATE INDEX idx_TournamentName ON Tournaments(TournamentName);
CREATE INDEX idx_OrderStatus ON ApparelOrders(Status);
```
