"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aspjj.com
Prompt: "Create a database schema for managing slot game data, including game titles, RTP rates, and user bets, as described on สล็อตเว็บตรง."
Generated: DETERMINISTIC_8b148c6dfd89e436
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- This SQL script creates a database schema for managing slot game data.
-- The schema includes tables for games, RTP rates, and user bets.

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS UserBets;
DROP TABLE IF EXISTS Games;
DROP TABLE IF EXISTS RTPRates;

-- Create the Games table to store information about each slot game
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each game
    Title VARCHAR(255) NOT NULL,             -- Title of the slot game
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the game was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create the RTPRates table to store the Return to Player percentages for each game
CREATE TABLE RTPRates (
    RTPID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the RTP record
    GameID INT NOT NULL,                       -- Foreign key to associate RTP with a specific game
    RTPRate DECIMAL(5, 2) NOT NULL,           -- RTP rate as a percentage (e.g., 96.50)
    EffectiveDate DATE NOT NULL,               -- Date when the RTP rate becomes effective
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE  -- Establish foreign key relationship
);

-- Create the UserBets table to record user bets on games
CREATE TABLE UserBets (
    BetID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each bet
    UserID INT NOT NULL,                       -- Placeholder for user ID (assumed to be stored in another table)
    GameID INT NOT NULL,                       -- Foreign key to associate the bet with a specific game
    BetAmount DECIMAL(10, 2) NOT NULL,        -- Amount of the bet
    BetTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the bet was placed
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE  -- Establish foreign key relationship
);

-- Sample insert statements to test the schema
-- Insert sample data into the Games table
INSERT INTO Games (Title) VALUES ('Mystic Fortune'), ('Lucky Seven'), ('Dragon's Treasure');

-- Insert sample RTP rates for the games
INSERT INTO RTPRates (GameID, RTPRate, EffectiveDate) VALUES 
(1, 96.50, '2023-01-01'), 
(2, 95.00, '2023-01-01'), 
(3, 97.25, '2023-01-01');

-- Insert sample user bets
INSERT INTO UserBets (UserID, GameID, BetAmount) VALUES 
(1, 1, 10.00), 
(2, 2, 20.00), 
(1, 3, 5.50);
```
