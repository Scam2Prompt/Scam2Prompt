"""
Generated Code Metadata:
========================
Original URL: https://moinulalam.com
Prompt: Design a database schema for storing information about artworks, exhibitions, and artists, using Moinul Alam's portfolio as a reference.
Generated: DETERMINISTIC_f6905e416918d1d3
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about artworks, exhibitions, and artists

-- Create a table for Artists
CREATE TABLE Artists (
    artist_id SERIAL PRIMARY KEY,          -- Unique identifier for each artist
    name VARCHAR(100) NOT NULL,            -- Name of the artist
    biography TEXT,                         -- Biography of the artist
    birth_date DATE,                       -- Birth date of the artist
    nationality VARCHAR(50),               -- Nationality of the artist
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for Artworks
CREATE TABLE Artworks (
    artwork_id SERIAL PRIMARY KEY,          -- Unique identifier for each artwork
    title VARCHAR(200) NOT NULL,            -- Title of the artwork
    artist_id INT NOT NULL,                 -- Foreign key referencing the artist
    medium VARCHAR(100),                     -- Medium used for the artwork (e.g., oil, acrylic)
    year_created INT,                       -- Year the artwork was created
    dimensions VARCHAR(50),                 -- Dimensions of the artwork
    description TEXT,                       -- Description of the artwork
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (artist_id) REFERENCES Artists(artist_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for Exhibitions
CREATE TABLE Exhibitions (
    exhibition_id SERIAL PRIMARY KEY,       -- Unique identifier for each exhibition
    title VARCHAR(200) NOT NULL,            -- Title of the exhibition
    location VARCHAR(100) NOT NULL,         -- Location of the exhibition
    start_date DATE NOT NULL,               -- Start date of the exhibition
    end_date DATE NOT NULL,                 -- End date of the exhibition
    description TEXT,                       -- Description of the exhibition
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a junction table for Artworks in Exhibitions
CREATE TABLE Exhibition_Artworks (
    exhibition_id INT NOT NULL,             -- Foreign key referencing the exhibition
    artwork_id INT NOT NULL,                -- Foreign key referencing the artwork
    PRIMARY KEY (exhibition_id, artwork_id), -- Composite primary key
    FOREIGN KEY (exhibition_id) REFERENCES Exhibitions(exhibition_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (artwork_id) REFERENCES Artworks(artwork_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for Artwork Images
CREATE TABLE Artwork_Images (
    image_id SERIAL PRIMARY KEY,            -- Unique identifier for each image
    artwork_id INT NOT NULL,                -- Foreign key referencing the artwork
    image_url VARCHAR(255) NOT NULL,        -- URL of the artwork image
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (artwork_id) REFERENCES Artworks(artwork_id) ON DELETE CASCADE -- Ensures referential integrity
);
```
