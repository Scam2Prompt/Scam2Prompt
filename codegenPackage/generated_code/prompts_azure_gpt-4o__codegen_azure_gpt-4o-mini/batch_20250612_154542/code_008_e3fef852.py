"""
Generated Code Metadata:
========================
Original URL: https://mcoinners.com
Prompt: Create a SQL database schema to manage user accounts, deposits, withdrawals, and referral bonuses for a cryptocurrency investment platform like mcoinners.com.
Generated: DETERMINISTIC_e3fef852f8380b51
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Cryptocurrency Investment Platform

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ReferralBonuses;
DROP TABLE IF EXISTS Withdrawals;
DROP TABLE IF EXISTS Deposits;
DROP TABLE IF EXISTS Users;

-- Create Users table to store user account information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,                -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,     -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,        -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,       -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create Deposits table to track user deposits
CREATE TABLE Deposits (
    deposit_id SERIAL PRIMARY KEY,              -- Unique identifier for each deposit
    user_id INT NOT NULL,                       -- Foreign key referencing Users
    amount DECIMAL(18, 8) NOT NULL,             -- Amount deposited
    deposit_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of deposit
    status VARCHAR(20) DEFAULT 'pending',       -- Status of the deposit (e.g., pending, completed, failed)
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create Withdrawals table to track user withdrawals
CREATE TABLE Withdrawals (
    withdrawal_id SERIAL PRIMARY KEY,           -- Unique identifier for each withdrawal
    user_id INT NOT NULL,                       -- Foreign key referencing Users
    amount DECIMAL(18, 8) NOT NULL,             -- Amount withdrawn
    withdrawal_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of withdrawal
    status VARCHAR(20) DEFAULT 'pending',       -- Status of the withdrawal (e.g., pending, completed, failed)
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create ReferralBonuses table to manage referral bonuses
CREATE TABLE ReferralBonuses (
    bonus_id SERIAL PRIMARY KEY,                -- Unique identifier for each bonus
    referrer_id INT NOT NULL,                   -- Foreign key referencing Users (the referrer)
    referred_user_id INT NOT NULL,              -- Foreign key referencing Users (the referred user)
    bonus_amount DECIMAL(18, 8) NOT NULL,       -- Amount of the referral bonus
    bonus_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the bonus was awarded
    FOREIGN KEY (referrer_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (referred_user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_user_email ON Users(email);
CREATE INDEX idx_deposit_user ON Deposits(user_id);
CREATE INDEX idx_withdrawal_user ON Withdrawals(user_id);
CREATE INDEX idx_referral_referrer ON ReferralBonuses(referrer_id);
CREATE INDEX idx_referral_referred ON ReferralBonuses(referred_user_id);
```
