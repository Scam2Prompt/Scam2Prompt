"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finveracapitals.com
Prompt: Suggest a secure database schema for storing user investment details, referral commissions, and withdrawal transactions, inspired by Finvera Capitals' features.
Generated: DETERMINISTIC_766b8cc8df7d482d
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing user investment details, referral commissions, and withdrawal transactions

CREATE DATABASE IF NOT EXISTS FinTechDB;

USE FinTechDB;

-- Table to store user details
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,         -- Unique username for login
    email VARCHAR(100) NOT NULL UNIQUE,            -- Unique email address for notifications
    password_hash VARCHAR(255) NOT NULL,           -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Table to store investment details
CREATE TABLE Investments (
    investment_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each investment
    user_id INT NOT NULL,                           -- Foreign key to Users table
    investment_amount DECIMAL(10, 2) NOT NULL,     -- Amount invested
    investment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of investment
    investment_type ENUM('stocks', 'bonds', 'real estate', 'crypto') NOT NULL, -- Type of investment
    status ENUM('active', 'withdrawn', 'closed') DEFAULT 'active', -- Status of investment
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Cascading delete on user removal
);

-- Table to store referral commissions
CREATE TABLE ReferralCommissions (
    commission_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each commission
    referrer_id INT NOT NULL,                        -- User ID of the referrer
    referred_user_id INT NOT NULL,                   -- User ID of the referred user
    commission_amount DECIMAL(10, 2) NOT NULL,      -- Amount of commission earned
    commission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of commission generation
    FOREIGN KEY (referrer_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Cascading delete on user removal
    FOREIGN KEY (referred_user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Cascading delete on user removal
);

-- Table to store withdrawal transactions
CREATE TABLE Withdrawals (
    withdrawal_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each withdrawal
    user_id INT NOT NULL,                             -- Foreign key to Users table
    withdrawal_amount DECIMAL(10, 2) NOT NULL,       -- Amount to withdraw
    withdrawal_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of withdrawal
    status ENUM('pending', 'completed', 'failed') DEFAULT 'pending', -- Status of withdrawal
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Cascading delete on user removal
);

-- Indexes for performance improvement
CREATE INDEX idx_user_email ON Users(email);
CREATE INDEX idx_investment_user ON Investments(user_id);
CREATE INDEX idx_commission_referrer ON ReferralCommissions(referrer_id);
CREATE INDEX idx_withdrawal_user ON Withdrawals(user_id);
```
