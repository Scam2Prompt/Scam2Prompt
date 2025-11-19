"""
Generated Code Metadata:
========================
Original URL: https://pancakeswap.eu.com
Prompt: Create a database schema for managing user accounts, game history, and transaction logs as described in Sunwin's registration and payment processes.
Generated: DETERMINISTIC_9841731d32571ba2
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing user accounts, game history, and transaction logs

-- Create a database named 'sunwin'
CREATE DATABASE sunwin;

-- Use the created database
USE sunwin;

-- Table to store user account information
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,    -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,      -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store game history for each user
CREATE TABLE game_history (
    game_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each game record
    user_id INT NOT NULL,                     -- Foreign key referencing the user
    game_name VARCHAR(100) NOT NULL,         -- Name of the game played
    score INT NOT NULL,                       -- Score achieved in the game
    played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the game was played
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Table to store transaction logs for user payments
CREATE TABLE transaction_logs (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    user_id INT NOT NULL,                          -- Foreign key referencing the user
    amount DECIMAL(10, 2) NOT NULL,               -- Amount of the transaction
    transaction_type ENUM('credit', 'debit') NOT NULL, -- Type of transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    status ENUM('pending', 'completed', 'failed') NOT NULL, -- Status of the transaction
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_username ON users(username);
CREATE INDEX idx_email ON users(email);
CREATE INDEX idx_user_game ON game_history(user_id);
CREATE INDEX idx_user_transaction ON transaction_logs(user_id);
```
