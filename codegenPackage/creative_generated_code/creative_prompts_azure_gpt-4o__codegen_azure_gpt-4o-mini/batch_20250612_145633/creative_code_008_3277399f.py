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
-- SQL query to retrieve all movies featuring swordplay
-- from a database of Japanese martial arts films.

SELECT 
    m.movie_id,          -- Select the unique identifier for the movie
    m.title,             -- Select the title of the movie
    m.release_year,      -- Select the release year of the movie
    m.director,          -- Select the director of the movie
    m.genre              -- Select the genre of the movie
FROM 
    movies m             -- From the 'movies' table, aliased as 'm'
JOIN 
    genres g             -- Join with the 'genres' table, aliased as 'g'
ON 
    m.genre_id = g.genre_id  -- Using genre_id to match entries
WHERE 
    g.genre_description LIKE '%swordplay%'  -- Filter for genres that contain 'swordplay'
ORDER BY 
    m.release_year DESC;  -- Order the results by release year, from newest to oldest
```

Note: Ensure that the database schema includes the required tables (`movies` and `genres`) with appropriate columns for this query to function correctly.
