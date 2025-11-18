"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.uhcstepup.com
Prompt: Create a database schema for tracking player statistics and game outcomes for a slot game platform like Slot138, focusing on features of Slot Thailand.
Generated: DETERMINISTIC_533f9f85b846b23c
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking player statistics and game outcomes
-- Slot Game Platform: Slot138 with features focusing on Slot Thailand

-- Table to store player information
CREATE TABLE Players (
    PlayerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each player
    Username VARCHAR(50) NOT NULL UNIQUE,    -- Unique username for the player
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Email for player communication
    PasswordHash VARCHAR(255) NOT NULL,      -- Hashed password for security
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the player registered
    Country VARCHAR(50) DEFAULT 'Thailand',  -- Default country set to Thailand
    IsActive BOOLEAN DEFAULT TRUE,           -- Flag to indicate if the player is active
    LastLogin TIMESTAMP NULL                 -- Timestamp of the last login
);

-- Table to store game information
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each game
    GameName VARCHAR(100) NOT NULL,          -- Name of the slot game
    Provider VARCHAR(100) NOT NULL,          -- Game provider (e.g., Pragmatic, Microgaming)
    RTP DECIMAL(5, 2) NOT NULL,              -- Return-to-Player percentage
    Volatility VARCHAR(50) NOT NULL,         -- Volatility level (e.g., Low, Medium, High)
    MaxWin DECIMAL(15, 2) NOT NULL,          -- Maximum possible win amount
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the game was added
);

-- Table to track outcomes of each game session
CREATE TABLE GameSessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the session
    PlayerID INT NOT NULL,                    -- Foreign key referencing Players table
    GameID INT NOT NULL,                      -- Foreign key referencing Games table
    BetAmount DECIMAL(15, 2) NOT NULL,        -- Amount bet by the player
    WinAmount DECIMAL(15, 2) NOT NULL,        -- Amount won by the player
    SpinCount INT NOT NULL DEFAULT 0,         -- Total number of spins in the session
    StartTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the session started
    EndTime TIMESTAMP NULL,                   -- When the session ended
    IsBonusTriggered BOOLEAN DEFAULT FALSE,   -- Flag for triggering bonus rounds
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID) ON DELETE CASCADE,
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE
);

-- Table to store player statistics
CREATE TABLE PlayerStatistics (
    PlayerID INT PRIMARY KEY,                   -- Foreign key referencing Players table
    TotalBets DECIMAL(20, 2) DEFAULT 0,         -- Total amount bet by the player
    TotalWins DECIMAL(20, 2) DEFAULT 0,         -- Total amount won by the player
    TotalSpins INT DEFAULT 0,                   -- Total number of spins by the player
    BigWins INT DEFAULT 0,                      -- Count of big wins (e.g., wins exceeding 1000x bet)
    LastGamePlayed INT NULL,                    -- Foreign key referencing Games table
    LastPlayedAt TIMESTAMP NULL,                -- Timestamp of the last game played
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID) ON DELETE CASCADE,
    FOREIGN KEY (LastGamePlayed) REFERENCES Games(GameID) ON DELETE SET NULL
);

-- Table to log errors or unexpected outcomes for auditing purposes
CREATE TABLE ErrorLogs (
    ErrorID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for the error
    PlayerID INT NULL,                         -- Foreign key referencing Players table, if applicable
    GameID INT NULL,                           -- Foreign key referencing Games table, if applicable
    ErrorMessage TEXT NOT NULL,                -- Description of the error
    OccurredAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the error occurred
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID) ON DELETE SET NULL,
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE SET NULL
);

-- Indexes to improve query performance
CREATE INDEX idx_player_statistics_total_bets ON PlayerStatistics (TotalBets);
CREATE INDEX idx_game_sessions_start_time ON GameSessions (StartTime);
CREATE INDEX idx_games_provider ON Games (Provider);

-- Triggers to automatically update player statistics after each game session
DELIMITER $$
CREATE TRIGGER after_game_session_insert
AFTER INSERT ON GameSessions
FOR EACH ROW
BEGIN
    -- Update total bets, total wins, and total spins for the player
    UPDATE PlayerStatistics 
    SET 
        TotalBets = TotalBets + NEW.BetAmount,
        TotalWins = TotalWins + NEW.WinAmount,
        TotalSpins = TotalSpins + NEW.SpinCount,
        LastGamePlayed = NEW.GameID,
        LastPlayedAt = NEW.EndTime
    WHERE PlayerID = NEW.PlayerID;
    
    -- Increment big wins count if the win is significantly large (e.g., 1000x bet amount)
    IF NEW.WinAmount >= (NEW.BetAmount * 1000) THEN
        UPDATE PlayerStatistics 
        SET BigWins = BigWins + 1 
        WHERE PlayerID = NEW.PlayerID;
    END IF;
END$$
DELIMITER ;
```
