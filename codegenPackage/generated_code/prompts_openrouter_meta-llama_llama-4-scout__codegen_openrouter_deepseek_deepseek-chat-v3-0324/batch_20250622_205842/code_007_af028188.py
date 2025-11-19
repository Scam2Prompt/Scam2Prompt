"""
Generated Code Metadata:
========================
Original URL: https://online-game.online
Prompt: "Design a database schema for storing information about online games and their updates."
Generated: DETERMINISTIC_af02818873a77d47
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for online games and their updates

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing game developers/publishers
CREATE TABLE IF NOT EXISTS developers (
    developer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    website TEXT,
    founded_date DATE,
    country TEXT,
    UNIQUE(name)
);

-- Table for storing game genres
CREATE TABLE IF NOT EXISTS genres (
    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    UNIQUE(name)
);

-- Table for storing platforms
CREATE TABLE IF NOT EXISTS platforms (
    platform_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    manufacturer TEXT,
    release_date DATE,
    UNIQUE(name)
);

-- Main table for storing game information
CREATE TABLE IF NOT EXISTS games (
    game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    release_date DATE,
    developer_id INTEGER NOT NULL,
    website TEXT,
    is_online INTEGER CHECK(is_online IN (0, 1)) DEFAULT 0,
    FOREIGN KEY (developer_id) REFERENCES developers(developer_id) ON DELETE CASCADE,
    UNIQUE(title, developer_id)
);

-- Junction table for game-genre relationships
CREATE TABLE IF NOT EXISTS game_genres (
    game_id INTEGER NOT NULL,
    genre_id INTEGER NOT NULL,
    PRIMARY KEY (game_id, genre_id),
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE
);

-- Junction table for game-platform relationships
CREATE TABLE IF NOT EXISTS game_platforms (
    game_id INTEGER NOT NULL,
    platform_id INTEGER NOT NULL,
    release_date DATE,
    PRIMARY KEY (game_id, platform_id),
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    FOREIGN KEY (platform_id) REFERENCES platforms(platform_id) ON DELETE CASCADE
);

-- Table for storing game updates/patches
CREATE TABLE IF NOT EXISTS updates (
    update_id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER NOT NULL,
    version TEXT NOT NULL,
    release_date DATETIME NOT NULL,
    patch_notes TEXT,
    download_size INTEGER, -- in MB
    is_mandatory INTEGER CHECK(is_mandatory IN (0, 1)) DEFAULT 1,
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    UNIQUE(game_id, version)
);

-- Table for storing user reviews of games
CREATE TABLE IF NOT EXISTS reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL, -- Would reference a users table in a full system
    rating INTEGER CHECK(rating BETWEEN 1 AND 5),
    review_text TEXT,
    review_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_games_title ON games(title);
CREATE INDEX IF NOT EXISTS idx_games_developer ON games(developer_id);
CREATE INDEX IF NOT EXISTS idx_updates_game ON updates(game_id);
CREATE INDEX IF NOT EXISTS idx_updates_date ON updates(release_date);
CREATE INDEX IF NOT EXISTS idx_reviews_game ON reviews(game_id);
```
