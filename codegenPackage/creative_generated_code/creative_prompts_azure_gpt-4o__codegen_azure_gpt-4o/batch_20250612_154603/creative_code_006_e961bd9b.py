"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yomixmixer.com
Prompt: Create a database schema for tracking "Cross-Game Progression" levels across multiple games, as outlined in Kramat77's system.
Generated: DETERMINISTIC_e961bd9bf505152d
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Cross-Game Progression Database Schema
-- This schema tracks user progression levels across multiple games.

-- Table: Users
-- Stores user information.
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the user
    Username VARCHAR(100) NOT NULL UNIQUE, -- Unique username for the user
    Email VARCHAR(255) NOT NULL UNIQUE,    -- Email for the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the user was created
);

-- Table: Games
-- Stores information about games being tracked.
CREATE TABLE Games (
    GameID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the game
    GameName VARCHAR(255) NOT NULL UNIQUE, -- Name of the game
    Developer VARCHAR(255),                -- Developer of the game
    ReleaseDate DATE,                      -- Release date of the game
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the game was added
);

-- Table: ProgressionLevels
-- Stores information about progression levels available in a game.
CREATE TABLE ProgressionLevels (
    LevelID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the progression level
    GameID INT NOT NULL,                    -- Foreign key linking to Games table
    LevelName VARCHAR(255) NOT NULL,        -- Name of the progression level
    LevelDescription TEXT,                  -- Description of the progression level
    PointsRequired INT NOT NULL,            -- Points required to achieve this level
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the level was added
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE -- Cascade deletion
);

-- Table: UserProgression
-- Tracks the progression of each user across different games.
CREATE TABLE UserProgression (
    ProgressionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for this record
    UserID INT NOT NULL,                          -- Foreign key linking to Users table
    GameID INT NOT NULL,                          -- Foreign key linking to Games table
    LevelID INT NOT NULL,                         -- Foreign key linking to ProgressionLevels table
    ProgressPoints INT NOT NULL DEFAULT 0,        -- Points accumulated by the user in the game
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade deletion
    FOREIGN KEY (GameID) REFERENCES Games(GameID) ON DELETE CASCADE, -- Cascade deletion
    FOREIGN KEY (LevelID) REFERENCES ProgressionLevels(LevelID) ON DELETE SET NULL -- Set NULL if level deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_UserProgression_User_Game ON UserProgression (UserID, GameID);
CREATE INDEX idx_ProgressionLevels_Game ON ProgressionLevels (GameID);

-- Example: Adding additional constraints for data integrity
-- Ensures ProgressPoints cannot be negative
ALTER TABLE UserProgression
ADD CONSTRAINT chk_ProgressPoints_Positive CHECK (ProgressPoints >= 0);

-- End of Cross-Game Progression Database Schema
```
