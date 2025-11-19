"""
Generated Code Metadata:
========================
Original URL: https://optionroom.finance
Prompt: "Design a basic database schema for managing user accounts, games, and transactions for an online betting platform like HUBET."
Generated: DETERMINISTIC_6f66424a58ed13f0
Batch ID: 20250622_212351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online betting platform

-- Create a table to store user accounts
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table to store games available for betting
CREATE TABLE games (
    game_id SERIAL PRIMARY KEY,           -- Unique identifier for each game
    game_name VARCHAR(100) NOT NULL,      -- Name of the game
    game_type VARCHAR(50) NOT NULL,       -- Type of the game (e.g., sports, casino)
    start_time TIMESTAMP NOT NULL,        -- Start time of the game
    end_time TIMESTAMP NOT NULL,          -- End time of the game
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Game creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table to store transactions related to bets
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,    -- Unique identifier for each transaction
    user_id INT NOT NULL,                 -- Foreign key referencing the user
    game_id INT NOT NULL,                 -- Foreign key referencing the game
    bet_amount DECIMAL(10, 2) NOT NULL,   -- Amount of money bet
    bet_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time of the bet
    result VARCHAR(20),                    -- Result of the bet (e.g., win, lose)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Transaction creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create an index on the transactions table for faster lookups by user_id
CREATE INDEX idx_user_id ON transactions(user_id);

-- Create an index on the transactions table for faster lookups by game_id
CREATE INDEX idx_game_id ON transactions(game_id);
```
