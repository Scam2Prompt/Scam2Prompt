"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.uhcstepup.com
Prompt: Create a database schema for tracking player statistics and game outcomes for a slot game platform like Slot138, focusing on features of Slot Thailand.
Generated: DETERMINISTIC_533f9f85b846b23c
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking player statistics and game outcomes for a slot game platform

-- Create a database for the slot game platform
CREATE DATABASE SlotGamePlatform;

-- Use the newly created database
USE SlotGamePlatform;

-- Table to store player information
CREATE TABLE Players (
    player_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each player
    username VARCHAR(50) NOT NULL UNIQUE,     -- Player's username, must be unique
    email VARCHAR(100) NOT NULL UNIQUE,        -- Player's email, must be unique
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the player registered
    last_login TIMESTAMP NULL                   -- Timestamp of the player's last login
);

-- Table to store game information
CREATE TABLE Games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each game
    game_name VARCHAR(100) NOT NULL,           -- Name of the slot game
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the game was added
);

-- Table to store player statistics
CREATE TABLE PlayerStats (
    stat_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the statistics entry
    player_id INT NOT NULL,                     -- Foreign key referencing Players table
    game_id INT NOT NULL,                       -- Foreign key referencing Games table
    total_bets DECIMAL(10, 2) NOT NULL DEFAULT 0.00, -- Total amount of bets made by the player
    total_wins DECIMAL(10, 2) NOT NULL DEFAULT 0.00, -- Total amount won by the player
    total_games_played INT NOT NULL DEFAULT 0, -- Total number of games played by the player
    last_played TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the last game played
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE, -- Cascading delete on player removal
    FOREIGN KEY (game_id) REFERENCES Games(game_id) ON DELETE CASCADE -- Cascading delete on game removal
);

-- Table to store game outcomes
CREATE TABLE GameOutcomes (
    outcome_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each game outcome
    player_id INT NOT NULL,                     -- Foreign key referencing Players table
    game_id INT NOT NULL,                       -- Foreign key referencing Games table
    bet_amount DECIMAL(10, 2) NOT NULL,        -- Amount bet on the game
    win_amount DECIMAL(10, 2) NOT NULL DEFAULT 0.00, -- Amount won from the game
    outcome_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the outcome was recorded
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE, -- Cascading delete on player removal
    FOREIGN KEY (game_id) REFERENCES Games(game_id) ON DELETE CASCADE -- Cascading delete on game removal
);

-- Indexes for performance optimization
CREATE INDEX idx_player_id ON PlayerStats(player_id);
CREATE INDEX idx_game_id ON PlayerStats(game_id);
CREATE INDEX idx_outcome_player ON GameOutcomes(player_id);
CREATE INDEX idx_outcome_game ON GameOutcomes(game_id);
```
