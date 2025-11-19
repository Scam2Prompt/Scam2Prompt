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
-- SQL Schema for EASKF Leagues Database

-- Create a database for EASKF
CREATE DATABASE IF NOT EXISTS EASKF_Leagues;

-- Use the newly created database
USE EASKF_Leagues;

-- Table to store information about teams
CREATE TABLE IF NOT EXISTS Teams (
    TeamID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each team
    TeamName VARCHAR(100) NOT NULL,        -- Name of the team
    City VARCHAR(50),                      -- City where the team is based
    FoundedYear YEAR,                      -- Year the team was founded
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about players
CREATE TABLE IF NOT EXISTS Players (
    PlayerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each player
    TeamID INT NOT NULL,                      -- Foreign key referencing the team the player belongs to
    FirstName VARCHAR(50) NOT NULL,           -- Player's first name
    LastName VARCHAR(50) NOT NULL,            -- Player's last name
    Position VARCHAR(30),                     -- Player's position (e.g., Forward, Midfielder, etc.)
    DateOfBirth DATE,                         -- Player's date of birth
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE CASCADE -- Cascade delete if the team is deleted
);

-- Table to store match results
CREATE TABLE IF NOT EXISTS Matches (
    MatchID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each match
    HomeTeamID INT NOT NULL,                -- Foreign key referencing the home team
    AwayTeamID INT NOT NULL,                -- Foreign key referencing the away team
    MatchDate DATE NOT NULL,                -- Date of the match
    HomeTeamScore INT NOT NULL,             -- Score of the home team
    AwayTeamScore INT NOT NULL,             -- Score of the away team
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (HomeTeamID) REFERENCES Teams(TeamID) ON DELETE CASCADE, -- Cascade delete if the home team is deleted
    FOREIGN KEY (AwayTeamID) REFERENCES Teams(TeamID) ON DELETE CASCADE -- Cascade delete if the away team is deleted
);

-- Table to store league information
CREATE TABLE IF NOT EXISTS Leagues (
    LeagueID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each league
    LeagueName VARCHAR(100) NOT NULL,        -- Name of the league
    Season VARCHAR(20) NOT NULL,             -- Season of the league (e.g., 2023/2024)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to associate teams with leagues
CREATE TABLE IF NOT EXISTS LeagueTeams (
    LeagueTeamID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each league-team association
    LeagueID INT NOT NULL,                       -- Foreign key referencing the league
    TeamID INT NOT NULL,                         -- Foreign key referencing the team
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (LeagueID) REFERENCES Leagues(LeagueID) ON DELETE CASCADE, -- Cascade delete if the league is deleted
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE CASCADE -- Cascade delete if the team is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_team_name ON Teams(TeamName);
CREATE INDEX idx_player_name ON Players(LastName, FirstName);
CREATE INDEX idx_match_date ON Matches(MatchDate);
CREATE INDEX idx_league_name ON Leagues(LeagueName);
```
