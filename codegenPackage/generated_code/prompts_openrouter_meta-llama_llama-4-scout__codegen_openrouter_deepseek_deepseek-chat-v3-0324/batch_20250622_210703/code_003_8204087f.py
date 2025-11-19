"""
Generated Code Metadata:
========================
Original URL: https://stardomrecordz.com
Prompt: Develop a simple database schema for a music record label like Stardom Recordz, including tables for artists, albums, and songs.
Generated: DETERMINISTIC_8204087f02ed1331
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a music record label

-- Create database
CREATE DATABASE IF NOT EXISTS stardom_recordz;
USE stardom_recordz;

-- Artists table
CREATE TABLE IF NOT EXISTS artists (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    bio TEXT,
    date_of_birth DATE,
    country_of_origin VARCHAR(100),
    date_signed DATE,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT unique_artist_name UNIQUE (name)
) ENGINE=InnoDB;

-- Albums table
CREATE TABLE IF NOT EXISTS albums (
    album_id INT AUTO_INCREMENT PRIMARY KEY,
    artist_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    release_date DATE,
    genre VARCHAR(50),
    record_label VARCHAR(100),
    total_tracks INT,
    duration_minutes INT,
    cover_art_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE,
    CONSTRAINT unique_album_per_artist UNIQUE (artist_id, title)
) ENGINE=InnoDB;

-- Songs table
CREATE TABLE IF NOT EXISTS songs (
    song_id INT AUTO_INCREMENT PRIMARY KEY,
    album_id INT,
    artist_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    duration_seconds INT NOT NULL,
    track_number INT,
    lyrics TEXT,
    release_date DATE,
    genre VARCHAR(50),
    is_single BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (album_id) REFERENCES albums(album_id) ON DELETE SET NULL,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE,
    CONSTRAINT unique_song_per_album UNIQUE (album_id, track_number)
) ENGINE=InnoDB;

-- Create indexes for performance
CREATE INDEX idx_artist_name ON artists(name);
CREATE INDEX idx_album_title ON albums(title);
CREATE INDEX idx_song_title ON songs(title);
CREATE INDEX idx_song_artist ON songs(artist_id);
CREATE INDEX idx_album_artist ON albums(artist_id);
```
