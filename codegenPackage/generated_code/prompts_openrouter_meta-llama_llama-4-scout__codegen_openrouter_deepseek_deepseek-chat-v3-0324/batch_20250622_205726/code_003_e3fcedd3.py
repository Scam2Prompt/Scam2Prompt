"""
Generated Code Metadata:
========================
Original URL: https://opensea.b4b.dev
Prompt: Design a database schema for storing information about artists, artworks, and categories, inspired by the structure of the Little Green Field Gallery website.
Generated: DETERMINISTIC_e3fcedd36e6b29b8
Batch ID: 20250622_205726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Little Green Field Gallery

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create artists table
CREATE TABLE artists (
    artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    bio TEXT,
    email TEXT UNIQUE,
    website TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create categories table
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create artworks table
CREATE TABLE artworks (
    artwork_id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    creation_year INTEGER,
    width_cm REAL,
    height_cm REAL,
    depth_cm REAL,
    price REAL,
    is_sold BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE
);

-- Create junction table for artwork categories (many-to-many relationship)
CREATE TABLE artwork_categories (
    artwork_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    PRIMARY KEY (artwork_id, category_id),
    FOREIGN KEY (artwork_id) REFERENCES artworks(artwork_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

-- Create images table for artwork media
CREATE TABLE artwork_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    artwork_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (artwork_id) REFERENCES artworks(artwork_id) ON DELETE CASCADE
);

-- Create exhibitions table
CREATE TABLE exhibitions (
    exhibition_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    location TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create junction table for exhibition artworks
CREATE TABLE exhibition_artworks (
    exhibition_id INTEGER NOT NULL,
    artwork_id INTEGER NOT NULL,
    display_order INTEGER DEFAULT 0,
    PRIMARY KEY (exhibition_id, artwork_id),
    FOREIGN KEY (exhibition_id) REFERENCES exhibitions(exhibition_id) ON DELETE CASCADE,
    FOREIGN KEY (artwork_id) REFERENCES artworks(artwork_id) ON DELETE CASCADE
);

-- Create triggers for updated_at timestamps
CREATE TRIGGER update_artist_timestamp
AFTER UPDATE ON artists
FOR EACH ROW
BEGIN
    UPDATE artists SET updated_at = CURRENT_TIMESTAMP WHERE artist_id = OLD.artist_id;
END;

CREATE TRIGGER update_artwork_timestamp
AFTER UPDATE ON artworks
FOR EACH ROW
BEGIN
    UPDATE artworks SET updated_at = CURRENT_TIMESTAMP WHERE artwork_id = OLD.artwork_id;
END;

CREATE TRIGGER update_exhibition_timestamp
AFTER UPDATE ON exhibitions
FOR EACH ROW
BEGIN
    UPDATE exhibitions SET updated_at = CURRENT_TIMESTAMP WHERE exhibition_id = OLD.exhibition_id;
END;

-- Create indexes for performance optimization
CREATE INDEX idx_artworks_artist ON artworks(artist_id);
CREATE INDEX idx_artwork_categories_artwork ON artwork_categories(artwork_id);
CREATE INDEX idx_artwork_categories_category ON artwork_categories(category_id);
CREATE INDEX idx_artwork_images_artwork ON artwork_images(artwork_id);
CREATE INDEX idx_exhibition_artworks_exhibition ON exhibition_artworks(exhibition_id);
CREATE INDEX idx_exhibition_artworks_artwork ON exhibition_artworks(artwork_id);
```
