"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foodandwine.one
Prompt: Write a SQL schema for a database to manage game categories, user bets, and transaction records for a gambling platform similar to Hi88.
Generated: DETERMINISTIC_c5b7b7902b8df56d
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Schema for a Gambling Platform

-- Create a table for storing categories of games
CREATE TABLE game_categories (
    category_id SERIAL PRIMARY KEY,       -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL,  -- Name of the game category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of category creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table for storing users
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,           -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Registration timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table for storing bets made by users
CREATE TABLE user_bets (
    bet_id SERIAL PRIMARY KEY,            -- Unique identifier for each bet
    user_id INT NOT NULL,                 -- Foreign key referencing the user
    category_id INT NOT NULL,             -- Foreign key referencing the game category
    bet_amount DECIMAL(10,2) NOT NULL,   -- Amount of the bet
    bet_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the bet was placed
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (category_id) REFERENCES game_categories(category_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for storing transaction records
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,    -- Unique identifier for each transaction
    user_id INT NOT NULL,                 -- Foreign key referencing the user
    transaction_type VARCHAR(50) NOT NULL, -- Type of transaction (e.g., deposit, withdrawal)
    amount DECIMAL(10,2) NOT NULL,       -- Transaction amount
    transaction_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the transaction occurred
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on user_bets for faster retrieval
CREATE INDEX idx_user_bets ON user_bets (user_id, category_id);

-- Create an index on transactions for faster retrieval
CREATE INDEX idx_transactions ON transactions (user_id, transaction_timestamp);
```
