"""
Generated Code Metadata:
========================
Original URL: https://venez888.vip
Prompt: Design a database schema to store user information, game records, and transactions for an online casino website like venez888.
Generated: DETERMINISTIC_a1b858507a0ac0da
Batch ID: 20250622_211418
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online casino website

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address
    FullName VARCHAR(100),                 -- Full name of the user
    DateOfBirth DATE,                      -- Date of birth of the user
    Balance DECIMAL(10, 2) DEFAULT 0.00,   -- Current balance of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store game records
CREATE TABLE GameRecords (
    GameID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game record
    UserID INT NOT NULL,                   -- Foreign key referencing Users table
    GameType VARCHAR(50) NOT NULL,         -- Type of game played (e.g., poker, slots)
    BetAmount DECIMAL(10, 2) NOT NULL,     -- Amount bet by the user
    WinAmount DECIMAL(10, 2) NOT NULL,     -- Amount won by the user
    GameResult ENUM('WIN', 'LOSS', 'DRAW') NOT NULL, -- Result of the game
    PlayedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the game was played
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store transaction records
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL,                          -- Foreign key referencing Users table
    TransactionType ENUM('DEPOSIT', 'WITHDRAWAL') NOT NULL, -- Type of transaction
    Amount DECIMAL(10, 2) NOT NULL,               -- Transaction amount
    TransactionStatus ENUM('PENDING', 'COMPLETED', 'FAILED') NOT NULL, -- Status of the transaction
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_user_balance ON Users (Balance);
CREATE INDEX idx_game_user ON GameRecords (UserID);
CREATE INDEX idx_transaction_user ON Transactions (UserID);

-- Error handling and constraints
-- Ensure positive values for balance, bet amount, and transaction amount
ALTER TABLE Users ADD CONSTRAINT chk_balance_positive CHECK (Balance >= 0);
ALTER TABLE GameRecords ADD CONSTRAINT chk_bet_positive CHECK (BetAmount >= 0);
ALTER TABLE Transactions ADD CONSTRAINT chk_amount_positive CHECK (Amount >= 0);
```
