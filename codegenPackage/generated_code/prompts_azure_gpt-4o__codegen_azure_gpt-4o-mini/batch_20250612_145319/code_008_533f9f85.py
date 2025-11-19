"""
Generated Code Metadata:
========================
Original URL: https://www.uhcstepup.com
Prompt: Create a database schema for tracking player statistics and game outcomes for a slot game platform like Slot138, focusing on features of Slot Thailand.
Generated: DETERMINISTIC_533f9f85b846b23c
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking player statistics and game outcomes for a slot game platform

-- Create a database for the slot game platform
CREATE DATABASE SlotGamePlatform;

-- Use the created database
USE SlotGamePlatform;

-- Table to store player information
CREATE TABLE Players (
    player_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each player
    username VARCHAR(50) NOT NULL UNIQUE,      -- Unique username for the player
    email VARCHAR(100) NOT NULL UNIQUE,         -- Unique email for the player
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the player registered
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last login
);

-- Table to store game information
CREATE TABLE Games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each game
    game_name VARCHAR(100) NOT NULL,            -- Name of the game
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of when the game was created
);

-- Table to store player statistics
CREATE TABLE PlayerStatistics (
    stat_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each statistic entry
    player_id INT NOT NULL,                      -- Foreign key referencing Players
    game_id INT NOT NULL,                        -- Foreign key referencing Games
    total_spins INT DEFAULT 0,                   -- Total number of spins made by the player
    total_wins DECIMAL(10, 2) DEFAULT 0.00,     -- Total amount won by the player
    total_bets DECIMAL(10, 2) DEFAULT 0.00,     -- Total amount bet by the player
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the statistics were recorded
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (game_id) REFERENCES Games(game_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store game outcomes
CREATE TABLE GameOutcomes (
    outcome_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each game outcome
    player_id INT NOT NULL,                      -- Foreign key referencing Players
    game_id INT NOT NULL,                        -- Foreign key referencing Games
    outcome_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the outcome was recorded
    bet_amount DECIMAL(10, 2) NOT NULL,         -- Amount bet in the game
    win_amount DECIMAL(10, 2) DEFAULT 0.00,     -- Amount won in the game
    outcome VARCHAR(255) NOT NULL,               -- Description of the outcome
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (game_id) REFERENCES Games(game_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_player_id ON PlayerStatistics(player_id);
CREATE INDEX idx_game_id ON PlayerStatistics(game_id);
CREATE INDEX idx_player_game ON GameOutcomes(player_id, game_id);
```
