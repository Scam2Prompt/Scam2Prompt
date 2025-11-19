"""
Generated Code Metadata:
========================
Original URL: https://shubaswap.com
Prompt: Create a database schema for storing user accounts, game history, and jackpot winnings, modeled after the MESIN128 platform.
Generated: DETERMINISTIC_20d203e2f42924f3
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing user accounts, game history, and jackpot winnings

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS jackpot_winnings;
DROP TABLE IF EXISTS game_history;
DROP TABLE IF EXISTS user_accounts;

-- Table to store user account information
CREATE TABLE user_accounts (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store game history for each user
CREATE TABLE game_history (
    game_id SERIAL PRIMARY KEY, -- Unique identifier for each game entry
    user_id INT NOT NULL, -- Foreign key referencing user_accounts
    game_name VARCHAR(100) NOT NULL, -- Name of the game played
    result VARCHAR(50) NOT NULL, -- Result of the game (e.g., win, lose)
    bet_amount DECIMAL(10, 2) NOT NULL, -- Amount bet in the game
    payout_amount DECIMAL(10, 2) DEFAULT 0.00, -- Amount won in the game
    played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the game was played
    FOREIGN KEY (user_id) REFERENCES user_accounts(user_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store jackpot winnings
CREATE TABLE jackpot_winnings (
    jackpot_id SERIAL PRIMARY KEY, -- Unique identifier for each jackpot entry
    user_id INT NOT NULL, -- Foreign key referencing user_accounts
    amount_won DECIMAL(10, 2) NOT NULL, -- Amount won in the jackpot
    won_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the jackpot was won
    FOREIGN KEY (user_id) REFERENCES user_accounts(user_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_username ON user_accounts(username);
CREATE INDEX idx_email ON user_accounts(email);
CREATE INDEX idx_user_game ON game_history(user_id);
CREATE INDEX idx_user_jackpot ON jackpot_winnings(user_id);
```
