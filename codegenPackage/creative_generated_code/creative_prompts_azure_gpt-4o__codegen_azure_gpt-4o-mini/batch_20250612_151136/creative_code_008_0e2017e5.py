"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pokemoney.info
Prompt: Provide an example of a database schema for managing user accounts, deposits, and game statistics for UW99, using details from https://pokemoney.info.
Generated: DETERMINISTIC_0e2017e5efa09ff6
Batch ID: 20250612_151136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing user accounts, deposits, and game statistics for UW99

-- Create the 'users' table to store user account information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,              -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,    -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,     -- Hashed password for secure storage
    email VARCHAR(100) NOT NULL UNIQUE,       -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    last_login TIMESTAMP                      -- Last login timestamp
);

-- Create the 'deposits' table to track user deposits
CREATE TABLE deposits (
    deposit_id SERIAL PRIMARY KEY,            -- Unique identifier for each deposit
    user_id INT NOT NULL,                     -- Reference to the user making the deposit
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0), -- Amount of the deposit must be positive
    deposit_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the deposit
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Create the 'game_statistics' table to store user game statistics
CREATE TABLE game_statistics (
    stat_id SERIAL PRIMARY KEY,                -- Unique identifier for each statistic entry
    user_id INT NOT NULL,                      -- Reference to the user whose statistics are recorded
    games_played INT DEFAULT 0,                -- Total number of games played by the user
    wins INT DEFAULT 0,                        -- Total number of wins
    losses INT DEFAULT 0,                      -- Total number of losses
    last_game TIMESTAMP,                       -- Timestamp of the last game played
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Indexes for optimizing query performance
CREATE INDEX idx_username ON users(username);
CREATE INDEX idx_email ON users(email);
CREATE INDEX idx_user_id ON deposits(user_id);
CREATE INDEX idx_user_stats ON game_statistics(user_id);
```
