"""
Generated Code Metadata:
========================
Original URL: https://cometrecords.co.uk
Prompt: Generate a SQL database schema for a music label management system inspired by Comet Records, including tables for artists, albums, and music genres like progressive house.
Generated: DETERMINISTIC_06a0ace48ddf7ae3
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- music_label_schema.sql

-- Create a database for the music label management system
CREATE DATABASE music_label;

-- Use the music_label database
USE music_label;

-- Create a table for music genres
CREATE TABLE genres (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create a table for artists
CREATE TABLE artists (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  stage_name VARCHAR(255),
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for albums
CREATE TABLE albums (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  release_date DATE NOT NULL,
  artist_id INT NOT NULL,
  genre_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (artist_id) REFERENCES artists(id) ON DELETE CASCADE,
  FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE RESTRICT
);

-- Create a table for album tracks
CREATE TABLE tracks (
  id INT AUTO_INCREMENT,
  album_id INT NOT NULL,
  title VARCHAR(255) NOT NULL,
  duration DECIMAL(5, 2) NOT NULL,
  track_number INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (album_id) REFERENCES albums(id) ON DELETE CASCADE
);

-- Create a table for artist genres (many-to-many relationship)
CREATE TABLE artist_genres (
  artist_id INT NOT NULL,
  genre_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (artist_id, genre_id),
  FOREIGN KEY (artist_id) REFERENCES artists(id) ON DELETE CASCADE,
  FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_albums_artist_id ON albums (artist_id);
CREATE INDEX idx_albums_genre_id ON albums (genre_id);
CREATE INDEX idx_tracks_album_id ON tracks (album_id);
CREATE INDEX idx_artist_genres_artist_id ON artist_genres (artist_id);
CREATE INDEX idx_artist_genres_genre_id ON artist_genres (genre_id);
```
