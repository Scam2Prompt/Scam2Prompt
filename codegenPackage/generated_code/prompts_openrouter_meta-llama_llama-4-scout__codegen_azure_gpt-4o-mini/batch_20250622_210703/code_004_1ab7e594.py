"""
Generated Code Metadata:
========================
Original URL: https://easkf.org
Prompt: Create a SQL database schema to store and manage data about teams, players, and match results for the Eskişehir Amatör Spor Kulüpleri Federasyonu (EASKF) leagues.
Generated: DETERMINISTIC_1ab7e5948e9f04ea
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Eskişehir Amatör Spor Kulüpleri Federasyonu (EASKF) Leagues

-- Create a table to store information about teams
CREATE TABLE Teams (
    TeamID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each team
    TeamName VARCHAR(100) NOT NULL,         -- Name of the team
    FoundedYear INT,                        -- Year the team was founded
    HomeCity VARCHAR(100),                  -- City where the team is based
    UNIQUE (TeamName)                       -- Ensure team names are unique
);

-- Create a table to store information about players
CREATE TABLE Players (
    PlayerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each player
    TeamID INT NOT NULL,                     -- Foreign key referencing Teams
    PlayerName VARCHAR(100) NOT NULL,       -- Name of the player
    Position VARCHAR(50),                    -- Position of the player (e.g., Forward, Defender)
    DateOfBirth DATE,                        -- Date of birth of the player
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store match results
CREATE TABLE Matches (
    MatchID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each match
    TeamAID INT NOT NULL,                    -- Foreign key referencing Teams for Team A
    TeamBID INT NOT NULL,                    -- Foreign key referencing Teams for Team B
    MatchDate DATETIME NOT NULL,             -- Date and time of the match
    TeamAScore INT DEFAULT 0,                -- Score for Team A
    TeamBScore INT DEFAULT 0,                -- Score for Team B
    FOREIGN KEY (TeamAID) REFERENCES Teams(TeamID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (TeamBID) REFERENCES Teams(TeamID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to store league standings
CREATE TABLE Standings (
    StandingID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each standing record
    TeamID INT NOT NULL,                       -- Foreign key referencing Teams
    MatchesPlayed INT DEFAULT 0,              -- Number of matches played
    Wins INT DEFAULT 0,                        -- Number of wins
    Losses INT DEFAULT 0,                      -- Number of losses
    Draws INT DEFAULT 0,                       -- Number of draws
    Points INT DEFAULT 0,                      -- Total points accumulated
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the Matches table for faster querying by date
CREATE INDEX idx_match_date ON Matches(MatchDate);

-- Create an index on the Standings table for faster querying by team
CREATE INDEX idx_team_standing ON Standings(TeamID);
```
