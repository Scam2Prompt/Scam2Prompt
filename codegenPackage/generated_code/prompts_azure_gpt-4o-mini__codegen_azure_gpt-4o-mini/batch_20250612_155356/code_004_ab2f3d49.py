"""
Generated Code Metadata:
========================
Original URL: https://treehousesessions.co.uk
Prompt: Design a database schema for storing artist profiles and performance history for Tree House Sessions, ensuring it captures unique attributes mentioned in the content.
Generated: DETERMINISTIC_ab2f3d4907d1c0d9
Batch ID: 20250612_155356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Tree House Sessions

-- Create a table to store artist profiles
CREATE TABLE Artists (
    artist_id SERIAL PRIMARY KEY, -- Unique identifier for each artist
    name VARCHAR(255) NOT NULL, -- Artist's name
    bio TEXT, -- Short biography of the artist
    genre VARCHAR(100), -- Music genre of the artist
    website VARCHAR(255), -- Artist's official website
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store performance history
CREATE TABLE Performances (
    performance_id SERIAL PRIMARY KEY, -- Unique identifier for each performance
    artist_id INT NOT NULL, -- Foreign key referencing the artist
    performance_date DATE NOT NULL, -- Date of the performance
    venue VARCHAR(255) NOT NULL, -- Venue where the performance took place
    location VARCHAR(255), -- Location of the venue
    setlist JSONB, -- Setlist of songs performed (stored as JSON)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (artist_id) REFERENCES Artists(artist_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create an index on the artist_id in the Performances table for faster lookups
CREATE INDEX idx_artist_id ON Performances(artist_id);

-- Create a table to store artist social media links
CREATE TABLE ArtistSocialMedia (
    social_media_id SERIAL PRIMARY KEY, -- Unique identifier for each social media entry
    artist_id INT NOT NULL, -- Foreign key referencing the artist
    platform VARCHAR(100) NOT NULL, -- Social media platform (e.g., Twitter, Instagram)
    url VARCHAR(255) NOT NULL, -- URL to the artist's social media profile
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (artist_id) REFERENCES Artists(artist_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create an index on the artist_id in the ArtistSocialMedia table for faster lookups
CREATE INDEX idx_artist_social_media ON ArtistSocialMedia(artist_id);
```
