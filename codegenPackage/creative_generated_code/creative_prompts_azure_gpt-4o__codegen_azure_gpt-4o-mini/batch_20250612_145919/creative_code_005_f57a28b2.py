"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanplatform.bet
Prompt: Create a database schema for managing user accounts, game history, and transaction records for an online casino platform similar to BaxBet.
Generated: DETERMINISTIC_f57a28b296bcd844
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for an online casino platform

CREATE DATABASE IF NOT EXISTS OnlineCasino;

USE OnlineCasino;

-- Table to store user accounts
CREATE TABLE IF NOT EXISTS Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,          -- Unique username for login
    PasswordHash VARCHAR(255) NOT NULL,             -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE,             -- Unique email for notifications
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Account creation timestamp
    LastLogin TIMESTAMP,                            -- Last login timestamp
    IsActive BOOLEAN DEFAULT TRUE,                  -- Status of the account
    CONSTRAINT chk_email CHECK (Email LIKE '%_@__%.__%') -- Email format check
);

-- Table to store game history of users
CREATE TABLE IF NOT EXISTS GameHistory (
    GameHistoryID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for the game history record
    UserID INT NOT NULL,                             -- Foreign key for users
    GameType VARCHAR(50) NOT NULL,                  -- Type of game (e.g., slots, poker, etc.)
    BetAmount DECIMAL(10, 2) NOT NULL,              -- Amount bet by the user
    WinAmount DECIMAL(10, 2) DEFAULT 0.00,          -- Amount won by the user
    GameDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Date and time when the game was played
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store transaction records
CREATE TABLE IF NOT EXISTS Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each transaction
    UserID INT NOT NULL,                             -- Foreign key for users
    TransactionType ENUM('Deposit', 'Withdrawal') NOT NULL,  -- Type of transaction
    Amount DECIMAL(10, 2) NOT NULL,                  -- Transaction amount
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    Status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending', -- Status of the transaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Create indices for performance optimization
CREATE INDEX idx_username ON Users (Username);
CREATE INDEX idx_game_user ON GameHistory (UserID);
CREATE INDEX idx_transaction_user ON Transactions (UserID);
```
