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
-- SQL schema for Stellar Crop: Hikaye Tabanlı Görevler
-- This schema includes tables to store task descriptions, rewards, and player progress tracking.

-- Table to store tasks information
CREATE TABLE Tasks (
    TaskID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each task
    TaskName VARCHAR(255) NOT NULL,                -- Name of the task
    TaskDescription TEXT NOT NULL,                 -- Detailed description of the task
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the task was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the task was last updated
);

-- Table to store rewards associated with tasks
CREATE TABLE Rewards (
    RewardID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each reward
    TaskID INT NOT NULL,                           -- Foreign key referencing the task
    RewardType VARCHAR(255) NOT NULL,              -- Type of reward (e.g., item, experience points)
    RewardValue VARCHAR(255) NOT NULL,             -- Value or description of the reward
    FOREIGN KEY (TaskID) REFERENCES Tasks(TaskID) ON DELETE CASCADE -- Ensure rewards are deleted if the task is deleted
);

-- Table to track player progress on tasks
CREATE TABLE PlayerProgress (
    ProgressID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for progress entry
    PlayerID INT NOT NULL,                         -- Unique identifier for the player
    TaskID INT NOT NULL,                           -- Foreign key referencing the task
    ProgressStatus ENUM('NotStarted', 'InProgress', 'Completed') NOT NULL DEFAULT 'NotStarted', -- Status of the progress
    ProgressUpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp for the progress
    FOREIGN KEY (TaskID) REFERENCES Tasks(TaskID) ON DELETE CASCADE -- Ensure progress is deleted if the task is deleted
);

-- Indexes for faster lookup
CREATE INDEX idx_TaskName ON Tasks(TaskName);        -- Index on the task name for quicker searches
CREATE INDEX idx_PlayerTask ON PlayerProgress(PlayerID, TaskID); -- Composite index for player-task associations
```
