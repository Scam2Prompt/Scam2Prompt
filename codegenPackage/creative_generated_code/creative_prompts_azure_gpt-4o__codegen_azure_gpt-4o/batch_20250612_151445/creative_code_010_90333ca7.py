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
-- Database Schema for Managing Various Poker Game Types

-- Create a table for poker game types
CREATE TABLE PokerGameTypes (
    GameTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game type
    GameName VARCHAR(50) NOT NULL,             -- Name of the poker game (e.g., Texas Hold'em, Omaha, Seven Card Stud)
    Description TEXT,                          -- Description of the game rules or details
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the game type was added
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Create a table for poker games
CREATE TABLE PokerGames (
    GameID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each game
    GameTypeID INT NOT NULL,                 -- Foreign key linking to the PokerGameTypes table
    MaxPlayers INT NOT NULL,                 -- Maximum number of players allowed in the game
    MinPlayers INT NOT NULL,                 -- Minimum number of players required to start the game
    StakeAmount DECIMAL(10, 2) NOT NULL,     -- Amount of stake for the game
    GameStartTime DATETIME,                  -- Scheduled start time for the game
    GameStatus ENUM('Scheduled', 'Ongoing', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Scheduled', -- Status of the game
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the game was created
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (GameTypeID) REFERENCES PokerGameTypes(GameTypeID) ON DELETE CASCADE ON UPDATE CASCADE -- Foreign key constraint
);

-- Create a table for player participation in poker games
CREATE TABLE PokerGamePlayers (
    ParticipationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each player-game relationship
    GameID INT NOT NULL,                            -- Foreign key linking to the PokerGames table
    PlayerID INT NOT NULL,                          -- Unique identifier for the player (assume a Player table exists elsewhere)
    BuyInAmount DECIMAL(10, 2) NOT NULL,            -- Amount of money the player bought into the game
    JoinTime DATETIME DEFAULT CURRENT_TIMESTAMP,    -- Timestamp when the player joined the game
    LeaveTime DATETIME,                             -- Timestamp when the player left the game (nullable)
    ParticipationStatus ENUM('Active', 'Left', 'Eliminated') NOT NULL DEFAULT 'Active', -- Status of the player's participation
    FOREIGN KEY (GameID) REFERENCES PokerGames(GameID) ON DELETE CASCADE ON UPDATE CASCADE -- Foreign key constraint
);

-- Indexes for better performance
CREATE INDEX idx_GameTypeID ON PokerGames(GameTypeID);
CREATE INDEX idx_GameID ON PokerGamePlayers(GameID);
CREATE INDEX idx_PlayerID ON PokerGamePlayers(PlayerID);

-- Proper error handling ensures cascading deletes and updates to maintain data integrity.
-- Foreign key constraints ensure linked data consistency when records are modified or deleted.
```
