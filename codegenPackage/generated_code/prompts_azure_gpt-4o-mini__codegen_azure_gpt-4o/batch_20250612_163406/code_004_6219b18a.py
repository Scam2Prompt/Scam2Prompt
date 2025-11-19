"""
Generated Code Metadata:
========================
Original URL: https://cuadrosblangar.es
Prompt: Construct a SQL query to fetch all available wall decorations categorized by room type from the Cuadros Blangar database.
Generated: DETERMINISTIC_6219b18a96c0111b
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to fetch all available wall decorations categorized by room type
-- from the Cuadros Blangar database.

-- Ensure the database connection is established before running this query.

SELECT 
    wd.id AS decoration_id,          -- Unique identifier for the wall decoration
    wd.name AS decoration_name,      -- Name of the wall decoration
    wd.description AS decoration_description, -- Description of the wall decoration
    wd.price AS decoration_price,    -- Price of the wall decoration
    rt.id AS room_type_id,           -- Unique identifier for the room type
    rt.name AS room_type_name        -- Name of the room type
FROM 
    wall_decorations AS wd           -- Table containing wall decoration details
JOIN 
    room_types AS rt                 -- Table containing room type details
ON 
    wd.room_type_id = rt.id          -- Foreign key relationship between wall decorations and room types
WHERE 
    wd.is_available = TRUE           -- Fetch only available wall decorations
ORDER BY 
    rt.name ASC,                     -- Sort by room type name alphabetically
    wd.name ASC;                     -- Sort by wall decoration name alphabetically within each room type

-- Notes:
-- 1. Ensure the `is_available` column exists in the `wall_decorations` table and is a boolean.
-- 2. Replace table and column names if they differ in your database schema.
-- 3. Add additional filters or pagination if required for production use.
```
