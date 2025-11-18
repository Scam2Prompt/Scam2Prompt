"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://downtownspokanehotels.com
Prompt: Create a database schema for storing Togel HK lottery results and user betting data, ensuring compatibility with the features offered by Holyslots88.
Generated: DETERMINISTIC_85630515a6b2e125
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing Togel HK lottery results and user betting data

-- Drop the database if it exists for a clean start (use with caution)
DROP DATABASE IF EXISTS TogelHK;
CREATE DATABASE TogelHK;

-- Use the newly created database
USE TogelHK;

-- Table to store user information
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,    -- Unique username for login
    password_hash VARCHAR(255) NOT NULL,     -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,       -- Unique email for notifications
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Account creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Last update timestamp
);

-- Table to store lottery results
CREATE TABLE LotteryResults (
    result_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each result
    draw_date DATE NOT NULL,                   -- Date of the lottery draw
    winning_numbers VARCHAR(50) NOT NULL,      -- Winning numbers as a string
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of when the result was recorded
);

-- Table to store user bets
CREATE TABLE UserBets (
    bet_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each bet
    user_id INT NOT NULL,                       -- User who placed the bet (foreign key)
    bet_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time when the bet was placed
    bet_numbers VARCHAR(50) NOT NULL,           -- Numbers bet by the user
    stake DECIMAL(10, 2) NOT NULL CHECK (stake > 0),  -- Amount staked
    result_id INT,                              -- Associated lottery result (foreign key)
    
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,  -- Enforce referential integrity
    FOREIGN KEY (result_id) REFERENCES LotteryResults(result_id) ON DELETE SET NULL  -- Link to results
);

-- Indexing for better performance on user bets and results
CREATE INDEX idx_user_id ON UserBets(user_id);
CREATE INDEX idx_draw_date ON LotteryResults(draw_date);
```
