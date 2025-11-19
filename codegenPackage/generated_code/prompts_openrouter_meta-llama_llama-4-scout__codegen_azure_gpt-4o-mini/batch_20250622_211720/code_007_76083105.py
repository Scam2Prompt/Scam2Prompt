"""
Generated Code Metadata:
========================
Original URL: https://status-ehaat.life
Prompt: "Design a database schema for a lottery platform, including tables for games, users, and transactions."
Generated: DETERMINISTIC_76083105817c8f49
Batch ID: 20250622_211720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a lottery platform

-- Table to store information about different lottery games
CREATE TABLE games (
    game_id SERIAL PRIMARY KEY,          -- Unique identifier for each game
    game_name VARCHAR(100) NOT NULL,    -- Name of the lottery game
    game_description TEXT,               -- Description of the game
    draw_date TIMESTAMP NOT NULL,        -- Date and time of the next draw
    ticket_price DECIMAL(10, 2) NOT NULL,-- Price of a single ticket
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,-- Unique username for the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,  -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store transactions related to lottery tickets
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,   -- Unique identifier for each transaction
    user_id INT NOT NULL,                -- Foreign key referencing the user
    game_id INT NOT NULL,                -- Foreign key referencing the game
    ticket_count INT NOT NULL CHECK (ticket_count > 0), -- Number of tickets purchased
    total_amount DECIMAL(10, 2) NOT NULL, -- Total amount spent on the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, -- Ensure user integrity
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE -- Ensure game integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_transactions_user ON transactions(user_id);
CREATE INDEX idx_transactions_game ON transactions(game_id);
```
