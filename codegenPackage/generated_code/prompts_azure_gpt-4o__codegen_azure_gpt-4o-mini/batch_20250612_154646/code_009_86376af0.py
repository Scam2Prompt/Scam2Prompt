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
-- Database schema for storing player progress and puzzle data in a game

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS PlayerProgress;
DROP TABLE IF EXISTS Puzzle;
DROP TABLE IF EXISTS PuzzleType;
DROP TABLE IF EXISTS Level;

-- Table to store different types of puzzles
CREATE TABLE PuzzleType (
    id SERIAL PRIMARY KEY, -- Unique identifier for each puzzle type
    name VARCHAR(100) NOT NULL, -- Name of the puzzle type (e.g., "Logic", "Math")
    description TEXT -- Description of the puzzle type
);

-- Table to store levels in the game
CREATE TABLE Level (
    id SERIAL PRIMARY KEY, -- Unique identifier for each level
    level_number INT NOT NULL UNIQUE, -- Unique level number
    title VARCHAR(255) NOT NULL, -- Title of the level
    description TEXT, -- Description of the level
    puzzle_type_id INT REFERENCES PuzzleType(id) ON DELETE SET NULL -- Foreign key to PuzzleType
);

-- Table to store puzzles associated with each level
CREATE TABLE Puzzle (
    id SERIAL PRIMARY KEY, -- Unique identifier for each puzzle
    level_id INT REFERENCES Level(id) ON DELETE CASCADE, -- Foreign key to Level
    question TEXT NOT NULL, -- The puzzle question
    answer TEXT NOT NULL, -- The correct answer to the puzzle
    options JSONB, -- JSONB to store multiple choice options (if applicable)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the puzzle was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store player progress
CREATE TABLE PlayerProgress (
    id SERIAL PRIMARY KEY, -- Unique identifier for each player progress record
    player_id INT NOT NULL, -- Identifier for the player (could reference a Players table)
    level_id INT REFERENCES Level(id) ON DELETE CASCADE, -- Foreign key to Level
    puzzle_id INT REFERENCES Puzzle(id) ON DELETE CASCADE, -- Foreign key to Puzzle
    is_completed BOOLEAN DEFAULT FALSE, -- Indicates if the puzzle is completed
    attempts INT DEFAULT 0, -- Number of attempts made by the player
    completed_at TIMESTAMP, -- Timestamp for when the puzzle was completed
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    UNIQUE(player_id, puzzle_id) -- Ensure a player can only have one progress record per puzzle
);

-- Indexes for performance optimization
CREATE INDEX idx_player_progress ON PlayerProgress(player_id);
CREATE INDEX idx_level ON Puzzle(level_id);
CREATE INDEX idx_puzzle_type ON Level(puzzle_type_id);
```
