"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://megami.live
Prompt: Write a SQL query to retrieve all movies featuring swordplay from a database of Japanese martial arts films.
Generated: DETERMINISTIC_3277399f25afe7e6
Batch ID: 20250612_145633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Query to retrieve all movies featuring swordplay from a database of Japanese martial arts films.

-- Assuming the database has a table named 'movies' with relevant columns:
-- 'id' (unique identifier for the movie),
-- 'title' (name of the movie),
-- 'genre' (movie genre),
-- and 'description' (text providing details about the movie).

SELECT 
    id,
    title,
    genre,
    description
FROM 
    movies
WHERE 
    -- Filtering movies where the description explicitly mentions 'swordplay'.
    -- Using case-insensitive matching for broader compatibility.
    LOWER(description) LIKE '%swordplay%'
    AND LOWER(genre) LIKE '%martial arts%' -- Ensuring the movie is part of the martial arts genre.
ORDER BY 
    title ASC; -- Sorting by title for better readability of the result set.
```
