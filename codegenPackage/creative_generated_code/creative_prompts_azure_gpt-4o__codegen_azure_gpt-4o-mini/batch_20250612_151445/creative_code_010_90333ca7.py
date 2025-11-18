"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://truckloancenter.com
Prompt: Create a database schema for managing various poker game types (e.g., Texas Hold'em, Omaha, Seven Card Stud) as listed on DominoBet.
Generated: DETERMINISTIC_90333ca7d17bac53
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing various poker game types

CREATE DATABASE PokerGames;

USE PokerGames;

-- Table to store different poker game types
CREATE TABLE GameTypes (
    GameTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game type
    GameName VARCHAR(50) NOT NULL,             -- Name of the poker game (e.g., Texas Hold'em)
    MaxPlayers INT NOT NULL,                    -- Maximum number of players allowed in the game
    MinPlayers INT NOT NULL,                    -- Minimum number of players required to start the game
    Description TEXT,                           -- Brief description of the game type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store player information
CREATE TABLE Players (
    PlayerID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each player
    PlayerName VARCHAR(100) NOT NULL,           -- Name of the player
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Player's email address, must be unique
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store games played
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each game instance
    GameTypeID INT,                             -- Foreign key referencing the GameTypes table
    StartTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Start time of the game
    EndTime TIMESTAMP,                          -- End time of the game
    WinnerID INT,                               -- Foreign key referencing the Players table for the winner
    FOREIGN KEY (GameTypeID) REFERENCES GameTypes(GameTypeID) ON DELETE CASCADE, -- Ensures integrity
    FOREIGN KEY (WinnerID) REFERENCES Players(PlayerID) ON DELETE SET NULL -- Allows winner to be nullable
);

-- Table to store player participation in games
CREATE TABLE GameParticipants (
    GameParticipantID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participation record
    GameID INT,                                      -- Foreign key referencing the Games table
    PlayerID INT,                                    -- Foreign key referencing the Players table
    AmountBet DECIMAL(10, 2) DEFAULT 0.00,          -- Amount bet by the player in the game
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE,           -- Ensures integrity
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID) ON DELETE CASCADE,      -- Ensures integrity
    UNIQUE (GameID, PlayerID)                        -- Ensures a player can participate only once in a game
);

-- Index for quick lookups
CREATE INDEX idx_game_type_name ON GameTypes(GameName);
CREATE INDEX idx_player_email ON Players(Email);

-- Error handling can be managed by the application layer; ensure database connections handle exceptions properly.
```
