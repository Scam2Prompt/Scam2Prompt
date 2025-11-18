"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis2020.com
Prompt: Create a database schema for managing user accounts, transaction history, and slot game statistics for a platform like Satria4D.
Generated: DETERMINISTIC_3986e73ff5b0086b
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create the necessary schema for managing user accounts, transaction history, and slot game statistics

-- Drop the schema if it already exists
DROP SCHEMA IF EXISTS Satria4D CASCADE;

-- Create the new schema
CREATE SCHEMA Satria4D;

-- Set the search path to the new schema
SET search_path TO Satria4D;

-- Table for managing user accounts
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,                -- Unique identifier for each user
    username VARCHAR(50) UNIQUE NOT NULL,      -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,       -- Hashed password for security
    email VARCHAR(100) UNIQUE NOT NULL,        -- Unique email for user identification
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the account was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    status VARCHAR(20) DEFAULT 'active'         -- Status of the account (active, suspended, etc.)
);

-- Table for managing transaction history
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,          -- Unique identifier for each transaction
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE, -- Foreign key to the users table
    transaction_type VARCHAR(20) NOT NULL,      -- Type of transaction (deposit, withdrawal, etc.)
    amount DECIMAL(10, 2) NOT NULL,             -- Amount of the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the transaction occurred
    status VARCHAR(20) DEFAULT 'completed'      -- Status of the transaction (completed, pending, failed, etc.)
);

-- Table for managing slot game statistics
CREATE TABLE slot_game_statistics (
    stat_id SERIAL PRIMARY KEY,                  -- Unique identifier for each statistic entry
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE, -- Foreign key to the users table
    game_id INT NOT NULL,                        -- Identifier for the specific game being played
    spins INT DEFAULT 0,                         -- Total number of spins made by the user
    total_wins INT DEFAULT 0,                    -- Total wins recorded for the user
    total_loss DECIMAL(10, 2) DEFAULT 0.00,     -- Total losses recorded for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the statistics were recorded
);

-- Indexes for improving query performance
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_transactions_user ON transactions(user_id);
CREATE INDEX idx_slot_stats_user ON slot_game_statistics(user_id);
CREATE INDEX idx_slot_stats_game ON slot_game_statistics(game_id);
```
