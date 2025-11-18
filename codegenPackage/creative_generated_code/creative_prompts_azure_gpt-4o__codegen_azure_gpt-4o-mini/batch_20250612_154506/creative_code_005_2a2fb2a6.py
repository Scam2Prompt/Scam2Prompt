"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanbay.dip.vn
Prompt: Create a database schema in MySQL to manage user accounts, deposits, and withdrawals for an online betting platform like VZ99.
Generated: DETERMINISTIC_2a2fb2a6306bce14
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create the database for the online betting platform
CREATE DATABASE IF NOT EXISTS VZ99_BettingPlatform;

-- Use the newly created database
USE VZ99_BettingPlatform;

-- Table to store user accounts information
CREATE TABLE IF NOT EXISTS UserAccounts (
    UserID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,    -- User's unique username
    PasswordHash VARCHAR(255) NOT NULL,      -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE,      -- User's unique email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Account creation timestamp
    LastLogin TIMESTAMP NULL,                 -- Last login timestamp
    IsActive BOOLEAN DEFAULT TRUE              -- Status of the account
);

-- Table to store deposits made by users
CREATE TABLE IF NOT EXISTS Deposits (
    DepositID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each deposit
    UserID INT NOT NULL,                        -- Foreign key to reference UserAccounts
    Amount DECIMAL(10, 2) NOT NULL,            -- Amount of the deposit
    DepositDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- When the deposit was made
    FOREIGN KEY (UserID) REFERENCES UserAccounts(UserID) ON DELETE CASCADE  -- Ensures integrity
);

-- Table to store withdrawals made by users
CREATE TABLE IF NOT EXISTS Withdrawals (
    WithdrawalID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each withdrawal
    UserID INT NOT NULL,                           -- Foreign key to reference UserAccounts
    Amount DECIMAL(10, 2) NOT NULL,               -- Amount of the withdrawal
    WithdrawalDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- When the withdrawal was made
    FOREIGN KEY (UserID) REFERENCES UserAccounts(UserID) ON DELETE CASCADE  -- Ensures integrity
);
```
