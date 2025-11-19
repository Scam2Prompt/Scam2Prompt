"""
Generated Code Metadata:
========================
Original URL: https://dromhusab.se
Prompt: "Design a database schema for an online casino platform, including tables for users, games, transactions, and bonuses, inspired by sites like Vulkan Vegas."
Generated: DETERMINISTIC_8ae20917dc018840
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Online Casino Platform

-- Table: Users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    Balance DECIMAL(10, 2) DEFAULT 0.00,   -- User's account balance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table: Games
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game
    Name VARCHAR(100) NOT NULL,            -- Name of the game
    Description TEXT,                      -- Description of the game
    MinBet DECIMAL(10, 2) NOT NULL,        -- Minimum bet amount
    MaxBet DECIMAL(10, 2) NOT NULL,        -- Maximum bet amount
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Game creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table: Transactions
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL,                          -- Reference to the user making the transaction
    Amount DECIMAL(10, 2) NOT NULL,               -- Transaction amount (positive for deposit, negative for withdrawal)
    TransactionType ENUM('Deposit', 'Withdrawal', 'Bet', 'Win') NOT NULL, -- Type of transaction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Transaction timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table: Bonuses
CREATE TABLE Bonuses (
    BonusID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each bonus
    UserID INT NOT NULL,                    -- Reference to the user receiving the bonus
    BonusType ENUM('Welcome', 'Deposit', 'Loyalty') NOT NULL, -- Type of bonus
    Amount DECIMAL(10, 2) NOT NULL,         -- Bonus amount
    IsActive BOOLEAN DEFAULT TRUE,         -- Whether the bonus is active
    ExpiryDate DATE,                        -- Expiration date of the bonus
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Bonus creation timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Foreign key constraint
);

-- Indexes for performance optimization
CREATE INDEX idx_users_email ON Users(Email);
CREATE INDEX idx_transactions_userid ON Transactions(UserID);
CREATE INDEX idx_bonuses_userid ON Bonuses(UserID);
```
