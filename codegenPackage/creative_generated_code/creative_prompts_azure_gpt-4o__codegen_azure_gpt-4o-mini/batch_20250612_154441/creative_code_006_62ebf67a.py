"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethopt.io
Prompt: Create a database schema for managing diverse casino games, user accounts, and transaction histories for a platform like 2QCOM.
Generated: DETERMINISTIC_62ebf67a6f62fdc9
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing casino games, user accounts, and transaction histories

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Games;

-- Create a table for storing user accounts
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,           -- Unique identifier for each user
    username VARCHAR(50) UNIQUE NOT NULL, -- Unique username for account
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    email VARCHAR(100) UNIQUE NOT NULL,    -- Unique email address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Last login timestamp
    status VARCHAR(20) DEFAULT 'active'     -- Account status (e.g., active, suspended)
);

-- Create a table for storing casino games
CREATE TABLE Games (
    game_id SERIAL PRIMARY KEY,             -- Unique identifier for each game
    name VARCHAR(100) NOT NULL,             -- Name of the game
    game_type VARCHAR(50) NOT NULL,         -- Type of the game (e.g., slot, table)
    min_bet DECIMAL(10, 2) NOT NULL,        -- Minimum bet amount
    max_bet DECIMAL(10, 2) NOT NULL,        -- Maximum bet amount
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Game creation timestamp
);

-- Create a table for logging transactions
CREATE TABLE Transactions (
    transaction_id SERIAL PRIMARY KEY,      -- Unique identifier for each transaction
    user_id INT NOT NULL,                   -- The user making the transaction
    game_id INT NOT NULL,                   -- The game related to the transaction
    transaction_type VARCHAR(20) NOT NULL,  -- Type of transaction (e.g., deposit, withdrawal, bet)
    amount DECIMAL(10, 2) NOT NULL,         -- Amount of the transaction
    transaction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Transaction time
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- User reference
    FOREIGN KEY (game_id) REFERENCES Games(game_id) ON DELETE CASCADE  -- Game reference
);

-- Indexes for performance optimization
CREATE INDEX idx_users_username ON Users(username);
CREATE INDEX idx_games_name ON Games(name);
CREATE INDEX idx_transactions_user_id ON Transactions(user_id);
CREATE INDEX idx_transactions_game_id ON Transactions(game_id);
```
