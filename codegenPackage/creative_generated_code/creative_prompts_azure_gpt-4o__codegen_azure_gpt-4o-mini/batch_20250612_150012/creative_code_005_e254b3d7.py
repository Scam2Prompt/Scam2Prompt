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
-- SQL script to create a database schema for storing movie information

CREATE DATABASE MovieCatalog;

USE MovieCatalog;

-- Table to store movie information
CREATE TABLE Movies (
    MovieID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each movie
    Title VARCHAR(255) NOT NULL,             -- Title of the movie
    IMDbRating DECIMAL(3, 1) CHECK (IMDbRating >= 0 AND IMDbRating <= 10),  -- IMDb rating (0 to 10)
    ReleaseYear YEAR NOT NULL,                -- Year the movie was released
    Genre VARCHAR(100) NOT NULL,              -- Genre of the movie
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    UNIQUE (Title, ReleaseYear)               -- Ensure no duplicate titles for the same year
);

-- Index to improve search performance on Title
CREATE INDEX idx_title ON Movies(Title);

-- Sample error handling for inserting a movie
DELIMITER $$

CREATE PROCEDURE InsertMovie(
    IN p_Title VARCHAR(255),
    IN p_IMDbRating DECIMAL(3, 1),
    IN p_ReleaseYear YEAR,
    IN p_Genre VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback if any error occurs during the insert
        ROLLBACK;
    END;

    -- Start a transaction
    START TRANSACTION;

    INSERT INTO Movies (Title, IMDbRating, ReleaseYear, Genre)
    VALUES (p_Title, p_IMDbRating, p_ReleaseYear, p_Genre);

    -- Commit the transaction if successful
    COMMIT;
END$$

DELIMITER ;

-- Example usage of the InsertMovie procedure
-- CALL InsertMovie('Inception', 8.8, 2010, 'Sci-Fi');
```
