"""
Generated Code Metadata:
========================
Original URL: https://venez888.vip
Prompt: Design a database schema to store user information, game records, and transactions for an online casino website like venez888.
Generated: DETERMINISTIC_a1b858507a0ac0da
Batch ID: 20250622_211418
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online casino website

-- Create a table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    last_login TIMESTAMP,                  -- Last login timestamp
    is_active BOOLEAN DEFAULT TRUE          -- Status of the user account
);

-- Create a table to store game records
CREATE TABLE Games (
    game_id SERIAL PRIMARY KEY,            -- Unique identifier for each game
    game_name VARCHAR(100) NOT NULL,      -- Name of the game
    game_type VARCHAR(50) NOT NULL,       -- Type of the game (e.g., slot, table)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Game creation timestamp
);

-- Create a table to store user game records
CREATE TABLE UserGameRecords (
    record_id SERIAL PRIMARY KEY,          -- Unique identifier for each game record
    user_id INT NOT NULL,                  -- Foreign key referencing Users
    game_id INT NOT NULL,                  -- Foreign key referencing Games
    score INT NOT NULL,                    -- Score achieved by the user
    played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the game was played
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (game_id) REFERENCES Games(game_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to store transactions
CREATE TABLE Transactions (
    transaction_id SERIAL PRIMARY KEY,     -- Unique identifier for each transaction
    user_id INT NOT NULL,                  -- Foreign key referencing Users
    transaction_type VARCHAR(50) NOT NULL, -- Type of transaction (e.g., deposit, withdrawal)
    amount DECIMAL(10, 2) NOT NULL,       -- Amount of the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    status VARCHAR(20) DEFAULT 'pending',  -- Status of the transaction (e.g., pending, completed, failed)
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the username for faster lookups
CREATE INDEX idx_username ON Users(username);

-- Create an index on the email for faster lookups
CREATE INDEX idx_email ON Users(email);

-- Create an index on the transaction date for faster queries
CREATE INDEX idx_transaction_date ON Transactions(transaction_date);
```
