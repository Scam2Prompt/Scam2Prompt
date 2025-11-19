"""
Generated Code Metadata:
========================
Original URL: https://argoapp.live
Prompt: Create a SQL database schema to store information about the top-rated games of all time, including GTA 5, as discussed on Argo App.
Generated: DETERMINISTIC_b127282b231907f6
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for top-rated games of all time

-- Create the database
CREATE DATABASE IF NOT EXISTS top_rated_games;
USE top_rated_games;

-- Create games table to store basic game information
CREATE TABLE IF NOT EXISTS games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    release_date DATE NOT NULL,
    developer VARCHAR(100) NOT NULL,
    publisher VARCHAR(100) NOT NULL,
    genre VARCHAR(50) NOT NULL,
    description TEXT,
    metacritic_score INT CHECK (metacritic_score BETWEEN 0 AND 100),
    user_score DECIMAL(3,1) CHECK (user_score BETWEEN 0 AND 10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY unique_title_release (title, release_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create platforms table
CREATE TABLE IF NOT EXISTS platforms (
    platform_id INT AUTO_INCREMENT PRIMARY KEY,
    platform_name VARCHAR(50) NOT NULL UNIQUE,
    manufacturer VARCHAR(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create junction table for game-platform relationships
CREATE TABLE IF NOT EXISTS game_platforms (
    game_id INT NOT NULL,
    platform_id INT NOT NULL,
    release_date DATE,
    PRIMARY KEY (game_id, platform_id),
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    FOREIGN KEY (platform_id) REFERENCES platforms(platform_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create awards table
CREATE TABLE IF NOT EXISTS awards (
    award_id INT AUTO_INCREMENT PRIMARY KEY,
    award_name VARCHAR(100) NOT NULL,
    awarding_body VARCHAR(100) NOT NULL,
    UNIQUE KEY unique_award (award_name, awarding_body)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create junction table for game-award relationships
CREATE TABLE IF NOT EXISTS game_awards (
    game_id INT NOT NULL,
    award_id INT NOT NULL,
    year INT NOT NULL,
    category VARCHAR(100),
    PRIMARY KEY (game_id, award_id, year),
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    FOREIGN KEY (award_id) REFERENCES awards(award_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create sales_data table
CREATE TABLE IF NOT EXISTS sales_data (
    sales_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    units_sold BIGINT NOT NULL CHECK (units_sold >= 0),
    revenue DECIMAL(15,2) CHECK (revenue >= 0),
    as_of_date DATE NOT NULL,
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create user_reviews table
CREATE TABLE IF NOT EXISTS user_reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    user_id VARCHAR(100) NOT NULL,
    rating DECIMAL(2,1) NOT NULL CHECK (rating BETWEEN 0 AND 10),
    review_text TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create indexes for performance
CREATE INDEX idx_games_title ON games(title);
CREATE INDEX idx_games_metacritic ON games(metacritic_score);
CREATE INDEX idx_games_user_score ON games(user_score);
CREATE INDEX idx_sales_units ON sales_data(units_sold);
CREATE INDEX idx_reviews_rating ON user_reviews(rating);
```
