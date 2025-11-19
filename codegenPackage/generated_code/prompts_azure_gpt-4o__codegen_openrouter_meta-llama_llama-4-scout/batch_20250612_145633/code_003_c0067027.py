"""
Generated Code Metadata:
========================
Original URL: https://megami.live
Prompt: Develop a database schema for organizing a VOD platform's catalog of Japanese martial arts movies, including fields for genre, choreography style, and combat techniques.
Generated: DETERMINISTIC_c00670270fb55fa8
Batch ID: 20250612_145633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the VOD platform's catalog
CREATE DATABASE martial_arts_vod;

-- Use the martial_arts_vod database
USE martial_arts_vod;

-- Create a table for genres
CREATE TABLE genres (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create a table for choreography styles
CREATE TABLE choreography_styles (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create a table for combat techniques
CREATE TABLE combat_techniques (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create a table for movies
CREATE TABLE movies (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  synopsis TEXT,
  release_year INT,
  genre_id INT,
  choreography_style_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE SET NULL,
  FOREIGN KEY (choreography_style_id) REFERENCES choreography_styles(id) ON DELETE SET NULL
);

-- Create a many-to-many relationship table for movies and combat techniques
CREATE TABLE movie_combat_techniques (
  movie_id INT,
  combat_technique_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (movie_id, combat_technique_id),
  FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE,
  FOREIGN KEY (combat_technique_id) REFERENCES combat_techniques(id) ON DELETE CASCADE
);

-- Create an index on the genre_id column in the movies table
CREATE INDEX idx_genre_id ON movies (genre_id);

-- Create an index on the choreography_style_id column in the movies table
CREATE INDEX idx_choreography_style_id ON movies (choreography_style_id);

-- Create an index on the movie_id column in the movie_combat_techniques table
CREATE INDEX idx_movie_id ON movie_combat_techniques (movie_id);

-- Create an index on the combat_technique_id column in the movie_combat_techniques table
CREATE INDEX idx_combat_technique_id ON movie_combat_techniques (combat_technique_id);
```
