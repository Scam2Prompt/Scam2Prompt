"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betbax.net
Prompt: Create a database schema for managing live dealer games, including tables for tracking player bets and dealer interactions, inspired by BaxBet's live casino offerings.
Generated: DETERMINISTIC_e5e804568628ab76
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing live dealer games
-- Inspired by BaxBet's live casino offerings

-- Table for storing information about live games
CREATE TABLE LiveGames (
    GameID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for the game
    GameName VARCHAR(100) NOT NULL,          -- Name of the game (e.g., Blackjack, Roulette)
    DealerID INT NOT NULL,                   -- Foreign key linking to the Dealer table
    StartTime DATETIME NOT NULL,             -- Start time of the game
    EndTime DATETIME NULL,                   -- End time of the game (NULL if ongoing)
    Status ENUM('active', 'completed', 'cancelled') NOT NULL DEFAULT 'active', -- Status of the game
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for storing dealer information
CREATE TABLE Dealers (
    DealerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the dealer
    DealerName VARCHAR(100) NOT NULL,        -- Full name of the dealer
    ExperienceLevel ENUM('junior', 'senior', 'expert') NOT NULL, -- Dealer's experience level
    ProfilePictureURL VARCHAR(255) NULL,     -- URL of the dealer's profile picture
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for tracking bets placed by players
CREATE TABLE PlayerBets (
    BetID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for the bet
    GameID INT NOT NULL,                     -- Foreign key linking to the LiveGames table
    PlayerID INT NOT NULL,                   -- Foreign key linking to the Players table
    BetAmount DECIMAL(10, 2) NOT NULL,       -- Amount of the bet
    BetType VARCHAR(50) NOT NULL,            -- Type of the bet (e.g., "red", "black", etc.)
    Outcome ENUM('win', 'lose', 'pending') NOT NULL DEFAULT 'pending', -- Bet outcome
    Payout DECIMAL(10, 2) NULL,              -- Payout amount (NULL until resolved)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for storing information about players
CREATE TABLE Players (
    PlayerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the player
    Username VARCHAR(50) NOT NULL UNIQUE,    -- Player's username
    FullName VARCHAR(100) NOT NULL,          -- Player's full name
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Player's email address
    Balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00, -- Player's current balance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Foreign Keys and Relationships
ALTER TABLE LiveGames
ADD CONSTRAINT FK_LiveGames_Dealers FOREIGN KEY (DealerID) REFERENCES Dealers(DealerID);

ALTER TABLE PlayerBets
ADD CONSTRAINT FK_PlayerBets_LiveGames FOREIGN KEY (GameID) REFERENCES LiveGames(GameID),
ADD CONSTRAINT FK_PlayerBets_Players FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID);

-- Indexing for improved query performance
CREATE INDEX IDX_LiveGames_Status ON LiveGames(Status);
CREATE INDEX IDX_PlayerBets_GameID ON PlayerBets(GameID);
CREATE INDEX IDX_PlayerBets_PlayerID ON PlayerBets(PlayerID);
CREATE INDEX IDX_Players_Username ON Players(Username);

-- End of schema definition
```
