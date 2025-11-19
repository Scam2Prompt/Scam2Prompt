"""
Generated Code Metadata:
========================
Original URL: https://hianime.baby
Prompt: Create a database schema for storing anime metadata, including trending titles like "Naruto: Shippuden" and "Attack on Titan," inspired by HiAnime's library structure.
Generated: DETERMINISTIC_f511052921e43e56
Batch ID: 20250612_153256
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for anime metadata storage
CREATE DATABASE IF NOT EXISTS anime_metadata;
USE anime_metadata;

-- Table for storing anime series information
CREATE TABLE IF NOT EXISTS anime_series (
    anime_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    english_title VARCHAR(255),
    japanese_title VARCHAR(255),
    synopsis TEXT,
    start_date DATE,
    end_date DATE,
    episodes INT,
    episode_duration INT COMMENT 'Duration in minutes',
    status ENUM('airing', 'finished', 'upcoming', 'unknown') NOT NULL DEFAULT 'unknown',
    source_material ENUM('manga', 'original', 'light_novel', 'visual_novel', 'game', 'other'),
    mal_id INT COMMENT 'MyAnimeList ID for reference',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_title (title),
    INDEX idx_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for genres
CREATE TABLE IF NOT EXISTS genres (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Junction table for anime-genre relationships
CREATE TABLE IF NOT EXISTS anime_genres (
    anime_id INT NOT NULL,
    genre_id INT NOT NULL,
    PRIMARY KEY (anime_id, genre_id),
    FOREIGN KEY (anime_id) REFERENCES anime_series(anime_id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for studios
CREATE TABLE IF NOT EXISTS studios (
    studio_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    founded_date DATE,
    website VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Junction table for anime-studio relationships
CREATE TABLE IF NOT EXISTS anime_studios (
    anime_id INT NOT NULL,
    studio_id INT NOT NULL,
    role ENUM('primary', 'secondary', 'co-production', 'other') DEFAULT 'primary',
    PRIMARY KEY (anime_id, studio_id),
    FOREIGN KEY (anime_id) REFERENCES anime_series(anime_id) ON DELETE CASCADE,
    FOREIGN KEY (studio_id) REFERENCES studios(studio_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for tracking trending anime
CREATE TABLE IF NOT EXISTS trending_anime (
    trend_id INT AUTO_INCREMENT PRIMARY KEY,
    anime_id INT NOT NULL,
    rank_position INT NOT NULL,
    trend_date DATE NOT NULL,
    score DECIMAL(5,2) COMMENT 'Popularity score',
    FOREIGN KEY (anime_id) REFERENCES anime_series(anime_id) ON DELETE CASCADE,
    INDEX idx_trend_date (trend_date),
    INDEX idx_rank_position (rank_position),
    UNIQUE KEY uniq_anime_date (anime_id, trend_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for user ratings
CREATE TABLE IF NOT EXISTS user_ratings (
    rating_id INT AUTO_INCREMENT PRIMARY KEY,
    anime_id INT NOT NULL,
    user_id INT NOT NULL COMMENT 'Reference to users table in authentication system',
    score DECIMAL(3,1) NOT NULL CHECK (score BETWEEN 1 AND 10),
    review TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (anime_id) REFERENCES anime_series(anime_id) ON DELETE CASCADE,
    INDEX idx_anime_id (anime_id),
    INDEX idx_user_id (user_id),
    UNIQUE KEY uniq_user_anime (user_id, anime_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for anime seasons
CREATE TABLE IF NOT EXISTS seasons (
    season_id INT AUTO_INCREMENT PRIMARY KEY,
    anime_id INT NOT NULL,
    season_number INT NOT NULL,
    title VARCHAR(255),
    episodes INT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (anime_id) REFERENCES anime_series(anime_id) ON DELETE CASCADE,
    INDEX idx_anime_season (anime_id, season_number)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for anime characters
CREATE TABLE IF NOT EXISTS characters (
    character_id INT AUTO_INCREMENT PRIMARY KEY,
    anime_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    japanese_name VARCHAR(255),
    role ENUM('main', 'supporting', 'cameo') DEFAULT 'supporting',
    description TEXT,
    FOREIGN KEY (anime_id) REFERENCES anime_series(anime_id) ON DELETE CASCADE,
    INDEX idx_anime_id (anime_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for voice actors
CREATE TABLE IF NOT EXISTS voice_actors (
    actor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    japanese_name VARCHAR(255),
    gender ENUM('male', 'female', 'non-binary', 'unknown'),
    birth_date DATE,
    website VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Junction table for character-voice actor relationships
CREATE TABLE IF NOT EXISTS character_actors (
    character_id INT NOT NULL,
    actor_id INT NOT NULL,
    language ENUM('japanese', 'english', 'other') DEFAULT 'japanese',
    PRIMARY KEY (character_id, actor_id, language),
    FOREIGN KEY (character_id) REFERENCES characters(character_id) ON DELETE CASCADE,
    FOREIGN KEY (actor_id) REFERENCES voice_actors(actor_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for related anime (sequels, prequels, spin-offs, etc.)
CREATE TABLE IF NOT EXISTS related_anime (
    relation_id INT AUTO_INCREMENT PRIMARY KEY,
    source_anime_id INT NOT NULL,
    related_anime_id INT NOT NULL,
    relation_type ENUM('sequel', 'prequel', 'alternative_setting', 'alternative_version', 'side_story', 'parent_story', 'summary', 'full_story', 'spin_off', 'other'),
    FOREIGN KEY (source_anime_id) REFERENCES anime_series(anime_id) ON DELETE CASCADE,
    FOREIGN KEY (related_anime_id) REFERENCES anime_series(anime_id) ON DELETE CASCADE,
    INDEX idx_source_anime (source_anime_id),
    INDEX idx_related_anime (related_anime_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```
