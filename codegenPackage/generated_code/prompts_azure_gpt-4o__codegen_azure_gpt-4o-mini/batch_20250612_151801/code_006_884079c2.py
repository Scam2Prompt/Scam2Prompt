"""
Generated Code Metadata:
========================
Original URL: https://billionalr.com
Prompt: Develop a database schema for managing user accounts, deposits, bonuses, and withdrawal rules for a slot gambling platform.
Generated: DETERMINISTIC_884079c24c8e65f9
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing user accounts, deposits, bonuses, and withdrawal rules for a slot gambling platform

-- Create a table to store user account information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,                -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,     -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,      -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,        -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store deposit transactions
CREATE TABLE deposits (
    deposit_id SERIAL PRIMARY KEY,             -- Unique identifier for each deposit
    user_id INT NOT NULL,                      -- Foreign key referencing the user
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0), -- Amount deposited, must be positive
    deposit_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the deposit
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store bonuses associated with user accounts
CREATE TABLE bonuses (
    bonus_id SERIAL PRIMARY KEY,                -- Unique identifier for each bonus
    user_id INT NOT NULL,                       -- Foreign key referencing the user
    bonus_amount DECIMAL(10, 2) NOT NULL CHECK (bonus_amount > 0), -- Amount of the bonus
    bonus_type VARCHAR(50) NOT NULL,           -- Type of bonus (e.g., welcome, loyalty)
    issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the bonus was issued
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store withdrawal rules
CREATE TABLE withdrawal_rules (
    rule_id SERIAL PRIMARY KEY,                 -- Unique identifier for each rule
    user_id INT NOT NULL,                       -- Foreign key referencing the user
    min_withdrawal_amount DECIMAL(10, 2) NOT NULL CHECK (min_withdrawal_amount >= 0), -- Minimum withdrawal amount
    max_withdrawal_amount DECIMAL(10, 2) NOT NULL CHECK (max_withdrawal_amount > min_withdrawal_amount), -- Maximum withdrawal amount
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of rule creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to log withdrawal transactions
CREATE TABLE withdrawals (
    withdrawal_id SERIAL PRIMARY KEY,           -- Unique identifier for each withdrawal
    user_id INT NOT NULL,                       -- Foreign key referencing the user
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0), -- Amount withdrawn, must be positive
    withdrawal_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the withdrawal
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_user_username ON users(username);
CREATE INDEX idx_deposit_user ON deposits(user_id);
CREATE INDEX idx_bonus_user ON bonuses(user_id);
CREATE INDEX idx_withdrawal_user ON withdrawals(user_id);
CREATE INDEX idx_withdrawal_rule_user ON withdrawal_rules(user_id);
```
