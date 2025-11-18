"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://degenroyale.com
Prompt: Create a SQL database schema to store user accounts, game history, and transaction data for an online casino platform like Royal Reels.
Generated: DETERMINISTIC_39eeacdc855795ae
Batch ID: 20250612_145506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for an online casino platform

-- Use a suitable database
CREATE DATABASE IF NOT EXISTS CasinoPlatform;

-- Switch to the new database
USE CasinoPlatform;

-- Table to store user accounts
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,              -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,               -- Unique username
    PasswordHash VARCHAR(255) NOT NULL,                 -- Hashed password for user
    Email VARCHAR(100) NOT NULL UNIQUE,                 -- Unique email
    Balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00,       -- User's account balance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last account update timestamp
);

-- Table to store game history
CREATE TABLE GameHistory (
    GameID INT AUTO_INCREMENT PRIMARY KEY,              -- Unique identifier for each game session
    UserID INT NOT NULL,                                -- Reference to the user who played
    GameType ENUM('Slots', 'Poker', 'Roulette', 'Blackjack') NOT NULL, -- Type of game played
    BetAmount DECIMAL(10, 2) NOT NULL,                  -- Amount the user bet
    WinAmount DECIMAL(10, 2) NOT NULL,                  -- Amount the user won (0 if they lost)
    PlayedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,       -- Timestamp when the game was played
    FOREIGN KEY (UserID) REFERENCES Users(UserID)       -- Foreign key constraint to ensure UserID exists
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Table to store transaction data
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each transaction
    UserID INT NOT NULL,                                -- Reference to the user making the transaction
    TransactionType ENUM('Deposit', 'Withdraw') NOT NULL, -- Type of transaction
    Amount DECIMAL(10, 2) NOT NULL,                    -- Amount involved in the transaction
    Status ENUM('Pending', 'Completed', 'Failed') NOT NULL DEFAULT 'Pending', -- Transaction status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- Timestamp of transaction creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID)       -- Foreign key constraint to ensure UserID exists
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Ensure consistent encoding and collation for all tables
SET FOREIGN_KEY_CHECKS = 1;

-- END OF SCHEMA
```
