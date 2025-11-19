"""
Generated Code Metadata:
========================
Original URL: https://www.celestiadao.app
Prompt: Create a database schema for managing user transactions and gameplay history in a slot game platform like BONANZASLOT, ensuring transparency and accountability.
Generated: DETERMINISTIC_bbc93881ecffc58f
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing user transactions and gameplay history in a slot game platform

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS gameplay_history;

-- Table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store transaction records
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,    -- Unique identifier for each transaction
    user_id INT NOT NULL,                 -- Foreign key referencing users
    transaction_type VARCHAR(20) NOT NULL, -- Type of transaction (e.g., deposit, withdrawal)
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0), -- Amount of the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    status VARCHAR(20) NOT NULL,          -- Status of the transaction (e.g., completed, pending, failed)
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store gameplay history
CREATE TABLE gameplay_history (
    gameplay_id SERIAL PRIMARY KEY,       -- Unique identifier for each gameplay record
    user_id INT NOT NULL,                 -- Foreign key referencing users
    game_id VARCHAR(50) NOT NULL,         -- Identifier for the game played
    bet_amount DECIMAL(10, 2) NOT NULL CHECK (bet_amount > 0), -- Amount bet in the game
    win_amount DECIMAL(10, 2) NOT NULL DEFAULT 0, -- Amount won in the game
    gameplay_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the gameplay
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_user_transactions ON transactions(user_id);
CREATE INDEX idx_user_gameplay ON gameplay_history(user_id);
```
