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
-- Database schema for storing information about slowpitch softball teams, players, and game scores

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS GameScores;
DROP TABLE IF EXISTS Players;
DROP TABLE IF EXISTS Teams;

-- Table to store information about teams
CREATE TABLE Teams (
    TeamID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each team
    TeamName VARCHAR(100) NOT NULL,         -- Name of the team
    CoachName VARCHAR(100),                  -- Name of the team's coach
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the team was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store information about players
CREATE TABLE Players (
    PlayerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each player
    TeamID INT NOT NULL,                      -- Foreign key referencing the Teams table
    PlayerName VARCHAR(100) NOT NULL,        -- Name of the player
    Position VARCHAR(50),                     -- Position of the player (e.g., pitcher, catcher)
    DateOfBirth DATE,                        -- Date of birth of the player
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the player was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store game scores
CREATE TABLE GameScores (
    GameID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each game
    Team1ID INT NOT NULL,                     -- Foreign key referencing the first team
    Team2ID INT NOT NULL,                     -- Foreign key referencing the second team
    Team1Score INT NOT NULL,                  -- Score of the first team
    Team2Score INT NOT NULL,                  -- Score of the second team
    GameDate DATETIME NOT NULL,               -- Date and time of the game
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the game score was recorded
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (Team1ID) REFERENCES Teams(TeamID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (Team2ID) REFERENCES Teams(TeamID) ON DELETE CASCADE   -- Ensures referential integrity
);

-- Sample data insertion (optional, for testing purposes)
INSERT INTO Teams (TeamName, CoachName) VALUES ('The Sluggers', 'John Doe');
INSERT INTO Teams (TeamName, CoachName) VALUES ('The Pitchers', 'Jane Smith');

INSERT INTO Players (TeamID, PlayerName, Position, DateOfBirth) VALUES (1, 'Alice Johnson', 'Pitcher', '1990-05-15');
INSERT INTO Players (TeamID, PlayerName, Position, DateOfBirth) VALUES (1, 'Bob Brown', 'Catcher', '1988-08-22');
INSERT INTO Players (TeamID, PlayerName, Position, DateOfBirth) VALUES (2, 'Charlie Green', 'Outfielder', '1992-03-10');

INSERT INTO GameScores (Team1ID, Team2ID, Team1Score, Team2Score, GameDate) VALUES (1, 2, 10, 8, '2023-10-01 14:00:00');
```
