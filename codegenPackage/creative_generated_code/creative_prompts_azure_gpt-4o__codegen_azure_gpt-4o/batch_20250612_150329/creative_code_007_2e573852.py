"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzocash.com
Prompt: Create a database schema for tracking user investments, referrals, and transaction history, similar to the functionality described on Renzo Cash's platform.
Generated: DETERMINISTIC_2e573852beecde73
Batch ID: 20250612_150329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Tracking User Investments, Referrals, and Transaction History

-- Table: users
-- This table stores basic user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,                -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,      -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,        -- User's email address
    hashed_password VARCHAR(255) NOT NULL,     -- Hashed password for authentication
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for the last update to user details
);

-- Table: investments
-- This table tracks user investments
CREATE TABLE investments (
    investment_id SERIAL PRIMARY KEY,          -- Unique identifier for each investment
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE, -- Reference to the user
    amount DECIMAL(15, 2) NOT NULL,            -- Amount invested
    investment_type VARCHAR(50) NOT NULL,     -- Type of investment (e.g., stocks, bonds, crypto)
    investment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of investment
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for the last update to the investment
);

-- Table: referrals
-- This table tracks user referrals
CREATE TABLE referrals (
    referral_id SERIAL PRIMARY KEY,            -- Unique identifier for each referral
    referrer_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE, -- Referring user
    referred_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE, -- Referred user
    referral_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date of referral
);

-- Table: transactions
-- This table tracks transaction history for users
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,         -- Unique identifier for each transaction
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE, -- Reference to the user
    transaction_type VARCHAR(50) NOT NULL,    -- Type of transaction (e.g., deposit, withdrawal, transfer)
    amount DECIMAL(15, 2) NOT NULL,           -- Amount in the transaction
    status VARCHAR(20) NOT NULL,              -- Status of the transaction (e.g., pending, completed, failed)
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of transaction
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for the last update to the transaction
);

-- Indexes for improving query performance
CREATE INDEX idx_user_investments ON investments(user_id);
CREATE INDEX idx_user_transactions ON transactions(user_id);
CREATE INDEX idx_referrals_referrer ON referrals(referrer_id);
CREATE INDEX idx_referrals_referred ON referrals(referred_id);

-- Example constraints for data integrity
ALTER TABLE referrals 
ADD CONSTRAINT check_referral_self_reference CHECK (referrer_id != referred_id); -- Prevent users from referring themselves

-- End of schema
```
