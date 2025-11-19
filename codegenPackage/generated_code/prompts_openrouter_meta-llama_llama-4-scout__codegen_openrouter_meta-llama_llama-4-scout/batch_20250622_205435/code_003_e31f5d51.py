"""
Generated Code Metadata:
========================
Original URL: https://sonic-lab.net
Prompt: Design a database schema to manage music metadata for an electronic music label like Soniculture, including artist information, music genres, and album tracks.
Generated: DETERMINISTIC_e31f5d51cfc4ce03
Batch ID: 20250622_205435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for music metadata
CREATE DATABASE soniculture;

-- Use the database
USE soniculture;

-- Create table for music genres
CREATE TABLE genres (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create table for artists
CREATE TABLE artists (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  bio TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create table for albums
CREATE TABLE albums (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  artist_id INT NOT NULL,
  release_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (artist_id) REFERENCES artists(id) ON DELETE CASCADE
);

-- Create table for tracks
CREATE TABLE tracks (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  album_id INT NOT NULL,
  genre_id INT,
  duration DECIMAL(5, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (album_id) REFERENCES albums(id) ON DELETE CASCADE,
  FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE SET NULL
);

-- Create table for artist_genres (many-to-many relationship)
CREATE TABLE artist_genres (
  artist_id INT NOT NULL,
  genre_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (artist_id, genre_id),
  FOREIGN KEY (artist_id) REFERENCES artists(id) ON DELETE CASCADE,
  FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE CASCADE
);

-- Example data
INSERT INTO genres (name, description) 
VALUES 
('Techno', 'A genre of electronic dance music'),
('Trance', 'A genre of electronic dance music'),
('House', 'A genre of electronic dance music');

INSERT INTO artists (name, bio) 
VALUES 
('John Doe', 'Electronic music producer'),
('Jane Doe', 'Electronic music DJ');

INSERT INTO albums (title, artist_id, release_date) 
VALUES 
('Album 1', 1, '2020-01-01'),
('Album 2', 2, '2020-06-01');

INSERT INTO tracks (title, album_id, genre_id, duration) 
VALUES 
('Track 1', 1, 1, 3.45),
('Track 2', 1, 2, 4.10),
('Track 3', 2, 3, 3.20);

INSERT INTO artist_genres (artist_id, genre_id) 
VALUES 
(1, 1),
(1, 2),
(2, 3);
```
