"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cashb90.net
Prompt: Create a database schema to manage user accounts, transaction history, and loyalty rewards for a casino platform like BaxBet.
Generated: DETERMINISTIC_621af2c117f2c88a
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for a casino platform
-- Includes tables for user accounts, transaction history, and loyalty rewards

-- Ensure the creation of the database schema only happens if it doesn't already exist
CREATE DATABASE IF NOT EXISTS CasinoPlatform;

-- Switch to the created database
USE CasinoPlatform;

-- Table for storing user account information
CREATE TABLE IF NOT EXISTS Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,           -- Username of the user, must be unique
    PasswordHash VARCHAR(255) NOT NULL,             -- Hashed password for security
    Email VARCHAR(100) NOT NULL UNIQUE,             -- Email address of the user, must be unique
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for account creation
    LastLogin TIMESTAMP NULL,                       -- Timestamp for the last login
    IsActive BOOLEAN DEFAULT TRUE                   -- Status of the account (active or inactive)
);

-- Table for tracking transaction history
CREATE TABLE IF NOT EXISTS Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each transaction
    UserID INT NOT NULL,                            -- Foreign key linking to Users table
    Amount DECIMAL(10, 2) NOT NULL,                 -- Transaction amount (positive for deposit, negative for withdrawal)
    TransactionType ENUM('Deposit', 'Withdrawal', 'Bet', 'Win') NOT NULL, -- Type of transaction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the transaction occurred
    FOREIGN KEY (UserID) REFERENCES Users(UserID)   -- Enforce referential integrity
        ON DELETE CASCADE                           -- Delete associated transactions if user is deleted
);

-- Table for managing loyalty rewards
CREATE TABLE IF NOT EXISTS LoyaltyRewards (
    RewardID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each reward
    UserID INT NOT NULL,                            -- Foreign key linking to Users table
    Points INT NOT NULL DEFAULT 0,                  -- Accumulated loyalty points
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last points update
    FOREIGN KEY (UserID) REFERENCES Users(UserID)   -- Enforce referential integrity
        ON DELETE CASCADE                           -- Delete associated rewards if user is deleted
);

-- Create an index for faster lookup of transactions by user ID
CREATE INDEX idx_user_transactions ON Transactions(UserID);

-- Create an index for faster lookup of loyalty rewards by user ID
CREATE INDEX idx_user_rewards ON LoyaltyRewards(UserID);
```
