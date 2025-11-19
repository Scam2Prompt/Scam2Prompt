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
-- Database schema for a music label management system

-- Create the database
CREATE DATABASE IF NOT EXISTS comet_records;
USE comet_records;

-- Table for storing music genres
CREATE TABLE IF NOT EXISTS genres (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for storing artists
CREATE TABLE IF NOT EXISTS artists (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    bio TEXT,
    country VARCHAR(50),
    date_formed DATE,
    website VARCHAR(255),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
);

-- Table for artist-genre relationships (many-to-many)
CREATE TABLE IF NOT EXISTS artist_genres (
    artist_id INT NOT NULL,
    genre_id INT NOT NULL,
    PRIMARY KEY (artist_id, genre_id),
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE
);

-- Table for storing albums
CREATE TABLE IF NOT EXISTS albums (
    album_id INT AUTO_INCREMENT PRIMARY KEY,
    artist_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    release_date DATE,
    label VARCHAR(100),
    catalog_number VARCHAR(50),
    format VARCHAR(20) CHECK (format IN ('Digital', 'Vinyl', 'CD', 'Cassette', 'Other')),
    duration INT COMMENT 'Total duration in seconds',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE
);

-- Table for album-genre relationships (many-to-many)
CREATE TABLE IF NOT EXISTS album_genres (
    album_id INT NOT NULL,
    genre_id INT NOT NULL,
    PRIMARY KEY (album_id, genre_id),
    FOREIGN KEY (album_id) REFERENCES albums(album_id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE
);

-- Table for storing tracks
CREATE TABLE IF NOT EXISTS tracks (
    track_id INT AUTO_INCREMENT PRIMARY KEY,
    album_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    track_number INT NOT NULL,
    duration INT NOT NULL COMMENT 'Duration in seconds',
    isrc VARCHAR(12) UNIQUE COMMENT 'International Standard Recording Code',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (album_id) REFERENCES albums(album_id) ON DELETE CASCADE,
    CONSTRAINT chk_isrc CHECK (LENGTH(isrc) = 12 OR isrc IS NULL)
);

-- Table for storing track genres (many-to-many)
CREATE TABLE IF NOT EXISTS track_genres (
    track_id INT NOT NULL,
    genre_id INT NOT NULL,
    PRIMARY KEY (track_id, genre_id),
    FOREIGN KEY (track_id) REFERENCES tracks(track_id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE
);

-- Table for storing releases (different versions of albums)
CREATE TABLE IF NOT EXISTS releases (
    release_id INT AUTO_INCREMENT PRIMARY KEY,
    album_id INT NOT NULL,
    release_type VARCHAR(20) CHECK (release_type IN ('Original', 'Remaster', 'Deluxe', 'Special', 'Limited')),
    release_date DATE,
    format VARCHAR(20) CHECK (format IN ('Digital', 'Vinyl', 'CD', 'Cassette', 'Other')),
    catalog_number VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (album_id) REFERENCES albums(album_id) ON DELETE CASCADE
);

-- Table for storing sales and distribution information
CREATE TABLE IF NOT EXISTS sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    release_id INT NOT NULL,
    sale_date DATE NOT NULL,
    quantity INT NOT NULL,
    revenue DECIMAL(10,2) NOT NULL,
    platform VARCHAR(50) COMMENT 'Sales platform (e.g., Beatport, iTunes, Bandcamp)',
    country VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (release_id) REFERENCES releases(release_id) ON DELETE CASCADE,
    CONSTRAINT chk_quantity CHECK (quantity > 0),
    CONSTRAINT chk_revenue CHECK (revenue >= 0)
);

-- Table for storing label staff
CREATE TABLE IF NOT EXISTS staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    role VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20),
    hire_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_staff_email CHECK (email LIKE '%@%.%')
);

-- Table for artist contracts
CREATE TABLE IF NOT EXISTS contracts (
    contract_id INT AUTO_INCREMENT PRIMARY KEY,
    artist_id INT NOT NULL,
    staff_id INT NOT NULL COMMENT 'Label representative',
    start_date DATE NOT NULL,
    end_date DATE,
    terms TEXT NOT NULL,
    royalty_rate DECIMAL(5,2) COMMENT 'Percentage rate',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE,
    CONSTRAINT chk_dates CHECK (end_date IS NULL OR end_date > start_date),
    CONSTRAINT chk_royalty CHECK (royalty_rate BETWEEN 0 AND 100)
);

-- Indexes for performance optimization
CREATE INDEX idx_artist_name ON artists(name);
CREATE INDEX idx_album_title ON albums(title);
CREATE INDEX idx_track_title ON tracks(title);
CREATE INDEX idx_genre_name ON genres(name);
CREATE INDEX idx_sale_date ON sales(sale_date);
```
