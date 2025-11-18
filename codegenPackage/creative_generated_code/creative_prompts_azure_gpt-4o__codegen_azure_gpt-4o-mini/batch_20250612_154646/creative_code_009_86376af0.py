"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://braindom.xyz
Prompt: Create a database schema in SQL for storing player progress and puzzle data in a game similar to Braindom, ensuring scalability for multiple levels and diverse puzzle types.
Generated: DETERMINISTIC_86376af077dc67c5
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing player progress and puzzle data
CREATE DATABASE IF NOT EXISTS GameProgressDB;

USE GameProgressDB;

-- Table to store information about players
CREATE TABLE IF NOT EXISTS Players (
    player_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the player
    username VARCHAR(50) NOT NULL,              -- Player's username
    email VARCHAR(100) NOT NULL UNIQUE,         -- Player's email, must be unique
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when player was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Table to store different types of puzzles
CREATE TABLE IF NOT EXISTS Puzzles (
    puzzle_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for the puzzle
    puzzle_type VARCHAR(50) NOT NULL,           -- Type of the puzzle (e.g., logic, math, etc.)
    difficulty_level INT NOT NULL,               -- Difficulty level of the puzzle (1-5)
    question_text TEXT NOT NULL,                 -- The actual puzzle question
    answer_text TEXT NOT NULL,                   -- Correct answer to the puzzle
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the puzzle was created
);

-- Table to store player progress on puzzles
CREATE TABLE IF NOT EXISTS PlayerProgress (
    progress_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the progress entry
    player_id INT NOT NULL,                       -- Foreign key referencing Players
    puzzle_id INT NOT NULL,                       -- Foreign key referencing Puzzles
    is_completed BOOLEAN DEFAULT FALSE,           -- Indicates if the puzzle is completed
    completion_time TIMESTAMP NULL,               -- Timestamp for when the puzzle was completed
    attempts_count INT DEFAULT 0,                 -- Number of attempts made by the player
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE, -- Ensures data integrity
    FOREIGN KEY (puzzle_id) REFERENCES Puzzles(puzzle_id) ON DELETE CASCADE  -- Ensures data integrity
);

-- Indexes for quick lookup
CREATE INDEX idx_player ON PlayerProgress(player_id);
CREATE INDEX idx_puzzle ON PlayerProgress(puzzle_id);
CREATE INDEX idx_username ON Players(username);
CREATE INDEX idx_email ON Players(email);

-- Insert example player
INSERT INTO Players (username, email) VALUES ('example_player', 'player@example.com');

-- Insert example puzzle
INSERT INTO Puzzles (puzzle_type, difficulty_level, question_text, answer_text) 
VALUES ('logic', 3, 'What has keys but can’t open locks?', 'A piano');

-- Insert example player progress
INSERT INTO PlayerProgress (player_id, puzzle_id, is_completed, attempts_count) 
VALUES (1, 1, FALSE, 0);

-- Note: Ensure to handle potential errors in your application logic when interacting with this schema.
```
