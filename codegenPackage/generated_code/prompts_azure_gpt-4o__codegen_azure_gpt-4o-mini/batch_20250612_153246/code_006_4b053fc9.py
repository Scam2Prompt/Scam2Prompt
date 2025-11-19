"""
Generated Code Metadata:
========================
Original URL: https://blogdotrabalhadordigital.com
Prompt: Create a database schema for managing user accounts, game statistics, and bonus claims for an online gaming platform similar to Pelangi189.
Generated: DETERMINISTIC_4b053fc91ad4d9d0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing user accounts, game statistics, and bonus claims
CREATE DATABASE IF NOT EXISTS OnlineGamingPlatform;

USE OnlineGamingPlatform;

-- Table to store user account information
CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,   -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,    -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,      -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Table to store game statistics for each user
CREATE TABLE IF NOT EXISTS GameStatistics (
    stat_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each statistic entry
    user_id INT NOT NULL,                   -- Foreign key referencing Users table
    game_name VARCHAR(100) NOT NULL,        -- Name of the game
    score INT NOT NULL,                      -- Score achieved by the user
    play_time INT NOT NULL,                  -- Total play time in seconds
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the statistic was recorded
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Table to store bonus claims made by users
CREATE TABLE IF NOT EXISTS BonusClaims (
    claim_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each bonus claim
    user_id INT NOT NULL,                    -- Foreign key referencing Users table
    bonus_type VARCHAR(50) NOT NULL,         -- Type of bonus claimed
    claim_amount DECIMAL(10, 2) NOT NULL,    -- Amount of the bonus claimed
    claim_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the claim was made
    status ENUM('Pending', 'Approved', 'Rejected') DEFAULT 'Pending', -- Status of the claim
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_username ON Users(username);
CREATE INDEX idx_email ON Users(email);
CREATE INDEX idx_user_id ON GameStatistics(user_id);
CREATE INDEX idx_bonus_user_id ON BonusClaims(user_id);
```
