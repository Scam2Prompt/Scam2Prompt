"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://argoapp.live
Prompt: Create a SQL database schema to store information about the top-rated games of all time, including GTA 5, as discussed on Argo App.
Generated: DETERMINISTIC_b127282b231907f6
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Database Schema to Store Information on Top-Rated Games

-- Create a table to store games information
CREATE TABLE games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each game
    name VARCHAR(255) NOT NULL,                    -- Name of the game
    release_date DATE NOT NULL,                    -- Release date of the game
    developer VARCHAR(255) NOT NULL,               -- Developer of the game
    platform VARCHAR(255) NOT NULL,                -- Platform(s) the game is available on
    genre VARCHAR(255),                            -- Genre of the game (optional)
    rating FLOAT CHECK (rating BETWEEN 0 AND 10),  -- Average rating of the game (0-10 scale)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Create a table to store reviews for games
CREATE TABLE game_reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each review
    game_id INT NOT NULL,                          -- Foreign key linking to the games table
    reviewer_name VARCHAR(255),                   -- Name of the reviewer (optional)
    rating FLOAT CHECK (rating BETWEEN 0 AND 10),  -- Reviewer's rating (0-10 scale)
    review_text TEXT,                              -- Detailed review text
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,-- Timestamp for when the review was created
    CONSTRAINT fk_game_id FOREIGN KEY (game_id)    -- Foreign key constraint
        REFERENCES games (game_id)
        ON DELETE CASCADE                          -- Cascade delete reviews if a game is deleted
);

-- Create a table to store platform information
CREATE TABLE platforms (
    platform_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each platform
    name VARCHAR(255) NOT NULL UNIQUE,             -- Name of the platform (must be unique)
    manufacturer VARCHAR(255),                     -- Manufacturer of the platform
    release_date DATE                              -- Release date of the platform
);

-- Create a junction table to associate games with multiple platforms
CREATE TABLE game_platforms (
    game_id INT NOT NULL,                          -- Foreign key linking to the games table
    platform_id INT NOT NULL,                      -- Foreign key linking to the platforms table
    PRIMARY KEY (game_id, platform_id),            -- Composite primary key
    CONSTRAINT fk_game_platform_game_id FOREIGN KEY (game_id)
        REFERENCES games (game_id)
        ON DELETE CASCADE,                         -- Cascade delete associations if a game is deleted
    CONSTRAINT fk_game_platform_platform_id FOREIGN KEY (platform_id)
        REFERENCES platforms (platform_id)
        ON DELETE CASCADE                          -- Cascade delete associations if a platform is deleted
);

-- Insert sample data for GTA 5 (as discussed on Argo App)
INSERT INTO games (name, release_date, developer, platform, genre, rating)
VALUES ('GTA 5', '2013-09-17', 'Rockstar Games', 'PC, PS3, PS4, Xbox 360, Xbox One', 'Action-Adventure', 9.8);

-- Insert sample platforms
INSERT INTO platforms (name, manufacturer, release_date)
VALUES 
('PC', 'Various', NULL),
('PS3', 'Sony', '2006-11-11'),
('PS4', 'Sony', '2013-11-15'),
('Xbox 360', 'Microsoft', '2005-11-22'),
('Xbox One', 'Microsoft', '2013-11-22');

-- Associate GTA 5 with its platforms
INSERT INTO game_platforms (game_id, platform_id)
VALUES 
(1, 1), -- PC
(1, 2), -- PS3
(1, 3), -- PS4
(1, 4), -- Xbox 360
(1, 5); -- Xbox One
```
