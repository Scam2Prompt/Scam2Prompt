"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://todaythegames.com
Prompt: Design a database schema for storing user data, game statistics, and leaderboard information for a social casino platform similar to todaythegames.com.
Generated: DETERMINISTIC_53d93363bbaccf3d
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a social casino platform

-- Create a table to store user data
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,           -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- User's username, must be unique
    email VARCHAR(100) NOT NULL UNIQUE,    -- User's email address, must be unique
    password_hash VARCHAR(255) NOT NULL,   -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    last_login TIMESTAMP,                   -- Timestamp of the last login
    is_active BOOLEAN DEFAULT TRUE          -- Active status of the user account
);

-- Create a table to store game statistics for each user
CREATE TABLE GameStatistics (
    stat_id SERIAL PRIMARY KEY,             -- Unique identifier for each statistic record
    user_id INT REFERENCES Users(user_id) ON DELETE CASCADE, -- Foreign key to Users table
    game_name VARCHAR(50) NOT NULL,        -- Name of the game
    games_played INT DEFAULT 0,            -- Total number of games played by the user
    wins INT DEFAULT 0,                     -- Total number of wins
    losses INT DEFAULT 0,                   -- Total number of losses
    total_score INT DEFAULT 0,              -- Total score accumulated by the user
    last_played TIMESTAMP                   -- Timestamp of when the user last played the game
);

-- Create a table to store leaderboard information
CREATE TABLE Leaderboard (
    leaderboard_id SERIAL PRIMARY KEY,      -- Unique identifier for each leaderboard entry
    game_name VARCHAR(50) NOT NULL,        -- Name of the game
    user_id INT REFERENCES Users(user_id) ON DELETE CASCADE, -- Foreign key to Users table
    score INT NOT NULL,                     -- User's score for the game
    rank INT NOT NULL,                      -- User's rank in the leaderboard for the game
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the leaderboard entry was created
);

-- Create an index on the leaderboard table for faster score lookups
CREATE INDEX idx_leaderboard_game_user ON Leaderboard (game_name, user_id);

-- Example of how to insert a new user (error handling should be implemented in application logic)
-- INSERT INTO Users (username, email, password_hash) VALUES ('exampleUser', 'user@example.com', 'hashed_password_here');

-- Example of how to insert game statistics for a user
-- INSERT INTO GameStatistics (user_id, game_name, games_played, wins, losses, total_score) 
-- VALUES (1, 'Poker', 100, 55, 45, 1500);

-- Example of how to insert leaderboard information
-- INSERT INTO Leaderboard (game_name, user_id, score, rank) 
-- VALUES ('Poker', 1, 1500, 1);
```
