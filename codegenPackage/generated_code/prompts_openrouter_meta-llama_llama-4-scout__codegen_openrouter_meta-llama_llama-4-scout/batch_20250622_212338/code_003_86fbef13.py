"""
Generated Code Metadata:
========================
Original URL: https://lethmixedslowpitch.com
Prompt: Design a database schema to store information about slowpitch softball teams, players, and game scores, inspired by the features of Slo-Pitch Central.
Generated: DETERMINISTIC_86fbef136af8c5d3
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for slowpitch softball teams, players, and game scores

-- Create database
CREATE DATABASE SlowpitchSoftball;

-- Use database
USE SlowpitchSoftball;

-- Create table for teams
CREATE TABLE Teams (
    TeamID INT AUTO_INCREMENT,
    TeamName VARCHAR(255) NOT NULL,
    TeamCity VARCHAR(100) NOT NULL,
    TeamState VARCHAR(50) NOT NULL,
    PRIMARY KEY (TeamID)
);

-- Create table for players
CREATE TABLE Players (
    PlayerID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    TeamID INT,
    PRIMARY KEY (PlayerID),
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE SET NULL
);

-- Create table for games
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT,
    HomeTeamID INT NOT NULL,
    AwayTeamID INT NOT NULL,
    GameDate DATE NOT NULL,
    PRIMARY KEY (GameID),
    FOREIGN KEY (HomeTeamID) REFERENCES Teams(TeamID),
    FOREIGN KEY (AwayTeamID) REFERENCES Teams(TeamID),
    CHECK (HomeTeamID <> AwayTeamID)
);

-- Create table for game scores
CREATE TABLE GameScores (
    ScoreID INT AUTO_INCREMENT,
    GameID INT NOT NULL,
    Inning INT NOT NULL,
    HomeTeamScore INT NOT NULL,
    AwayTeamScore INT NOT NULL,
    PRIMARY KEY (ScoreID),
    FOREIGN KEY (GameID) REFERENCES Games(GameID)
);

-- Create table for final game scores
CREATE TABLE FinalGameScores (
    FinalScoreID INT AUTO_INCREMENT,
    GameID INT NOT NULL,
    HomeTeamScore INT NOT NULL,
    AwayTeamScore INT NOT NULL,
    PRIMARY KEY (FinalScoreID),
    FOREIGN KEY (GameID) REFERENCES Games(GameID)
);

-- Create table for player game stats
CREATE TABLE PlayerGameStats (
    StatID INT AUTO_INCREMENT,
    GameID INT NOT NULL,
    PlayerID INT NOT NULL,
    AtBats INT NOT NULL DEFAULT 0,
    Runs INT NOT NULL DEFAULT 0,
    Hits INT NOT NULL DEFAULT 0,
    RunsBattedIn INT NOT NULL DEFAULT 0,
    PRIMARY KEY (StatID),
    FOREIGN KEY (GameID) REFERENCES Games(GameID),
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID)
);

-- Example insert statements
INSERT INTO Teams (TeamName, TeamCity, TeamState)
VALUES 
('Sluggers', 'Anytown', 'CA'),
('Bangers', 'Othertown', 'NY');

INSERT INTO Players (FirstName, LastName, Email, Phone, TeamID)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', 1),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', 2);

INSERT INTO Games (HomeTeamID, AwayTeamID, GameDate)
VALUES 
(1, 2, '2022-01-01'),
(2, 1, '2022-01-15');

INSERT INTO GameScores (GameID, Inning, HomeTeamScore, AwayTeamScore)
VALUES 
(1, 1, 0, 0),
(1, 2, 2, 1),
(2, 1, 1, 0),
(2, 2, 0, 2);

INSERT INTO FinalGameScores (GameID, HomeTeamScore, AwayTeamScore)
VALUES 
(1, 5, 3),
(2, 2, 4);

INSERT INTO PlayerGameStats (GameID, PlayerID, AtBats, Runs, Hits, RunsBattedIn)
VALUES 
(1, 1, 3, 1, 2, 1),
(1, 2, 4, 0, 1, 0),
(2, 1, 4, 0, 1, 0),
(2, 2, 3, 1, 2, 2);
```
