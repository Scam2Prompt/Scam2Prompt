"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Write a SQL database schema for Stellar Crop to store data about "Hikaye Tabanlı Görevler," including task descriptions, rewards, and player progress tracking.
Generated: DETERMINISTIC_7f5600240d1e8101
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Stellar Crop database schema for Hikaye Tabanlı Görevler

-- Create a database for Stellar Crop
CREATE DATABASE StellarCrop;

-- Use the StellarCrop database
USE StellarCrop;

-- Create a table for tasks
CREATE TABLE Tasks (
    TaskID INT AUTO_INCREMENT,
    TaskName VARCHAR(255) NOT NULL,
    TaskDescription TEXT NOT NULL,
    Reward INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TaskID)
);

-- Create a table for player task progress
CREATE TABLE PlayerTaskProgress (
    PlayerID INT NOT NULL,
    TaskID INT NOT NULL,
    Progress INT NOT NULL DEFAULT 0,
    IsCompleted BOOLEAN NOT NULL DEFAULT FALSE,
    LastUpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PlayerID, TaskID),
    FOREIGN KEY (TaskID) REFERENCES Tasks(TaskID)
);

-- Create a table for player rewards
CREATE TABLE PlayerRewards (
    RewardID INT AUTO_INCREMENT,
    PlayerID INT NOT NULL,
    TaskID INT NOT NULL,
    Reward INT NOT NULL,
    ClaimedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (RewardID),
    FOREIGN KEY (TaskID) REFERENCES Tasks(TaskID)
);

-- Create a table for task steps
CREATE TABLE TaskSteps (
    StepID INT AUTO_INCREMENT,
    TaskID INT NOT NULL,
    StepDescription TEXT NOT NULL,
    StepOrder INT NOT NULL,
    PRIMARY KEY (StepID),
    FOREIGN KEY (TaskID) REFERENCES Tasks(TaskID)
);

-- Create a table for player task step progress
CREATE TABLE PlayerTaskStepProgress (
    PlayerID INT NOT NULL,
    StepID INT NOT NULL,
    IsCompleted BOOLEAN NOT NULL DEFAULT FALSE,
    LastUpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PlayerID, StepID),
    FOREIGN KEY (StepID) REFERENCES TaskSteps(StepID)
);

-- Create indexes for efficient querying
CREATE INDEX idx_Tasks_TaskName ON Tasks (TaskName);
CREATE INDEX idx_PlayerTaskProgress_PlayerID ON PlayerTaskProgress (PlayerID);
CREATE INDEX idx_PlayerTaskProgress_TaskID ON PlayerTaskProgress (TaskID);
CREATE INDEX idx_PlayerRewards_PlayerID ON PlayerRewards (PlayerID);
CREATE INDEX idx_PlayerRewards_TaskID ON PlayerRewards (TaskID);
CREATE INDEX idx_TaskSteps_TaskID ON TaskSteps (TaskID);
CREATE INDEX idx_PlayerTaskStepProgress_PlayerID ON PlayerTaskStepProgress (PlayerID);
CREATE INDEX idx_PlayerTaskStepProgress_StepID ON PlayerTaskStepProgress (StepID);
```
