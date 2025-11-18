"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shubaswap.com
Prompt: Create a database schema for storing user accounts, game history, and jackpot winnings, modeled after the MESIN128 platform.
Generated: DETERMINISTIC_20d203e2f42924f3
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Creating a database schema for storing user accounts, game history, and jackpot winnings

-- Start by creating the main database
CREATE DATABASE MESIN128;

-- Use the MESIN128 database
USE MESIN128;

-- Table to store user account information
CREATE TABLE UserAccounts (
    user_id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,          -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,           -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,             -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Table to store game history for each user
CREATE TABLE GameHistory (
    history_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each game record
    user_id INT NOT NULL,                           -- Foreign key referencing UserAccounts
    game_name VARCHAR(100) NOT NULL,                -- Name of the game played
    play_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time of the game played
    result VARCHAR(50) NOT NULL,                    -- Result of the game (e.g., win, lose)
    winnings DECIMAL(10, 2) DEFAULT 0.00,           -- Amount won in the game
    FOREIGN KEY (user_id) REFERENCES UserAccounts(user_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Table to store jackpot winnings
CREATE TABLE JackpotWinnings (
    jackpot_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each jackpot record
    user_id INT NOT NULL,                           -- Foreign key referencing UserAccounts
    winning_amount DECIMAL(10, 2) NOT NULL,        -- Amount won in the jackpot
    winning_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the jackpot was won
    FOREIGN KEY (user_id) REFERENCES UserAccounts(user_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Create indexes for performance optimization
CREATE INDEX idx_username ON UserAccounts(username);
CREATE INDEX idx_userid_gamehistory ON GameHistory(user_id);
CREATE INDEX idx_userid_jackpot ON JackpotWinnings(user_id);

-- End of schema creation
```
