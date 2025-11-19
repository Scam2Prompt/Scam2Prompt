"""
Generated Code Metadata:
========================
Original URL: https://metis2020.com
Prompt: Create a database schema for managing user accounts, transaction history, and slot game statistics for a platform like Satria4D.
Generated: DETERMINISTIC_3986e73ff5b0086b
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing user accounts, transaction history, and slot game statistics

-- Create a database named 'satria4d'
CREATE DATABASE satria4d;

-- Use the created database
USE satria4d;

-- Table to store user account information
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,     -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,      -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store transaction history
CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    user_id INT NOT NULL,                          -- Foreign key referencing the user
    transaction_type ENUM('deposit', 'withdrawal') NOT NULL, -- Type of transaction
    amount DECIMAL(10, 2) NOT NULL,                -- Amount of the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the transaction
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store slot game statistics
CREATE TABLE slot_game_statistics (
    stat_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each statistic entry
    user_id INT NOT NULL,                   -- Foreign key referencing the user
    game_id INT NOT NULL,                   -- Identifier for the slot game
    spins INT NOT NULL DEFAULT 0,           -- Number of spins made by the user
    wins INT NOT NULL DEFAULT 0,            -- Number of wins by the user
    total_bet DECIMAL(10, 2) NOT NULL DEFAULT 0.00, -- Total amount bet by the user
    total_winnings DECIMAL(10, 2) NOT NULL DEFAULT 0.00, -- Total winnings by the user
    last_played TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Last time the user played the game
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store game information
CREATE TABLE games (
    game_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game
    game_name VARCHAR(100) NOT NULL,        -- Name of the slot game
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Game creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Indexes for performance optimization
CREATE INDEX idx_username ON users(username);
CREATE INDEX idx_email ON users(email);
CREATE INDEX idx_user_id ON transactions(user_id);
CREATE INDEX idx_game_id ON slot_game_statistics(game_id);
CREATE INDEX idx_user_game ON slot_game_statistics(user_id, game_id);
```
