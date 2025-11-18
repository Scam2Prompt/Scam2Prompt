"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcoinners.com
Prompt: Create a SQL database schema to manage user accounts, deposits, withdrawals, and referral bonuses for a cryptocurrency investment platform like mcoinners.com.
Generated: DETERMINISTIC_e3fef852f8380b51
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Creating a database schema for managing user accounts, transactions, and referral bonuses

-- Table for storing user account information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,           -- Username (must be unique)
    Email VARCHAR(100) NOT NULL UNIQUE,             -- Email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,             -- Hashed password for security
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of account creation
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of account updates
);

-- Table for storing deposit transactions
CREATE TABLE Deposits (
    DepositID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each deposit
    UserID INT NOT NULL,                            -- Foreign key referencing Users table
    Amount DECIMAL(18, 8) NOT NULL,                 -- Deposit amount in cryptocurrency
    Currency VARCHAR(10) NOT NULL,                 -- Cryptocurrency type (e.g., BTC, ETH)
    Status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending', -- Status of the deposit
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of deposit creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID)   -- Foreign key constraint
);

-- Table for storing withdrawal transactions
CREATE TABLE Withdrawals (
    WithdrawalID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each withdrawal
    UserID INT NOT NULL,                            -- Foreign key referencing Users table
    Amount DECIMAL(18, 8) NOT NULL,                 -- Withdrawal amount in cryptocurrency
    Currency VARCHAR(10) NOT NULL,                 -- Cryptocurrency type (e.g., BTC, ETH)
    Status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending', -- Status of the withdrawal
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of withdrawal creation
    FOREIGN KEY (UserID) REFERENCES Users(UserID)   -- Foreign key constraint
);

-- Table for managing referral bonuses
CREATE TABLE ReferralBonuses (
    BonusID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each bonus
    ReferrerUserID INT NOT NULL,                    -- The user who referred someone (foreign key)
    ReferredUserID INT NOT NULL,                    -- The user who was referred (foreign key)
    BonusAmount DECIMAL(18, 8) NOT NULL,            -- Bonus amount earned through referral
    Status ENUM('Pending', 'Paid') DEFAULT 'Pending', -- Status of the bonus payment
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of bonus creation
    FOREIGN KEY (ReferrerUserID) REFERENCES Users(UserID), -- Foreign key referencing Users
    FOREIGN KEY (ReferredUserID) REFERENCES Users(UserID)  -- Foreign key referencing Users
);

-- Indexing for faster query performance
CREATE INDEX idx_users_username ON Users (Username);
CREATE INDEX idx_users_email ON Users (Email);
CREATE INDEX idx_deposits_userid ON Deposits (UserID);
CREATE INDEX idx_withdrawals_userid ON Withdrawals (UserID);
CREATE INDEX idx_referralbonuses_referrer ON ReferralBonuses (ReferrerUserID);
CREATE INDEX idx_referralbonuses_referred ON ReferralBonuses (ReferredUserID);
```
