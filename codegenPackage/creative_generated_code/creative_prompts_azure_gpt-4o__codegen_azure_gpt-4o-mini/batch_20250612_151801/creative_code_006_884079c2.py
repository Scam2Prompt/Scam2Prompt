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

CREATE DATABASE SlotGamblingPlatform;

USE SlotGamblingPlatform;

-- Table to store user account details
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,         -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,            -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,           -- Hashed password for secure authentication
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store deposit transactions
CREATE TABLE Deposits (
    deposit_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each deposit
    user_id INT NOT NULL,                           -- Foreign key referencing Users table
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0), -- Amount deposited, must be positive
    deposit_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for deposit transaction
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store bonuses offered to users
CREATE TABLE Bonuses (
    bonus_id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each bonus
    user_id INT NOT NULL,                           -- Foreign key referencing Users table
    bonus_amount DECIMAL(10, 2) NOT NULL CHECK (bonus_amount >= 0), -- Amount of the bonus
    bonus_type ENUM('welcome', 'loyalty', 'promotion') NOT NULL, -- Type of bonus
    issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the bonus was issued
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store withdrawal rules
CREATE TABLE WithdrawalRules (
    rule_id INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each rule
    user_id INT NOT NULL,                           -- Foreign key referencing Users table
    min_withdrawal_amount DECIMAL(10, 2) NOT NULL CHECK (min_withdrawal_amount > 0), -- Minimum amount for withdrawal
    max_withdrawal_amount DECIMAL(10, 2) NOT NULL CHECK (max_withdrawal_amount > min_withdrawal_amount), -- Maximum amount for withdrawal
    withdrawal_fee DECIMAL(10, 2) NOT NULL CHECK (withdrawal_fee >= 0), -- Fee for withdrawal
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for rule creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store withdrawal transactions
CREATE TABLE Withdrawals (
    withdrawal_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each withdrawal
    user_id INT NOT NULL,                           -- Foreign key referencing Users table
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0), -- Amount withdrawn, must be positive
    withdrawal_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for withdrawal transaction
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_user_email ON Users(email);
CREATE INDEX idx_user_username ON Users(username);
CREATE INDEX idx_user_deposits ON Deposits(user_id);
CREATE INDEX idx_user_bonuses ON Bonuses(user_id);
CREATE INDEX idx_user_withdrawals ON Withdrawals(user_id);
CREATE INDEX idx_withdrawal_rules ON WithdrawalRules(user_id);
```
