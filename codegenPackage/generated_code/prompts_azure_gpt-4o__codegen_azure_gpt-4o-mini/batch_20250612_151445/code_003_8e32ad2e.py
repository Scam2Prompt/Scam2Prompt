"""
Generated Code Metadata:
========================
Original URL: https://www.shibaswaap.us.com
Prompt: Create a database schema for managing user accounts, game statistics, and transaction histories for a multi-platform gaming ecosystem like 789Club.
Generated: DETERMINISTIC_8e32ad2e89fb5cb8
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing user accounts, game statistics, and transaction histories
CREATE DATABASE IF NOT EXISTS GamingEcosystem;

USE GamingEcosystem;

-- Table to store user account information
CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,      -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,     -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store game statistics for each user
CREATE TABLE IF NOT EXISTS GameStatistics (
    stat_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each statistic entry
    user_id INT NOT NULL,                   -- Foreign key referencing Users table
    game_id INT NOT NULL,                   -- Identifier for the game
    score INT NOT NULL,                     -- Score achieved by the user
    play_time INT NOT NULL,                 -- Total play time in seconds
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the statistic entry
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Table to store transaction histories for each user
CREATE TABLE IF NOT EXISTS Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    user_id INT NOT NULL,                          -- Foreign key referencing Users table
    transaction_type ENUM('deposit', 'withdrawal', 'purchase') NOT NULL, -- Type of transaction
    amount DECIMAL(10, 2) NOT NULL,               -- Amount involved in the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Table to store game information
CREATE TABLE IF NOT EXISTS Games (
    game_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game
    game_name VARCHAR(100) NOT NULL UNIQUE,  -- Name of the game
    platform ENUM('PC', 'Console', 'Mobile') NOT NULL, -- Supported platform
    release_date DATE NOT NULL,               -- Release date of the game
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of game entry
);

-- Indexes for performance optimization
CREATE INDEX idx_username ON Users(username);
CREATE INDEX idx_email ON Users(email);
CREATE INDEX idx_user_id ON GameStatistics(user_id);
CREATE INDEX idx_game_id ON GameStatistics(game_id);
CREATE INDEX idx_transaction_user ON Transactions(user_id);
```
