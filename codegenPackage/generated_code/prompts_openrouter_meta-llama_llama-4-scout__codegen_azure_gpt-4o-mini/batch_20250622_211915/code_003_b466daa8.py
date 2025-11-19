"""
Generated Code Metadata:
========================
Original URL: https://swanbay.dip.vn
Prompt: Design a database schema for storing user information, game data, and transaction records for a betting platform like VZ99.
Generated: DETERMINISTIC_b466daa8a6fbfde0
Batch ID: 20250622_211915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a betting platform

-- Create a table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store game data
CREATE TABLE Games (
    game_id SERIAL PRIMARY KEY,            -- Unique identifier for each game
    game_name VARCHAR(100) NOT NULL,      -- Name of the game
    game_type VARCHAR(50) NOT NULL,       -- Type of the game (e.g., slot, poker)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of game creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store transaction records
CREATE TABLE Transactions (
    transaction_id SERIAL PRIMARY KEY,     -- Unique identifier for each transaction
    user_id INT NOT NULL,                  -- Foreign key referencing Users
    game_id INT NOT NULL,                  -- Foreign key referencing Games
    transaction_type VARCHAR(10) NOT NULL, -- Type of transaction (e.g., deposit, withdrawal)
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0), -- Amount of the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (game_id) REFERENCES Games(game_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create an index on the Transactions table for faster lookups by user_id
CREATE INDEX idx_user_id ON Transactions(user_id);

-- Create an index on the Transactions table for faster lookups by game_id
CREATE INDEX idx_game_id ON Transactions(game_id);
```
