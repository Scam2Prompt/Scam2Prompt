"""
Generated Code Metadata:
========================
Original URL: https://stellar-neurongate.xyz
Prompt: Given the variety of games on Zeus Fortune, such as Crazy Time and Book of Ra, design a database schema to store game metadata, user progress, and rewards.
Generated: DETERMINISTIC_3c1840590d38c1b6
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Zeus Fortune platform

-- Table to store metadata about games
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each game
    Name VARCHAR(255) NOT NULL,            -- Name of the game (e.g., Crazy Time, Book of Ra)
    Description TEXT,                      -- Brief description of the game
    Genre VARCHAR(100),                    -- Genre of the game (e.g., Casino, Adventure)
    ReleaseDate DATE,                      -- Release date of the game
    Developer VARCHAR(255),                -- Developer of the game
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the game was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store user information and progress in games
CREATE TABLE UserProgress (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each progress record
    UserID INT NOT NULL,                       -- Foreign key to identify the user
    GameID INT NOT NULL,                       -- Foreign key to identify the game
    Level INT DEFAULT 1,                       -- Current level of the user in the game
    Score INT DEFAULT 0,                       -- Current score of the user in the game
    LastPlayed TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the last time the user played the game
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the progress record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID), -- Reference to Users table
    FOREIGN KEY (GameID) REFERENCES Games(GameID) -- Reference to Games table
);

-- Table to store rewards earned by users
CREATE TABLE Rewards (
    RewardID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each reward
    UserID INT NOT NULL,                     -- Foreign key to identify the user
    GameID INT NOT NULL,                     -- Foreign key to identify the game
    RewardName VARCHAR(255) NOT NULL,        -- Name of the reward (e.g., Bonus Coins, Free Spins)
    RewardType VARCHAR(100),                 -- Type of reward (e.g., Coins, Spins, Items)
    Quantity INT DEFAULT 1,                  -- Quantity of the reward
    EarnedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the reward was earned
    FOREIGN KEY (UserID) REFERENCES Users(UserID), -- Reference to Users table
    FOREIGN KEY (GameID) REFERENCES Games(GameID) -- Reference to Games table
);

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Username VARCHAR(255) NOT NULL UNIQUE, -- Unique username for the user
    Email VARCHAR(255) NOT NULL UNIQUE,    -- Unique email for the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Indexes for optimization
CREATE INDEX idx_user_game_progress ON UserProgress(UserID, GameID);
CREATE INDEX idx_user_game_rewards ON Rewards(UserID, GameID);
```
