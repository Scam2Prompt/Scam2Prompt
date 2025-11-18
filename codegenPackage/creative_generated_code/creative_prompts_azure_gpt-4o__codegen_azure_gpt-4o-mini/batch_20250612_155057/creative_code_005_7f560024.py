"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarcropgame.fun
Prompt: Write a SQL database schema for Stellar Crop to store data about "Hikaye Tabanlı Görevler," including task descriptions, rewards, and player progress tracking.
Generated: DETERMINISTIC_7f5600240d1e8101
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Creating the StellarCrop database schema for "Hikaye Tabanlı Görevler"

CREATE DATABASE StellarCrop;

USE StellarCrop;

-- Table to store information about tasks
CREATE TABLE Tasks (
    TaskID INT AUTO_INCREMENT PRIMARY KEY,             -- Unique identifier for each task
    TaskDescription TEXT NOT NULL,                      -- Description of the task
    Reward INT NOT NULL,                                -- Reward for completing the task
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp of when the task was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store player information
CREATE TABLE Players (
    PlayerID INT AUTO_INCREMENT PRIMARY KEY,            -- Unique identifier for each player
    PlayerName VARCHAR(100) NOT NULL UNIQUE,           -- Name of the player
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP      -- Timestamp of when the player was created
);

-- Table to track player progress on tasks
CREATE TABLE PlayerTaskProgress (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each progress record
    PlayerID INT NOT NULL,                               -- Foreign key referencing Players
    TaskID INT NOT NULL,                                 -- Foreign key referencing Tasks
    IsCompleted BOOLEAN DEFAULT FALSE,                  -- Boolean indicating whether the task is completed
    CompletionDate TIMESTAMP,                            -- Date of task completion
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (TaskID) REFERENCES Tasks(TaskID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexing for better performance in queries
CREATE INDEX idx_player_id ON PlayerTaskProgress(PlayerID);
CREATE INDEX idx_task_id ON PlayerTaskProgress(TaskID);
```
