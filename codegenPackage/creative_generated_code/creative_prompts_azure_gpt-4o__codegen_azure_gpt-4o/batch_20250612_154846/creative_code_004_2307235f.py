"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tronlink.at
Prompt: Create a database schema for storing user information, transaction history, and game statistics for a gambling platform similar to VSO777.
Generated: DETERMINISTIC_2307235f5deed5e2
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Gambling Platform

-- Table for storing user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,       -- Username chosen by the user
    Email VARCHAR(100) NOT NULL UNIQUE,         -- User's email address
    PasswordHash VARCHAR(255) NOT NULL,         -- Hashed password for security
    DateOfBirth DATE NOT NULL,                  -- User's date of birth
    Country VARCHAR(50),                        -- User's country
    Balance DECIMAL(10, 2) DEFAULT 0.00,        -- User's account balance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table for storing transaction history
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL,                          -- FK to identify the user
    TransactionType ENUM('Deposit', 'Withdrawal', 'Bet', 'Win') NOT NULL, -- Type of transaction
    Amount DECIMAL(10, 2) NOT NULL,               -- Transaction amount
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the transaction happened
    Description VARCHAR(255),                     -- Optional description for the transaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) -- Link to Users table
);

-- Table for storing game statistics
CREATE TABLE GameStatistics (
    GameID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each game
    UserID INT NOT NULL,                         -- FK to associate stats with a user
    GameName VARCHAR(100) NOT NULL,              -- Name of the game played
    BetsPlaced INT DEFAULT 0,                    -- Number of bets placed by the user
    TotalAmountBet DECIMAL(10, 2) DEFAULT 0.00,  -- Total amount bet on the game
    TotalAmountWon DECIMAL(10, 2) DEFAULT 0.00,  -- Total amount won by the user in the game
    LastPlayed TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the game was last played
    FOREIGN KEY (UserID) REFERENCES Users(UserID) -- Link to Users table
);

-- Indexes to optimize performance
CREATE INDEX idx_username ON Users(Username);     -- Index for faster username lookups
CREATE INDEX idx_userid_transactions ON Transactions(UserID); -- Index for transaction lookups
CREATE INDEX idx_userid_game_statistics ON GameStatistics(UserID); -- Index for game statistics lookups

-- Error handling and constraints to ensure data integrity
ALTER TABLE Users ADD CONSTRAINT chk_balance_positive CHECK (Balance >= 0); -- Ensure balance cannot be negative
ALTER TABLE Transactions ADD CONSTRAINT chk_amount_positive CHECK (Amount > 0); -- Ensure transaction amount is positive
ALTER TABLE GameStatistics ADD CONSTRAINT chk_bets_positive CHECK (BetsPlaced >= 0); -- Ensure bet count is not negative
ALTER TABLE GameStatistics ADD CONSTRAINT chk_amounts_positive CHECK (TotalAmountBet >= 0 AND TotalAmountWon >= 0); -- Ensure amounts are non-negative
```
