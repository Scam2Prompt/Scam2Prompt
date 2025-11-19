"""
Generated Code Metadata:
========================
Original URL: https://braindom.xyz
Prompt: Create a database schema in SQL for storing player progress and puzzle data in a game similar to Braindom, ensuring scalability for multiple levels and diverse puzzle types.
Generated: DETERMINISTIC_86376af077dc67c5
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a puzzle game similar to Braindom
-- Supports multiple levels, diverse puzzle types, and player progress tracking

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Players table to store user information
CREATE TABLE IF NOT EXISTS players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    total_score INTEGER DEFAULT 0,
    coins INTEGER DEFAULT 0,
    avatar_id INTEGER DEFAULT 1,
    is_active BOOLEAN DEFAULT TRUE,
    CHECK (email LIKE '%@%.%' OR email IS NULL)
);

-- Puzzle categories/types
CREATE TABLE IF NOT EXISTS puzzle_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    icon TEXT
);

-- Levels table
CREATE TABLE IF NOT EXISTS levels (
    level_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    level_number INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    required_score INTEGER DEFAULT 0,
    is_locked BOOLEAN DEFAULT TRUE,
    background_image TEXT,
    FOREIGN KEY (category_id) REFERENCES puzzle_categories(category_id),
    UNIQUE (category_id, level_number)
);

-- Puzzles table
CREATE TABLE IF NOT EXISTS puzzles (
    puzzle_id INTEGER PRIMARY KEY AUTOINCREMENT,
    level_id INTEGER NOT NULL,
    puzzle_number INTEGER NOT NULL,
    puzzle_type TEXT NOT NULL CHECK (puzzle_type IN ('riddle', 'math', 'pattern', 'memory', 'logic', 'word')),
    question TEXT NOT NULL,
    solution TEXT NOT NULL,
    hint TEXT,
    time_limit INTEGER, -- in seconds, NULL means no time limit
    base_score INTEGER NOT NULL,
    difficulty INTEGER CHECK (difficulty BETWEEN 1 AND 5),
    FOREIGN KEY (level_id) REFERENCES levels(level_id),
    UNIQUE (level_id, puzzle_number)
);

-- Puzzle options (for multiple choice puzzles)
CREATE TABLE IF NOT EXISTS puzzle_options (
    option_id INTEGER PRIMARY KEY AUTOINCREMENT,
    puzzle_id INTEGER NOT NULL,
    option_text TEXT NOT NULL,
    is_correct BOOLEAN NOT NULL,
    FOREIGN KEY (puzzle_id) REFERENCES puzzles(puzzle_id) ON DELETE CASCADE
);

-- Player progress tracking
CREATE TABLE IF NOT EXISTS player_progress (
    progress_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    level_id INTEGER NOT NULL,
    is_completed BOOLEAN DEFAULT FALSE,
    completion_date TIMESTAMP,
    best_score INTEGER DEFAULT 0,
    attempts INTEGER DEFAULT 0,
    stars_earned INTEGER DEFAULT 0 CHECK (stars_earned BETWEEN 0 AND 3),
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE,
    FOREIGN KEY (level_id) REFERENCES levels(level_id),
    UNIQUE (player_id, level_id)
);

-- Puzzle attempts tracking
CREATE TABLE IF NOT EXISTS puzzle_attempts (
    attempt_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    puzzle_id INTEGER NOT NULL,
    attempt_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    was_successful BOOLEAN NOT NULL,
    time_taken INTEGER, -- in seconds
    score_earned INTEGER,
    used_hint BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE,
    FOREIGN KEY (puzzle_id) REFERENCES puzzles(puzzle_id)
);

-- Player inventory (items, power-ups, etc.)
CREATE TABLE IF NOT EXISTS player_inventory (
    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    item_type TEXT NOT NULL CHECK (item_type IN ('hint', 'skip', 'time_boost', 'coin_multiplier')),
    quantity INTEGER DEFAULT 0 CHECK (quantity >= 0),
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE,
    UNIQUE (player_id, item_type)
);

-- Player achievements
CREATE TABLE IF NOT EXISTS achievements (
    achievement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    icon TEXT,
    score_reward INTEGER DEFAULT 0,
    coin_reward INTEGER DEFAULT 0
);

-- Player earned achievements
CREATE TABLE IF NOT EXISTS player_achievements (
    player_achievement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    achievement_id INTEGER NOT NULL,
    earned_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE,
    FOREIGN KEY (achievement_id) REFERENCES achievements(achievement_id),
    UNIQUE (player_id, achievement_id)
);

-- Daily challenges
CREATE TABLE IF NOT EXISTS daily_challenges (
    challenge_id INTEGER PRIMARY KEY AUTOINCREMENT,
    puzzle_id INTEGER NOT NULL,
    challenge_date DATE NOT NULL UNIQUE,
    reward_coins INTEGER DEFAULT 100,
    FOREIGN KEY (puzzle_id) REFERENCES puzzles(puzzle_id)
);

-- Player daily challenge participation
CREATE TABLE IF NOT EXISTS player_daily_challenges (
    participation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    challenge_id INTEGER NOT NULL,
    completion_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    was_successful BOOLEAN NOT NULL,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE,
    FOREIGN KEY (challenge_id) REFERENCES daily_challenges(challenge_id),
    UNIQUE (player_id, challenge_id)
);

-- Create indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_player_progress ON player_progress(player_id, level_id);
CREATE INDEX IF NOT EXISTS idx_puzzle_attempts ON puzzle_attempts(player_id, puzzle_id);
CREATE INDEX IF NOT EXISTS idx_puzzles_level ON puzzles(level_id);
CREATE INDEX IF NOT EXISTS idx_levels_category ON levels(category_id);
```
