"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billionalr.com
Prompt: Develop a database schema for managing user accounts, deposits, bonuses, and withdrawal rules for a slot gambling platform.
Generated: DETERMINISTIC_884079c24c8e65f9
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing user accounts, deposits, bonuses, and withdrawal rules for a slot gambling platform

-- Users table: Stores information about user accounts
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,           -- Unique username for the user
    PasswordHash VARCHAR(255) NOT NULL,             -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE,             -- Unique email address
    DateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the account was created
    IsActive BOOLEAN DEFAULT TRUE,                  -- Indicates if the account is active
    Balance DECIMAL(10, 2) DEFAULT 0.00             -- Current balance of the user
);

-- Deposits table: Records all deposit transactions made by users
CREATE TABLE Deposits (
    DepositID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each deposit
    UserID INT NOT NULL,                            -- Foreign key referencing Users table
    Amount DECIMAL(10, 2) NOT NULL,                 -- Amount deposited
    DateDeposited TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of deposit
    Status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending', -- Status of the deposit
    FOREIGN KEY (UserID) REFERENCES Users(UserID)   -- Enforce relationship with Users table
);

-- Bonuses table: Records bonus information for users
CREATE TABLE Bonuses (
    BonusID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each bonus
    UserID INT NOT NULL,                            -- Foreign key referencing Users table
    BonusType ENUM('Free Spins', 'Deposit Match', 'Cashback') NOT NULL, -- Type of bonus
    BonusAmount DECIMAL(10, 2) NOT NULL,            -- Bonus amount awarded
    DateAwarded TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the bonus was awarded
    IsClaimed BOOLEAN DEFAULT FALSE,                -- Indicates if the bonus has been claimed
    FOREIGN KEY (UserID) REFERENCES Users(UserID)   -- Enforce relationship with Users table
);

-- WithdrawalRules table: Defines the rules for withdrawals
CREATE TABLE WithdrawalRules (
    RuleID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each withdrawal rule
    RuleDescription VARCHAR(255) NOT NULL,          -- Description of the rule
    MinWithdrawalAmount DECIMAL(10, 2) NOT NULL,    -- Minimum amount allowed for withdrawal
    MaxWithdrawalAmount DECIMAL(10, 2),             -- Maximum amount allowed for withdrawal
    AppliesToBonus BOOLEAN DEFAULT FALSE,           -- Indicates if the rule applies to bonus funds
    DateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date when the rule was created
);

-- Withdrawals table: Records all withdrawal transactions made by users
CREATE TABLE Withdrawals (
    WithdrawalID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each withdrawal
    UserID INT NOT NULL,                            -- Foreign key referencing Users table
    Amount DECIMAL(10, 2) NOT NULL,                 -- Amount withdrawn
    DateRequested TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of withdrawal request
    Status ENUM('Pending', 'Completed', 'Rejected') DEFAULT 'Pending', -- Status of the withdrawal
    FOREIGN KEY (UserID) REFERENCES Users(UserID)   -- Enforce relationship with Users table
);

-- Indexes to improve query performance
CREATE INDEX idx_user_balance ON Users (Balance);
CREATE INDEX idx_deposit_userid ON Deposits (UserID);
CREATE INDEX idx_bonus_userid ON Bonuses (UserID);
CREATE INDEX idx_withdrawal_userid ON Withdrawals (UserID);
```
