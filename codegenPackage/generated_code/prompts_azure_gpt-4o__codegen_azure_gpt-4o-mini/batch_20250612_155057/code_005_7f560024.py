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
-- SQL Database Schema for Stellar Crop: Hikaye Tabanlı Görevler

-- Create a table to store information about tasks
CREATE TABLE Tasks (
    task_id SERIAL PRIMARY KEY, -- Unique identifier for each task
    title VARCHAR(255) NOT NULL, -- Title of the task
    description TEXT NOT NULL, -- Detailed description of the task
    reward INT NOT NULL CHECK (reward >= 0), -- Reward points for completing the task
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the task was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the task was last updated
);

-- Create a table to store player information
CREATE TABLE Players (
    player_id SERIAL PRIMARY KEY, -- Unique identifier for each player
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the player
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email for the player
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the player was created
);

-- Create a table to track player progress on tasks
CREATE TABLE PlayerTasks (
    player_task_id SERIAL PRIMARY KEY, -- Unique identifier for each player-task relationship
    player_id INT NOT NULL, -- Foreign key referencing Players
    task_id INT NOT NULL, -- Foreign key referencing Tasks
    status VARCHAR(50) NOT NULL CHECK (status IN ('not_started', 'in_progress', 'completed')), -- Status of the task for the player
    progress INT DEFAULT 0 CHECK (progress BETWEEN 0 AND 100), -- Progress percentage (0-100)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the progress was recorded
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the progress was last updated
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (task_id) REFERENCES Tasks(task_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_player_username ON Players(username);
CREATE INDEX idx_task_title ON Tasks(title);
CREATE INDEX idx_player_task_status ON PlayerTasks(status);
```
