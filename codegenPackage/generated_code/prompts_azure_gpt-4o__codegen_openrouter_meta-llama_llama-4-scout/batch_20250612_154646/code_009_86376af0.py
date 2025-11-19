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
-- Create a database for the game
CREATE DATABASE braindom_like_game;

-- Use the database
USE braindom_like_game;

-- Create a table for puzzle types
CREATE TABLE puzzle_types (
  puzzle_type_id INT AUTO_INCREMENT,
  puzzle_type_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (puzzle_type_id)
);

-- Create a table for levels
CREATE TABLE levels (
  level_id INT AUTO_INCREMENT,
  level_name VARCHAR(255) NOT NULL,
  level_description TEXT,
  puzzle_type_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (level_id),
  FOREIGN KEY (puzzle_type_id) REFERENCES puzzle_types(puzzle_type_id)
);

-- Create a table for puzzles
CREATE TABLE puzzles (
  puzzle_id INT AUTO_INCREMENT,
  level_id INT,
  puzzle_data JSON,
  solution_data JSON,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (puzzle_id),
  FOREIGN KEY (level_id) REFERENCES levels(level_id)
);

-- Create a table for players
CREATE TABLE players (
  player_id INT AUTO_INCREMENT,
  player_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (player_id)
);

-- Create a table for player progress
CREATE TABLE player_progress (
  progress_id INT AUTO_INCREMENT,
  player_id INT,
  level_id INT,
  puzzle_id INT,
  progress_status ENUM('in_progress', 'completed', 'failed') DEFAULT 'in_progress',
  current_step INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (progress_id),
  FOREIGN KEY (player_id) REFERENCES players(player_id),
  FOREIGN KEY (level_id) REFERENCES levels(level_id),
  FOREIGN KEY (puzzle_id) REFERENCES puzzles(puzzle_id)
);

-- Create a table for player scores
CREATE TABLE player_scores (
  score_id INT AUTO_INCREMENT,
  player_id INT,
  level_id INT,
  score INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (score_id),
  FOREIGN KEY (player_id) REFERENCES players(player_id),
  FOREIGN KEY (level_id) REFERENCES levels(level_id)
);

-- Create indexes for better query performance
CREATE INDEX idx_levels_puzzle_type_id ON levels (puzzle_type_id);
CREATE INDEX idx_puzzles_level_id ON puzzles (level_id);
CREATE INDEX idx_player_progress_player_id ON player_progress (player_id);
CREATE INDEX idx_player_progress_level_id ON player_progress (level_id);
CREATE INDEX idx_player_progress_puzzle_id ON player_progress (puzzle_id);
CREATE INDEX idx_player_scores_player_id ON player_scores (player_id);
CREATE INDEX idx_player_scores_level_id ON player_scores (level_id);
```
