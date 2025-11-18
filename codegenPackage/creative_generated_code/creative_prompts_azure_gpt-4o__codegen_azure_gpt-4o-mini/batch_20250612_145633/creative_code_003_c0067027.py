"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://megami.live
Prompt: Develop a database schema for organizing a VOD platform's catalog of Japanese martial arts movies, including fields for genre, choreography style, and combat techniques.
Generated: DETERMINISTIC_c00670270fb55fa8
Batch ID: 20250612_145633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a Video On Demand (VOD) platform's catalog of Japanese martial arts movies

CREATE TABLE Genres (
    genre_id SERIAL PRIMARY KEY,        -- Unique identifier for each genre
    name VARCHAR(100) NOT NULL UNIQUE   -- Name of the genre (e.g., Action, Drama)
);

CREATE TABLE ChoreographyStyles (
    style_id SERIAL PRIMARY KEY,        -- Unique identifier for each choreography style
    name VARCHAR(100) NOT NULL UNIQUE   -- Name of the choreography style (e.g., Iaido, Judo)
);

CREATE TABLE CombatTechniques (
    technique_id SERIAL PRIMARY KEY,    -- Unique identifier for each combat technique
    name VARCHAR(100) NOT NULL UNIQUE,  -- Name of the combat technique (e.g., Kicking, Grappling)
    description TEXT                    -- Description of the combat technique
);

CREATE TABLE Movies (
    movie_id SERIAL PRIMARY KEY,          -- Unique identifier for each movie
    title VARCHAR(255) NOT NULL,         -- Title of the movie
    release_year INT CHECK (release_year > 1888),  -- Release year of the movie (after the invention of film)
    genre_id INT REFERENCES Genres(genre_id) ON DELETE SET NULL,     -- Foreign key reference to Genres table
    choreography_style_id INT REFERENCES ChoreographyStyles(style_id) ON DELETE SET NULL, -- Foreign key reference to ChoreographyStyles table
    combat_technique_id INT REFERENCES CombatTechniques(technique_id) ON DELETE SET NULL, -- Foreign key reference to CombatTechniques table
    director VARCHAR(255) NOT NULL,      -- Director of the movie
    description TEXT,                    -- Description or synopsis of the movie
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Indexes for optimizing searches
CREATE INDEX idx_movies_title ON Movies(title);
CREATE INDEX idx_movies_release_year ON Movies(release_year);
CREATE INDEX idx_movies_genre ON Movies(genre_id);
CREATE INDEX idx_movies_choreography_style ON Movies(choreography_style_id);
CREATE INDEX idx_movies_combat_technique ON Movies(combat_technique_id);
```
