"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.eu.com
Prompt: Create a database schema for managing user accounts, game history, and transaction logs as described in Sunwin's registration and payment processes.
Generated: DETERMINISTIC_9841731d32571ba2
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create the database for managing user accounts, game history, and transaction logs
CREATE DATABASE IF NOT EXISTS SunwinDB;

USE SunwinDB;

-- Table for storing user accounts
CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,            -- Username for the user (unique)
    password_hash VARCHAR(255) NOT NULL,              -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,               -- User's email (unique)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the account was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Table for storing game history
CREATE TABLE IF NOT EXISTS GameHistory (
    game_id INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for each game record
    user_id INT NOT NULL,                              -- Foreign key referencing Users table
    game_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Date and time when the game was played
    score INT NOT NULL,                                -- Score obtained in the game
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Cascade delete for user removal
);

-- Table for storing transaction logs
CREATE TABLE IF NOT EXISTS TransactionLogs (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each transaction
    user_id INT NOT NULL,                              -- Foreign key referencing Users table
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the transaction occurred
    amount DECIMAL(10, 2) NOT NULL,                   -- Amount for the transaction
    transaction_type ENUM('credit', 'debit') NOT NULL, -- Type of transaction (credit or debit)
    description VARCHAR(255),                          -- Description of the transaction
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Cascade delete for user removal
);

-- Indexes for faster queries
CREATE INDEX idx_username ON Users(username);
CREATE INDEX idx_email ON Users(email);
CREATE INDEX idx_user_game ON GameHistory(user_id);
CREATE INDEX idx_user_transaction ON TransactionLogs(user_id);

-- Sample stored procedure for adding a new user with error handling
DELIMITER $$

CREATE PROCEDURE AddUser(IN p_username VARCHAR(50), IN p_password VARCHAR(255), IN p_email VARCHAR(100))
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Error handling: roll back and signal an error
        ROLLBACK;
    END;

    START TRANSACTION;

    INSERT INTO Users (username, password_hash, email) VALUES (p_username, p_password, p_email);

    COMMIT;
END$$

DELIMITER ;
```
