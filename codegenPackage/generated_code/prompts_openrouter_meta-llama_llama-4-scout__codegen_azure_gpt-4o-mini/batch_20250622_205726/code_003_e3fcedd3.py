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
-- Database schema for storing information about artists, artworks, and categories

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Artwork;
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Category;

-- Table to store artist information
CREATE TABLE Artist (
    artist_id SERIAL PRIMARY KEY, -- Unique identifier for each artist
    name VARCHAR(100) NOT NULL, -- Name of the artist
    bio TEXT, -- Biography of the artist
    birth_date DATE, -- Birth date of the artist
    death_date DATE, -- Death date of the artist (if applicable)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store category information
CREATE TABLE Category (
    category_id SERIAL PRIMARY KEY, -- Unique identifier for each category
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the category
    description TEXT, -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store artwork information
CREATE TABLE Artwork (
    artwork_id SERIAL PRIMARY KEY, -- Unique identifier for each artwork
    title VARCHAR(200) NOT NULL, -- Title of the artwork
    artist_id INT NOT NULL, -- Foreign key referencing the artist
    category_id INT NOT NULL, -- Foreign key referencing the category
    year_created INT, -- Year the artwork was created
    medium VARCHAR(100), -- Medium used for the artwork
    dimensions VARCHAR(100), -- Dimensions of the artwork
    price DECIMAL(10, 2), -- Price of the artwork
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (category_id) REFERENCES Category(category_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_artist_name ON Artist(name);
CREATE INDEX idx_category_name ON Category(name);
CREATE INDEX idx_artwork_title ON Artwork(title);
CREATE INDEX idx_artwork_artist ON Artwork(artist_id);
CREATE INDEX idx_artwork_category ON Artwork(category_id);
```
