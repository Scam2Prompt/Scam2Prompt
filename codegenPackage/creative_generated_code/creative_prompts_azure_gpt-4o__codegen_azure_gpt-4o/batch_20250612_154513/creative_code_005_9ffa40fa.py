"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://locinews.com
Prompt: Create a database schema for a betting platform inspired by Bet88, including tables for users, bets, payouts, and game results.
Generated: DETERMINISTIC_9ffa40fa3cdbc5f1
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for a Betting Platform

-- Table: Users
-- Stores information about the users of the betting platform.
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Username for the platform (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE,    -- User's email address (must be unique)
    Balance DECIMAL(10, 2) DEFAULT 0.00,   -- User's account balance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table: Games
-- Stores information about games available for betting.
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game
    GameName VARCHAR(100) NOT NULL,        -- Name of the game
    StartTime DATETIME NOT NULL,           -- Scheduled start time of the game
    EndTime DATETIME,                      -- Scheduled end time (can be NULL if not ended yet)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of game creation
);

-- Table: Bets
-- Stores information about bets placed by users.
CREATE TABLE Bets (
    BetID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each bet
    UserID INT NOT NULL,                  -- Foreign key referencing Users(UserID)
    GameID INT NOT NULL,                  -- Foreign key referencing Games(GameID)
    BetAmount DECIMAL(10, 2) NOT NULL,    -- Amount of money placed on the bet
    BetType VARCHAR(50) NOT NULL,         -- Type/category of the bet (e.g., win, score, etc.)
    Odds DECIMAL(5, 2) NOT NULL,          -- Odds associated with the bet
    Status ENUM('Pending', 'Won', 'Lost') DEFAULT 'Pending', -- Status of the bet
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of bet creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE
);

-- Table: GameResults
-- Stores the results of games after completion.
CREATE TABLE GameResults (
    ResultID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game result
    GameID INT NOT NULL,                     -- Foreign key referencing Games(GameID)
    ResultDetails JSON NOT NULL,             -- JSON object containing detailed results (e.g., scores)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of result creation
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE
);

-- Table: Payouts
-- Stores information about payouts issued to users.
CREATE TABLE Payouts (
    PayoutID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payout
    UserID INT NOT NULL,                     -- Foreign key referencing Users(UserID)
    BetID INT NOT NULL,                      -- Foreign key referencing Bets(BetID)
    PayoutAmount DECIMAL(10, 2) NOT NULL,    -- Amount paid out to the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of payout creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (BetID) REFERENCES Bets(BetID) ON DELETE CASCADE
);

-- Indexes
-- Adding indexes for better query performance on frequently searched columns.
CREATE INDEX idx_user_balance ON Users(Balance);
CREATE INDEX idx_game_start_time ON Games(StartTime);
CREATE INDEX idx_bet_status ON Bets(Status);

-- Error handling and constraints
-- Ensure proper constraints to maintain data integrity.
ALTER TABLE Users ADD CONSTRAINT chk_balance_positive CHECK (Balance >= 0);
ALTER TABLE Bets ADD CONSTRAINT chk_bet_amount_positive CHECK (BetAmount > 0);
ALTER TABLE Payouts ADD CONSTRAINT chk_payout_amount_positive CHECK (PayoutAmount > 0);
```
