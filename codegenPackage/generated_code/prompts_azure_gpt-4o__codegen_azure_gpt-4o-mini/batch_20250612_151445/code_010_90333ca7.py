"""
Generated Code Metadata:
========================
Original URL: https://truckloancenter.com
Prompt: Create a database schema for managing various poker game types (e.g., Texas Hold'em, Omaha, Seven Card Stud) as listed on DominoBet.
Generated: DETERMINISTIC_90333ca7d17bac53
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing various poker game types

CREATE DATABASE PokerGames;

USE PokerGames;

-- Table to store different types of poker games
CREATE TABLE GameTypes (
    GameTypeID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each game type
    GameName VARCHAR(50) NOT NULL,              -- Name of the poker game (e.g., Texas Hold'em)
    Description TEXT,                            -- Description of the game rules and features
    MaxPlayers INT NOT NULL CHECK (MaxPlayers > 1),  -- Maximum number of players allowed
    MinPlayers INT NOT NULL CHECK (MinPlayers > 1),  -- Minimum number of players required
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the game type was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store game sessions
CREATE TABLE GameSessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each game session
    GameTypeID INT NOT NULL,                     -- Foreign key referencing the GameTypes table
    StartTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Start time of the game session
    EndTime TIMESTAMP,                           -- End time of the game session
    WinnerID INT,                                -- Player ID of the winner (if applicable)
    FOREIGN KEY (GameTypeID) REFERENCES GameTypes(GameTypeID) ON DELETE CASCADE,  -- Ensures referential integrity
    CHECK (EndTime IS NULL OR EndTime > StartTime)  -- Ensures end time is after start time
);

-- Table to store players participating in the game sessions
CREATE TABLE Players (
    PlayerID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each player
    PlayerName VARCHAR(100) NOT NULL,             -- Name of the player
    Email VARCHAR(100) UNIQUE NOT NULL,           -- Unique email for player identification
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the player was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to link players to game sessions
CREATE TABLE SessionPlayers (
    SessionPlayerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each session-player link
    SessionID INT NOT NULL,                          -- Foreign key referencing the GameSessions table
    PlayerID INT NOT NULL,                           -- Foreign key referencing the Players table
    FOREIGN KEY (SessionID) REFERENCES GameSessions(SessionID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID) ON DELETE CASCADE,  -- Ensures referential integrity
    UNIQUE (SessionID, PlayerID)                    -- Ensures a player can only join a session once
);

-- Table to store game results
CREATE TABLE GameResults (
    ResultID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each game result
    SessionID INT NOT NULL,                         -- Foreign key referencing the GameSessions table
    PlayerID INT NOT NULL,                          -- Foreign key referencing the Players table
    Position INT NOT NULL,                          -- Position of the player in the game (1 for winner, etc.)
    Prize DECIMAL(10, 2) DEFAULT 0.00,             -- Prize won by the player (if applicable)
    FOREIGN KEY (SessionID) REFERENCES GameSessions(SessionID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_game_type_name ON GameTypes(GameName);
CREATE INDEX idx_session_start_time ON GameSessions(StartTime);
CREATE INDEX idx_player_email ON Players(Email);
```
