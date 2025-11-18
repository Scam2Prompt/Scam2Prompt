"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bolehshop.id
Prompt: Create a database schema in SQL for managing lottery game results, user accounts, and payment transactions, inspired by the HONGTOGEL platform.
Generated: DETERMINISTIC_078d2b3a960e1199
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing lottery game results, user accounts, and payment transactions

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS transactions CASCADE;
DROP TABLE IF EXISTS lottery_results CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- Table for storing user accounts
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,                -- Unique identifier for each user
    username VARCHAR(50) UNIQUE NOT NULL,     -- Username of the user
    password_hash VARCHAR(255) NOT NULL,      -- Hashed password for security
    email VARCHAR(100) UNIQUE NOT NULL,        -- User's email address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    is_active BOOLEAN DEFAULT TRUE              -- Active status of the account
);

-- Table for storing lottery game results
CREATE TABLE lottery_results (
    result_id SERIAL PRIMARY KEY,               -- Unique identifier for each result
    game_name VARCHAR(50) NOT NULL,            -- Name of the lottery game
    draw_date DATE NOT NULL,                    -- Date of the draw
    winning_numbers VARCHAR(50) NOT NULL,      -- Winning numbers as a string
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Result creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Table for storing payment transactions
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,          -- Unique identifier for each transaction
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE, -- User associated with the transaction
    amount DECIMAL(10, 2) NOT NULL,            -- Amount of the transaction
    transaction_type VARCHAR(20) NOT NULL,     -- Type of transaction (e.g., deposit, withdrawal)
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    status VARCHAR(20) NOT NULL DEFAULT 'pending' -- Status of the transaction (e.g., pending, completed, failed)
);

-- Indexes for performance optimization
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_lottery_results_game_name ON lottery_results(game_name);
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_transaction_date ON transactions(transaction_date);
```
