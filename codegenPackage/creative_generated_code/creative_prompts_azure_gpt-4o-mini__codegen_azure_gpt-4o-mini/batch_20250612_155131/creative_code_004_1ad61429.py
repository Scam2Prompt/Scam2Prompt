"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1wknju.top
Prompt: Describe how to set up a database schema for storing user bets and sports events for a platform like 1win.
Generated: DETERMINISTIC_1ad61429cc007835
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for a sports betting platform

-- Create a new database for the betting platform
CREATE DATABASE BettingPlatform;

-- Use the created database
USE BettingPlatform;

-- Table for storing users
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,    -- Unique username for each user
    password_hash VARCHAR(255) NOT NULL,      -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,       -- Unique email address for each user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for last update
);

-- Table for storing sports events
CREATE TABLE SportsEvents (
    event_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each event
    sport VARCHAR(50) NOT NULL,                  -- Type of sport (e.g., Football, Basketball)
    event_name VARCHAR(100) NOT NULL,            -- Name of the event
    event_date DATETIME NOT NULL,                -- Date and time of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for event creation
);

-- Table for storing user bets
CREATE TABLE Bets (
    bet_id INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each bet
    user_id INT NOT NULL,                           -- Foreign key referencing Users
    event_id INT NOT NULL,                          -- Foreign key referencing SportsEvents
    bet_amount DECIMAL(10, 2) NOT NULL CHECK (bet_amount > 0),  -- Amount of the bet
    odds DECIMAL(5, 2) NOT NULL CHECK (odds > 0),  -- Odds for the bet
    bet_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the bet was placed
    status ENUM('Pending', 'Won', 'Lost') DEFAULT 'Pending', -- Status of the bet
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,  -- Referential integrity
    FOREIGN KEY (event_id) REFERENCES SportsEvents(event_id) ON DELETE CASCADE  -- Referential integrity
);

-- Table for storing bet outcomes (optional for future use)
CREATE TABLE BetOutcomes (
    outcome_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each outcome
    bet_id INT NOT NULL,                           -- Foreign key referencing Bets
    payout DECIMAL(10, 2) DEFAULT 0.00,           -- Amount to payout if the bet is won
    outcome_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the outcome is recorded
    FOREIGN KEY (bet_id) REFERENCES Bets(bet_id) ON DELETE CASCADE  -- Referential integrity
);
```
