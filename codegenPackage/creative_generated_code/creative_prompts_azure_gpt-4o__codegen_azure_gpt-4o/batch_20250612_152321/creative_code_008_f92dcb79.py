"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memefi-club.pages.dev
Prompt: Create a database schema in SQL to store MemeFi player data, including clan affiliations, earned rewards, and leaderboard positions.
Generated: DETERMINISTIC_f92dcb798b076074
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for MemeFi player data

-- Ensure the database can handle proper charset and collation
CREATE DATABASE IF NOT EXISTS MemeFiGame
CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;

USE MemeFiGame;

-- Table to store player information
CREATE TABLE IF NOT EXISTS Players (
    PlayerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each player
    Username VARCHAR(50) NOT NULL UNIQUE,    -- Player's username, must be unique
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Player's email, must be unique
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the player was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Table to store clan information
CREATE TABLE IF NOT EXISTS Clans (
    ClanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each clan
    ClanName VARCHAR(50) NOT NULL UNIQUE,  -- Clan name, must be unique
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the clan was created
    LeaderID INT NOT NULL, -- Foreign key referencing the clan leader (PlayerID)
    FOREIGN KEY (LeaderID) REFERENCES Players(PlayerID) ON DELETE CASCADE
);

-- Junction table to associate players and clans
CREATE TABLE IF NOT EXISTS PlayerClans (
    PlayerClanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the association
    PlayerID INT NOT NULL,      -- Foreign key referencing the player
    ClanID INT NOT NULL,        -- Foreign key referencing the clan
    JoinedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the player joined the clan
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID) ON DELETE CASCADE,
    FOREIGN KEY (ClanID) REFERENCES Clans(ClanID) ON DELETE CASCADE
);

-- Table to store rewards earned by players
CREATE TABLE IF NOT EXISTS Rewards (
    RewardID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the reward
    RewardName VARCHAR(100) NOT NULL,        -- Name of the reward
    RewardDescription TEXT,                  -- Description of the reward
    RewardPoints INT NOT NULL,               -- Points associated with the reward
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- When the reward was created
);

-- Table to associate players with earned rewards
CREATE TABLE IF NOT EXISTS PlayerRewards (
    PlayerRewardID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the association
    PlayerID INT NOT NULL,      -- Foreign key referencing the player
    RewardID INT NOT NULL,      -- Foreign key referencing the reward
    EarnedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the reward was earned
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID) ON DELETE CASCADE,
    FOREIGN KEY (RewardID) REFERENCES Rewards(RewardID) ON DELETE CASCADE
);

-- Table to store leaderboard positions
CREATE TABLE IF NOT EXISTS Leaderboard (
    LeaderboardID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each leaderboard entry
    PlayerID INT NOT NULL,        -- Foreign key referencing the player
    Rank INT NOT NULL,            -- Player's rank on the leaderboard
    Score INT NOT NULL,           -- Player's score
    RecordedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the leaderboard entry was recorded
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_player_email ON Players(Email);
CREATE INDEX idx_clan_name ON Clans(ClanName);
CREATE INDEX idx_reward_name ON Rewards(RewardName);
CREATE INDEX idx_leaderboard_rank ON Leaderboard(Rank);

-- Done!
```
