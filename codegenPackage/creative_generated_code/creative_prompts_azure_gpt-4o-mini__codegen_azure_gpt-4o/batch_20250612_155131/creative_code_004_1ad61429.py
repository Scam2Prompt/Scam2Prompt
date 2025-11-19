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
-- SQL script to set up a database schema for storing user bets and sports events
-- This schema is designed for a betting platform like 1win

-- Create a table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for the user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username
    PasswordHash VARCHAR(255) NOT NULL,    -- Password hash for security
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address
    Balance DECIMAL(10, 2) DEFAULT 0.00,   -- User's account balance
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store sports events
CREATE TABLE SportsEvents (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for the event
    EventName VARCHAR(100) NOT NULL,        -- Name of the event
    EventDate DATETIME NOT NULL,            -- Date and time of the event
    SportType VARCHAR(50) NOT NULL,         -- Type of sport (e.g. football, basketball)
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp of event creation
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store user bets
CREATE TABLE Bets (
    BetID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique ID for the bet
    UserID INT NOT NULL,                           -- Foreign key to Users table
    EventID INT NOT NULL,                          -- Foreign key to SportsEvents table
    BetAmount DECIMAL(10, 2) NOT NULL,             -- Amount of money placed on the bet
    BetType VARCHAR(50) NOT NULL,                  -- Type of bet (e.g. "win", "over/under")
    Odds DECIMAL(5, 2) NOT NULL,                   -- Odds for the bet
    BetStatus ENUM('pending', 'won', 'lost') DEFAULT 'pending', -- Status of the bet
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of bet creation
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete to remove bets if user is deleted
    FOREIGN KEY (EventID) REFERENCES SportsEvents(EventID) ON DELETE CASCADE -- Cascade delete to remove bets if event is deleted
);

-- Create indexes for better query performance
CREATE INDEX idx_UserID ON Bets(UserID);
CREATE INDEX idx_EventID ON Bets(EventID);
CREATE INDEX idx_EventDate ON SportsEvents(EventDate);
CREATE INDEX idx_Username ON Users(Username);
CREATE INDEX idx_Email ON Users(Email);

-- Error handling for strict mode and transactional integrity
SET SESSION sql_mode = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ZERO_DATE,NO_ZERO_IN_DATE,NO_ENGINE_SUBSTITUTION';

-- Ensure proper default values and data integrity
ALTER TABLE Users MODIFY Balance DECIMAL(10, 2) DEFAULT 0.00 CHECK (Balance >= 0);
```
