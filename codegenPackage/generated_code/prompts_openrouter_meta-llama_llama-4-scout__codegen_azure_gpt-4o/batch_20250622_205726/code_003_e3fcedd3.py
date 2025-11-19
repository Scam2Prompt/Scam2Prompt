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
-- Database Schema for Little Green Field Gallery

-- Table to store information about artists
CREATE TABLE Artists (
    ArtistID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each artist
    Name VARCHAR(255) NOT NULL,              -- Full name of the artist
    Bio TEXT,                                -- Short biography of the artist
    BirthDate DATE,                          -- Date of birth of the artist
    DeathDate DATE,                          -- Date of death of the artist (nullable for living artists)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL UNIQUE,         -- Name of the category (e.g., "Landscape", "Abstract")
    Description TEXT,                          -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about artworks
CREATE TABLE Artworks (
    ArtworkID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each artwork
    Title VARCHAR(255) NOT NULL,              -- Title of the artwork
    Description TEXT,                         -- Description of the artwork
    YearCreated INT,                          -- Year the artwork was created
    ArtistID INT NOT NULL,                    -- Foreign key referencing the artist who created the artwork
    CategoryID INT NOT NULL,                  -- Foreign key referencing the category of the artwork
    ImageURL VARCHAR(2083),                   -- URL to an image of the artwork
    Price DECIMAL(10, 2),                     -- Price of the artwork
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID) ON DELETE CASCADE, -- Cascade delete if artist is removed
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL -- Set category to NULL if deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_artist_name ON Artists(Name);
CREATE INDEX idx_category_name ON Categories(Name);
CREATE INDEX idx_artwork_title ON Artworks(Title);

-- Example error handling: Ensure strict mode is enabled for better data integrity
SET sql_mode = 'STRICT_TRANS_TABLES';
```
