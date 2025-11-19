"""
Generated Code Metadata:
========================
Original URL: https://todaythegames.com
Prompt: Design a database schema for storing user data, game statistics, and leaderboard information for a social casino platform similar to todaythegames.com.
Generated: DETERMINISTIC_53d93363bbaccf3d
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a social casino platform

-- Table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    last_login TIMESTAMP                   -- Last login timestamp
);

-- Table to store game information
CREATE TABLE Games (
    game_id SERIAL PRIMARY KEY,            -- Unique identifier for each game
    game_name VARCHAR(100) NOT NULL,      -- Name of the game
    game_type VARCHAR(50) NOT NULL,       -- Type of the game (e.g., slot, poker)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Game creation timestamp
);

-- Table to store user game statistics
CREATE TABLE UserGameStats (
    stat_id SERIAL PRIMARY KEY,            -- Unique identifier for each stat entry
    user_id INT NOT NULL,                  -- Foreign key referencing Users
    game_id INT NOT NULL,                  -- Foreign key referencing Games
    total_played INT DEFAULT 0,            -- Total number of times the user played the game
    total_won INT DEFAULT 0,               -- Total amount won by the user in the game
    total_lost INT DEFAULT 0,              -- Total amount lost by the user in the game
    last_played TIMESTAMP,                 -- Last time the user played the game
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensures data integrity
    FOREIGN KEY (game_id) REFERENCES Games(game_id) ON DELETE CASCADE  -- Ensures data integrity
);

-- Table to store leaderboard information
CREATE TABLE Leaderboard (
    leaderboard_id SERIAL PRIMARY KEY,     -- Unique identifier for each leaderboard entry
    game_id INT NOT NULL,                  -- Foreign key referencing Games
    user_id INT NOT NULL,                  -- Foreign key referencing Users
    score INT NOT NULL,                    -- Score achieved by the user in the game
    rank INT NOT NULL,                     -- Rank of the user in the leaderboard
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the leaderboard entry
    FOREIGN KEY (game_id) REFERENCES Games(game_id) ON DELETE CASCADE, -- Ensures data integrity
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE  -- Ensures data integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_username ON Users(username);
CREATE INDEX idx_email ON Users(email);
CREATE INDEX idx_game_id ON UserGameStats(game_id);
CREATE INDEX idx_user_id ON UserGameStats(user_id);
CREATE INDEX idx_leaderboard_game_id ON Leaderboard(game_id);
CREATE INDEX idx_leaderboard_user_id ON Leaderboard(user_id);
```
