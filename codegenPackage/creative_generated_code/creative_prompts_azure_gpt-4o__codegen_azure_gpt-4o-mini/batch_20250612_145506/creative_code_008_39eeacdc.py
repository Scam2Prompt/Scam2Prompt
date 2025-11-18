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
-- SQL Database Schema for an Online Casino Platform

-- Create a table to store user account information
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,   -- User's chosen username
    PasswordHash VARCHAR(255) NOT NULL,     -- Securely stored password hash
    Email VARCHAR(100) NOT NULL UNIQUE,     -- User's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Account creation timestamp
    LastLogin TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Last login timestamp
);

-- Create a table to store game history for each user
CREATE TABLE GameHistory (
    GameID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each game record
    UserID INT NOT NULL,                     -- Foreign key referencing Users table
    GameName VARCHAR(100) NOT NULL,         -- Name of the game played
    BetAmount DECIMAL(10, 2) NOT NULL,      -- Amount bet by the user
    WinAmount DECIMAL(10, 2) DEFAULT 0.00,  -- Amount won by the user
    PlayedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the game was played
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table to store transaction data for deposits and withdrawals
CREATE TABLE Transactions (
    TransactionID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each transaction
    UserID INT NOT NULL,                           -- Foreign key referencing Users table
    TransactionType ENUM('Deposit', 'Withdrawal') NOT NULL,  -- Type of transaction
    Amount DECIMAL(10, 2) NOT NULL,               -- Amount involved in the transaction
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of the transaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create an index on the Transactions table for faster lookup by UserID
CREATE INDEX idx_userid ON Transactions(UserID);

-- Create an index on the GameHistory table for faster lookup by UserID
CREATE INDEX idx_userid_history ON GameHistory(UserID);

-- Optional: Create a table to store user preferences or settings
CREATE TABLE UserSettings (
    UserID INT PRIMARY KEY,                -- Foreign key referencing Users table
    PreferredLanguage VARCHAR(20) DEFAULT 'English',  -- User's preferred language
    NotificationsEnabled BOOLEAN DEFAULT TRUE,         -- Notification preferences
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE  -- Ensures referential integrity
);
```
