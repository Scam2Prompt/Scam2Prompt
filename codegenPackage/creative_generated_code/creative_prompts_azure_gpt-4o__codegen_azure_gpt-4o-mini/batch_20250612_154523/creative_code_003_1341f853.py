"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galxe.de.com
Prompt: Develop a database schema for storing user data, game statistics, and transaction history for a casino platform, referencing features from 123B.
Generated: DETERMINISTIC_1341f8535fd07c3f
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a casino platform
-- This schema will store user data, game statistics, and transaction history.

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS game_statistics;
DROP TABLE IF EXISTS users;

-- Table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,                -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,     -- Unique username for each user
    password_hash VARCHAR(255) NOT NULL,      -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,       -- Unique email address for each user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the user was last updated
    last_login TIMESTAMP,                      -- Timestamp for the last login
    is_active BOOLEAN DEFAULT TRUE             -- Indicates if the user is active
);

-- Table to store game statistics
CREATE TABLE game_statistics (
    stat_id SERIAL PRIMARY KEY,                 -- Unique identifier for each game statistic
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE, -- Foreign key referencing users
    game_name VARCHAR(50) NOT NULL,            -- Name of the game played
    total_played INT DEFAULT 0,                 -- Total number of times the game has been played
    total_won DECIMAL(10, 2) DEFAULT 0.00,     -- Total amount won by the user in this game
    total_lost DECIMAL(10, 2) DEFAULT 0.00,     -- Total amount lost by the user in this game
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the statistics were created
);

-- Table to store transaction history
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,          -- Unique identifier for each transaction
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE, -- Foreign key referencing users
    transaction_type ENUM('deposit', 'withdrawal') NOT NULL, -- Type of transaction
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0), -- Amount of the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    status ENUM('pending', 'completed', 'failed') DEFAULT 'pending' -- Status of the transaction
);

-- Indexes for performance optimization
CREATE INDEX idx_username ON users(username);
CREATE INDEX idx_email ON users(email);
CREATE INDEX idx_user_game ON game_statistics(user_id, game_name);
CREATE INDEX idx_transaction ON transactions(user_id, transaction_date);
```
