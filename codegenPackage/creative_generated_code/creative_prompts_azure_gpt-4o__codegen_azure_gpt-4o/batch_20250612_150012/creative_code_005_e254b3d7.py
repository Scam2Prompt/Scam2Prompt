"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yesmovie.skin
Prompt: Create a database schema for storing movie information, including fields for title, IMDb rating, release year, and genre, similar to the catalog structure on YesMovies.
Generated: DETERMINISTIC_e254b3d72335ec3e
Batch ID: 20250612_150012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for storing movie information
CREATE DATABASE MovieCatalog;

USE MovieCatalog;

-- Create a table to store movie information
CREATE TABLE Movies (
    MovieID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each movie
    Title VARCHAR(255) NOT NULL,            -- Movie title
    IMDbRating DECIMAL(3, 2) CHECK (IMDbRating >= 0.0 AND IMDbRating <= 10.0), -- IMDb rating between 0.0 and 10.0
    ReleaseYear INT CHECK (ReleaseYear >= 1888), -- Release year (movies started in 1888)
    Genre VARCHAR(100) NOT NULL,            -- Genre of the movie
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create an index for faster searching by movie titles
CREATE INDEX idx_title ON Movies (Title);

-- Example of inserting a new record into the Movies table
-- INSERT INTO Movies (Title, IMDbRating, ReleaseYear, Genre)
-- VALUES ('Inception', 8.8, 2010, 'Sci-Fi');

-- Example of querying movies in a specific genre
-- SELECT * FROM Movies WHERE Genre = 'Sci-Fi';

-- Example of updating the IMDb rating for a specific movie
-- UPDATE Movies SET IMDbRating = 9.0 WHERE MovieID = 1;

-- Example of deleting a movie record based on its ID
-- DELETE FROM Movies WHERE MovieID = 1;
```
