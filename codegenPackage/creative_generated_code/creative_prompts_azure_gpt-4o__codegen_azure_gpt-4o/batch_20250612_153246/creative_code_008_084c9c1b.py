"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirrorsshadows.com
Prompt: Develop a database schema for managing artist profiles and their work categories, such as sculptures and paintings, as outlined in "The Perfect Studio."
Generated: DETERMINISTIC_084c9c1b5ff2ba28
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the production-ready SQL code for the requested database schema.

```sql
-- Create a database schema for managing artist profiles and their work categories

-- Create the 'artists' table to store artist profiles
CREATE TABLE artists (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each artist
    name VARCHAR(255) NOT NULL,                -- Name of the artist
    biography TEXT,                            -- Short biography of the artist
    birth_date DATE,                           -- Birth date of the artist
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Create the 'categories' table to store work categories such as sculptures, paintings, etc.
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    name VARCHAR(100) NOT NULL UNIQUE,           -- Name of the category (e.g., Sculpture, Painting)
    description TEXT,                            -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Create the 'artist_categories' table to map artists to their categories
CREATE TABLE artist_categories (
    artist_category_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for the relationship
    artist_id INT NOT NULL,                             -- ID of the artist (foreign key)
    category_id INT NOT NULL,                           -- ID of the category (foreign key)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp when the record was created
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Optional: Insert some sample data into the categories table for testing
INSERT INTO categories (name, description)
VALUES 
    ('Sculpture', 'Three-dimensional artwork created by shaping or combining materials.'),
    ('Painting', 'Visual art created using pigments on a surface such as canvas or paper.');

-- Ensure proper indexing for faster lookups
CREATE INDEX idx_artist_id ON artist_categories(artist_id);
CREATE INDEX idx_category_id ON artist_categories(category_id);
```
