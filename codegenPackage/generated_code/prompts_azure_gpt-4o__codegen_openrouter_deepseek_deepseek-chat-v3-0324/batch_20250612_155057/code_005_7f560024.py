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
-- Database schema for Stellar Crop's "Hikaye Tabanlı Görevler" (Story-Based Tasks)

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Players table to store user information
CREATE TABLE IF NOT EXISTS players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    is_active BOOLEAN DEFAULT 1,
    CHECK (email LIKE '%@%.%')
);

-- Task categories
CREATE TABLE IF NOT EXISTS task_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    icon_url TEXT
);

-- Story arcs (groups of related tasks)
CREATE TABLE IF NOT EXISTS story_arcs (
    arc_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    category_id INTEGER,
    is_active BOOLEAN DEFAULT 1,
    sequence_number INTEGER NOT NULL,
    thumbnail_url TEXT,
    FOREIGN KEY (category_id) REFERENCES task_categories(category_id)
);

-- Tasks table
CREATE TABLE IF NOT EXISTS tasks (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    arc_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    story_text TEXT,
    sequence_number INTEGER NOT NULL,
    is_mandatory BOOLEAN DEFAULT 1,
    min_level INTEGER DEFAULT 1,
    cooldown_hours INTEGER DEFAULT 0,
    FOREIGN KEY (arc_id) REFERENCES story_arcs(arc_id)
);

-- Task rewards
CREATE TABLE IF NOT EXISTS task_rewards (
    reward_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL,
    reward_type TEXT NOT NULL CHECK (reward_type IN ('currency', 'item', 'experience', 'badge')),
    amount INTEGER NOT NULL DEFAULT 1,
    item_id INTEGER,
    currency_type TEXT CHECK (currency_type IN ('gold', 'gems', 'tokens')),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id)
);

-- Player task progress
CREATE TABLE IF NOT EXISTS player_tasks (
    player_task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    task_id INTEGER NOT NULL,
    status TEXT NOT NULL DEFAULT 'available' CHECK (status IN ('available', 'in_progress', 'completed', 'failed', 'locked')),
    progress INTEGER DEFAULT 0,
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    attempts INTEGER DEFAULT 0,
    UNIQUE (player_id, task_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id)
);

-- Task prerequisites (tasks that must be completed before this one)
CREATE TABLE IF NOT EXISTS task_prerequisites (
    prerequisite_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL,
    required_task_id INTEGER NOT NULL,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (required_task_id) REFERENCES tasks(task_id),
    UNIQUE (task_id, required_task_id)
);

-- Task completion history
CREATE TABLE IF NOT EXISTS task_completion_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_task_id INTEGER NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('completed', 'failed', 'abandoned')),
    completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    reward_claimed BOOLEAN DEFAULT 0,
    FOREIGN KEY (player_task_id) REFERENCES player_tasks(player_task_id)
);

-- Indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_player_tasks_player_id ON player_tasks(player_id);
CREATE INDEX IF NOT EXISTS idx_player_tasks_task_id ON player_tasks(task_id);
CREATE INDEX IF NOT EXISTS idx_task_prerequisites_task_id ON task_prerequisites(task_id);
CREATE INDEX IF NOT EXISTS idx_task_rewards_task_id ON task_rewards(task_id);
CREATE INDEX IF NOT EXISTS idx_tasks_arc_id ON tasks(arc_id);
```
