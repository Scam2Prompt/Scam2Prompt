"""
Generated Code Metadata:
========================
Original URL: https://casinovlad.com
Prompt: "Design a simple database schema for storing user information, game records, and transactions for an online casino like Cazino Vlad, using SQL."
Generated: DETERMINISTIC_b6bbf73f5f4c2de2
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online casino

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS GameRecords;
DROP TABLE IF EXISTS Users;

-- Table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    last_login TIMESTAMP                   -- Timestamp of last login
);

-- Table to store game records
CREATE TABLE GameRecords (
    game_id SERIAL PRIMARY KEY,            -- Unique identifier for each game record
    user_id INT NOT NULL,                  -- Foreign key referencing Users
    game_name VARCHAR(100) NOT NULL,       -- Name of the game played
    bet_amount DECIMAL(10, 2) NOT NULL,    -- Amount bet by the user
    win_amount DECIMAL(10, 2) DEFAULT 0,   -- Amount won by the user
    game_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the game
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store transactions
CREATE TABLE Transactions (
    transaction_id SERIAL PRIMARY KEY,     -- Unique identifier for each transaction
    user_id INT NOT NULL,                   -- Foreign key referencing Users
    transaction_type VARCHAR(50) NOT NULL,  -- Type of transaction (e.g., deposit, withdrawal)
    amount DECIMAL(10, 2) NOT NULL,         -- Amount of the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_username ON Users(username);
CREATE INDEX idx_email ON Users(email);
CREATE INDEX idx_user_game ON GameRecords(user_id);
CREATE INDEX idx_user_transaction ON Transactions(user_id);
```
