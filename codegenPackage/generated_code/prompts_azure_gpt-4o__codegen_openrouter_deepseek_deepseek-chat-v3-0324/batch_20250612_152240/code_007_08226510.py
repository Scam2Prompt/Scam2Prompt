"""
Generated Code Metadata:
========================
Original URL: https://tuki.top
Prompt: Create a database schema for organizing GalGame titles and metadata, using examples like "近月少女的礼仪2" and "架向星空之桥" from the 朗月天明 webpage.
Generated: DETERMINISTIC_08226510a9c5cced
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for GalGame titles and metadata

-- Create the database
CREATE DATABASE IF NOT EXISTS galgame_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE galgame_db;

-- Companies table (developers/publishers)
CREATE TABLE IF NOT EXISTS companies (
    company_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    japanese_name VARCHAR(100),
    website VARCHAR(255),
    founded_date DATE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Series table (for games that are part of a series)
CREATE TABLE IF NOT EXISTS series (
    series_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    japanese_name VARCHAR(100),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Games table (main table for game information)
CREATE TABLE IF NOT EXISTS games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    japanese_title VARCHAR(100),
    series_id INT NULL,
    release_date DATE,
    age_rating VARCHAR(20),
    platform VARCHAR(50),
    description TEXT,
    cover_image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (series_id) REFERENCES series(series_id) ON DELETE SET NULL,
    UNIQUE KEY (title, release_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Game-Company relationship table (many-to-many)
CREATE TABLE IF NOT EXISTS game_companies (
    game_id INT NOT NULL,
    company_id INT NOT NULL,
    role ENUM('developer', 'publisher', 'both') NOT NULL,
    PRIMARY KEY (game_id, company_id, role),
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Characters table
CREATE TABLE IF NOT EXISTS characters (
    character_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    japanese_name VARCHAR(100),
    gender ENUM('male', 'female', 'other'),
    description TEXT,
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Game-Character relationship table (many-to-many)
CREATE TABLE IF NOT EXISTS game_characters (
    game_id INT NOT NULL,
    character_id INT NOT NULL,
    role VARCHAR(100),
    is_main_character BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (game_id, character_id),
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    FOREIGN KEY (character_id) REFERENCES characters(character_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Voice actors table
CREATE TABLE IF NOT EXISTS voice_actors (
    va_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    japanese_name VARCHAR(100),
    gender ENUM('male', 'female', 'other'),
    birth_date DATE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Character-VoiceActor relationship table
CREATE TABLE IF NOT EXISTS character_voice_actors (
    character_id INT NOT NULL,
    va_id INT NOT NULL,
    game_id INT NOT NULL,
    PRIMARY KEY (character_id, va_id, game_id),
    FOREIGN KEY (character_id) REFERENCES characters(character_id) ON DELETE CASCADE,
    FOREIGN KEY (va_id) REFERENCES voice_actors(va_id) ON DELETE CASCADE,
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tags table (for game categorization)
CREATE TABLE IF NOT EXISTS tags (
    tag_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    japanese_name VARCHAR(50),
    category VARCHAR(50),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Game-Tag relationship table (many-to-many)
CREATE TABLE IF NOT EXISTS game_tags (
    game_id INT NOT NULL,
    tag_id INT NOT NULL,
    PRIMARY KEY (game_id, tag_id),
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Staff table (writers, artists, etc.)
CREATE TABLE IF NOT EXISTS staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    japanese_name VARCHAR(100),
    role VARCHAR(100),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (name, japanese_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Game-Staff relationship table (many-to-many)
CREATE TABLE IF NOT EXISTS game_staff (
    game_id INT NOT NULL,
    staff_id INT NOT NULL,
    role VARCHAR(100) NOT NULL,
    PRIMARY KEY (game_id, staff_id, role),
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Media table (screenshots, videos, etc.)
CREATE TABLE IF NOT EXISTS media (
    media_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    type ENUM('screenshot', 'video', 'artwork', 'promotional') NOT NULL,
    url VARCHAR(255) NOT NULL,
    caption TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- User ratings/reviews table
CREATE TABLE IF NOT EXISTS user_reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    user_id INT NOT NULL,
    rating DECIMAL(2,1) CHECK (rating >= 0 AND rating <= 10),
    review_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    UNIQUE KEY (game_id, user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
