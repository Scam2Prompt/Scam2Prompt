"""
Generated Code Metadata:
========================
Original URL: https://mirrorsshadows.com
Prompt: Develop a database schema for managing artist profiles and their work categories, such as sculptures and paintings, as outlined in "The Perfect Studio."
Generated: DETERMINISTIC_084c9c1b5ff2ba28
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing artist profiles and their work categories

-- Create a table to store artist profiles
CREATE TABLE Artists (
    artist_id SERIAL PRIMARY KEY,          -- Unique identifier for each artist
    name VARCHAR(100) NOT NULL,            -- Name of the artist
    bio TEXT,                               -- Biography of the artist
    email VARCHAR(100) UNIQUE NOT NULL,    -- Email address of the artist
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the profile was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store work categories
CREATE TABLE WorkCategories (
    category_id SERIAL PRIMARY KEY,        -- Unique identifier for each work category
    category_name VARCHAR(50) NOT NULL UNIQUE, -- Name of the work category (e.g., Sculpture, Painting)
    description TEXT                        -- Description of the work category
);

-- Create a table to link artists to their works
CREATE TABLE ArtistWorks (
    work_id SERIAL PRIMARY KEY,             -- Unique identifier for each work
    artist_id INT NOT NULL,                 -- Foreign key referencing the artist
    category_id INT NOT NULL,               -- Foreign key referencing the work category
    title VARCHAR(100) NOT NULL,            -- Title of the work
    year_created INT,                       -- Year the work was created
    medium VARCHAR(50),                     -- Medium used for the work (e.g., oil, clay)
    dimensions VARCHAR(50),                 -- Dimensions of the work
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the work was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (artist_id) REFERENCES Artists(artist_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (category_id) REFERENCES WorkCategories(category_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on artist_id in ArtistWorks for faster lookups
CREATE INDEX idx_artist_id ON ArtistWorks(artist_id);

-- Create an index on category_id in ArtistWorks for faster lookups
CREATE INDEX idx_category_id ON ArtistWorks(category_id);
```
