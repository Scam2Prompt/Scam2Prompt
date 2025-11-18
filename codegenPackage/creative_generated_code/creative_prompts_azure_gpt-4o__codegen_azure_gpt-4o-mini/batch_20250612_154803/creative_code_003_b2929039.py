"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxful-login.id
Prompt: Create a database schema for managing slot game data, including game titles, RTP percentages, and user rewards, based on the features of Planet128.
Generated: DETERMINISTIC_b2929039830adfa4
Batch ID: 20250612_154803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for managing slot game data

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS UserRewards;
DROP TABLE IF EXISTS SlotGames;

-- Create a table to store slot game information
CREATE TABLE SlotGames (
    GameID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each game
    Title VARCHAR(255) NOT NULL,            -- Title of the slot game
    RTP DECIMAL(5, 2) NOT NULL CHECK (RTP BETWEEN 0 AND 100), -- Return to Player percentage
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the game record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store user rewards associated with games
CREATE TABLE UserRewards (
    RewardID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each reward
    UserID INT NOT NULL,                      -- ID of the user receiving the reward
    GameID INT NOT NULL,                      -- ID of the associated slot game
    RewardAmount DECIMAL(10, 2) NOT NULL,    -- Amount of reward given to the user
    RewardDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the reward was issued
    FOREIGN KEY (GameID) REFERENCES SlotGames(GameID) ON DELETE CASCADE -- Link to SlotGames table
);

-- Insert example data into SlotGames table
INSERT INTO SlotGames (Title, RTP) VALUES
('Dragon’s Fortune', 96.5),
('Mystic Wealth', 94.0),
('Treasure Quest', 97.8);

-- Insert example data into UserRewards table
INSERT INTO UserRewards (UserID, GameID, RewardAmount) VALUES
(1, 1, 10.00),
(2, 1, 20.50),
(1, 2, 15.00);

-- Database schema ready for managing slot game data and user rewards
-- Ensure to implement proper error handling in your application code to handle potential database errors.
```
