"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatangame.games
Prompt: Create a database schema for managing user accounts, loyalty programs, and cashback rewards in an online casino platform like BaxBet.
Generated: DETERMINISTIC_769d86743632f73d
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Online Casino Platform

-- Table to store user accounts
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,             -- Unique identifier for each user
    username VARCHAR(50) UNIQUE NOT NULL,   -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,    -- Hashed password for security
    email VARCHAR(100) UNIQUE NOT NULL,     -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    last_login TIMESTAMP,                   -- Last login timestamp
    is_active BOOLEAN DEFAULT TRUE          -- Indicates if the account is active
);

-- Table to manage loyalty programs
CREATE TABLE LoyaltyPrograms (
    program_id SERIAL PRIMARY KEY,          -- Unique identifier for each loyalty program
    program_name VARCHAR(50) NOT NULL,      -- Name of the loyalty program
    description TEXT,                       -- Detailed description of the program
    points_multiplier DECIMAL(5,2) NOT NULL DEFAULT 1.0, -- Points multiplier for bets
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Program creation timestamp
    is_active BOOLEAN DEFAULT TRUE          -- Indicates if the program is active
);

-- Table to track user participation in loyalty programs
CREATE TABLE UserLoyaltyPoints (
    user_id INT REFERENCES Users(user_id) ON DELETE CASCADE, -- User ID foreign key
    program_id INT REFERENCES LoyaltyPrograms(program_id) ON DELETE CASCADE, -- Program ID foreign key
    points_balance DECIMAL(10,2) DEFAULT 0.0, -- Current loyalty points balance
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Last update timestamp
    PRIMARY KEY (user_id, program_id)         -- Composite primary key
);

-- Table to manage cashback rewards
CREATE TABLE CashbackRewards (
    reward_id SERIAL PRIMARY KEY,           -- Unique identifier for each cashback reward
    user_id INT REFERENCES Users(user_id) ON DELETE CASCADE, -- User ID foreign key
    amount DECIMAL(10,2) NOT NULL,          -- Cashback reward amount
    issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the reward was issued
    is_claimed BOOLEAN DEFAULT FALSE        -- Indicates if the reward has been claimed
);

-- Table to log transactions related to loyalty points and cashback rewards
CREATE TABLE Transactions (
    transaction_id SERIAL PRIMARY KEY,      -- Unique identifier for each transaction
    user_id INT REFERENCES Users(user_id) ON DELETE CASCADE, -- User ID foreign key
    transaction_type VARCHAR(50) NOT NULL, -- Type of transaction (e.g., 'loyalty_points', 'cashback')
    amount DECIMAL(10,2) NOT NULL,         -- Amount of points or cashback involved
    description TEXT,                      -- Optional description of the transaction
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Transaction timestamp
);

-- Indexes to optimize queries
CREATE INDEX idx_user_loyalty_points_user_id ON UserLoyaltyPoints(user_id);
CREATE INDEX idx_cashback_rewards_user_id ON CashbackRewards(user_id);
CREATE INDEX idx_transactions_user_id ON Transactions(user_id);
```
