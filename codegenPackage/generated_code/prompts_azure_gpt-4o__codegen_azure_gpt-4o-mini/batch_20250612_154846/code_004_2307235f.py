"""
Generated Code Metadata:
========================
Original URL: https://tronlink.at
Prompt: Create a database schema for storing user information, transaction history, and game statistics for a gambling platform similar to VSO777.
Generated: DETERMINISTIC_2307235f5deed5e2
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a gambling platform

-- Create a database for the gambling platform
CREATE DATABASE IF NOT EXISTS GamblingPlatform;

-- Use the created database
USE GamblingPlatform;

-- Table to store user information
CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,    -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,      -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    last_login TIMESTAMP NULL,               -- Timestamp of last login
    status ENUM('active', 'inactive', 'banned') DEFAULT 'active' -- User status
);

-- Table to store transaction history
CREATE TABLE IF NOT EXISTS Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    user_id INT NOT NULL,                          -- Foreign key referencing Users
    transaction_type ENUM('deposit', 'withdrawal', 'bet') NOT NULL, -- Type of transaction
    amount DECIMAL(10, 2) NOT NULL,               -- Amount involved in the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store game statistics
CREATE TABLE IF NOT EXISTS GameStatistics (
    stat_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game statistic
    user_id INT NOT NULL,                    -- Foreign key referencing Users
    game_name VARCHAR(50) NOT NULL,         -- Name of the game played
    games_played INT DEFAULT 0,              -- Total games played by the user
    wins INT DEFAULT 0,                       -- Total wins by the user
    losses INT DEFAULT 0,                     -- Total losses by the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_username ON Users(username);
CREATE INDEX idx_email ON Users(email);
CREATE INDEX idx_user_id ON Transactions(user_id);
CREATE INDEX idx_game_user ON GameStatistics(user_id);
```
