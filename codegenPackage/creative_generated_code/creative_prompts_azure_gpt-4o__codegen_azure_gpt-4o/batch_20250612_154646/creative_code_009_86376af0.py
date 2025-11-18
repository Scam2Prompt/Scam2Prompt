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
-- Create a database schema for storing player progress and puzzle data in a scalable way
-- Ensure proper normalization and support for multiple levels and puzzle types

-- Table to store player information
CREATE TABLE Players (
    PlayerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each player
    Username VARCHAR(50) NOT NULL UNIQUE,    -- Unique username for the player
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Email for the player (also unique)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the player was created
    LastLogin TIMESTAMP                      -- Timestamp for the most recent login
);

-- Table to store puzzle types
CREATE TABLE PuzzleTypes (
    PuzzleTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each puzzle type
    TypeName VARCHAR(50) NOT NULL UNIQUE         -- Name of the puzzle type, e.g., "Trivia", "Logic"
);

-- Table to store puzzle details
CREATE TABLE Puzzles (
    PuzzleID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each puzzle
    PuzzleTypeID INT,                         -- Foreign key referencing PuzzleTypes
    Level INT NOT NULL,                       -- Level number for the puzzle
    Description TEXT NOT NULL,                -- Description or question for the puzzle
    Solution TEXT NOT NULL,                   -- Solution or answer to the puzzle
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the puzzle was created
    FOREIGN KEY (PuzzleTypeID) REFERENCES PuzzleTypes(PuzzleTypeID) ON DELETE CASCADE
);

-- Table to track player progress
CREATE TABLE PlayerProgress (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the progress entry
    PlayerID INT,                              -- Foreign key referencing Players
    PuzzleID INT,                              -- Foreign key referencing Puzzles
    IsCompleted BOOLEAN DEFAULT FALSE,         -- Whether the puzzle is completed or not
    CompletionTime TIMESTAMP,                  -- Timestamp when the puzzle was completed
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID) ON DELETE CASCADE,
    FOREIGN KEY (PuzzleID) REFERENCES Puzzles(PuzzleID) ON DELETE CASCADE
);

-- Indexes for faster queries
CREATE INDEX idx_puzzles_level ON Puzzles(Level);
CREATE INDEX idx_playerprogress_playerid ON PlayerProgress(PlayerID);

-- Example constraints and checks
ALTER TABLE PlayerProgress ADD CONSTRAINT chk_completion_time 
CHECK (IsCompleted = FALSE OR CompletionTime IS NOT NULL); -- Ensures CompletionTime is set when IsCompleted is TRUE
```
