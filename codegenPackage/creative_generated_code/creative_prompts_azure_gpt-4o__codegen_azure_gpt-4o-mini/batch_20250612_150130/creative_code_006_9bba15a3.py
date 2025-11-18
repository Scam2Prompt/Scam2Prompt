"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://epiccoin-miners.ltd
Prompt: Create a database schema to manage user accounts, deposits, withdrawals, and referral bonuses for an investment platform similar to epiccoin-miners.ltd.
Generated: DETERMINISTIC_9bba15a3666bb17e
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for managing user accounts, deposits, withdrawals, and referral bonuses

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS referral_bonuses;
DROP TABLE IF EXISTS withdrawals;
DROP TABLE IF EXISTS deposits;
DROP TABLE IF EXISTS users;

-- Table to store user accounts information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last account update
);

-- Table to track deposits made by users
CREATE TABLE deposits (
    deposit_id SERIAL PRIMARY KEY,         -- Unique identifier for each deposit
    user_id INT NOT NULL,                  -- Foreign key referencing the user
    amount DECIMAL(10, 2) NOT NULL,       -- Amount deposited
    deposit_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the deposit
    status VARCHAR(20) DEFAULT 'pending',  -- Status of the deposit (e.g., pending, completed, failed)
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures deposits are deleted if user is deleted
);

-- Table to track withdrawals made by users
CREATE TABLE withdrawals (
    withdrawal_id SERIAL PRIMARY KEY,     -- Unique identifier for each withdrawal
    user_id INT NOT NULL,                 -- Foreign key referencing the user
    amount DECIMAL(10, 2) NOT NULL,      -- Amount withdrawn
    withdrawal_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the withdrawal
    status VARCHAR(20) DEFAULT 'pending', -- Status of the withdrawal (e.g., pending, completed, failed)
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures withdrawals are deleted if user is deleted
);

-- Table to manage referral bonuses for users
CREATE TABLE referral_bonuses (
    bonus_id SERIAL PRIMARY KEY,           -- Unique identifier for each bonus
    referrer_id INT NOT NULL,              -- Foreign key referencing the referring user
    referred_user_id INT NOT NULL,         -- Foreign key referencing the referred user
    bonus_amount DECIMAL(10, 2) NOT NULL, -- Amount of the referral bonus
    bonus_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the bonus issuance
    FOREIGN KEY (referrer_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Ensures bonuses are deleted if the referrer is deleted
    FOREIGN KEY (referred_user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures bonuses are deleted if the referred user is deleted
);

-- Indexes for improving query performance
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_deposits_user_id ON deposits(user_id);
CREATE INDEX idx_withdrawals_user_id ON withdrawals(user_id);
CREATE INDEX idx_referral_bonuses_referrer_id ON referral_bonuses(referrer_id);
CREATE INDEX idx_referral_bonuses_referred_user_id ON referral_bonuses(referred_user_id);
```
