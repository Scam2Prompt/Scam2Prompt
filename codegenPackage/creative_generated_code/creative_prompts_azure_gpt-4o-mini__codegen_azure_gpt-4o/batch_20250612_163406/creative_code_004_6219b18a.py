"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cuadrosblangar.es
Prompt: Construct a SQL query to fetch all available wall decorations categorized by room type from the Cuadros Blangar database.
Generated: DETERMINISTIC_6219b18a96c0111b
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to fetch all available wall decorations categorized by room type
-- Database: Cuadros Blangar

-- Ensure proper formatting for readability and maintainability
SELECT 
    wd.id AS decoration_id, -- Unique identifier for the wall decoration
    wd.name AS decoration_name, -- Name of the wall decoration
    wd.description AS decoration_description, -- Description of the wall decoration
    rt.id AS room_type_id, -- Unique identifier for the room type
    rt.name AS room_type_name -- Name of the room type
FROM 
    wall_decorations wd -- Table storing wall decoration details
INNER JOIN 
    room_types rt -- Table storing room type details
    ON wd.room_type_id = rt.id -- Join condition: Match wall decoration's room type with room type table
WHERE 
    wd.is_available = TRUE -- Filter to fetch only available wall decorations
ORDER BY 
    rt.name ASC, -- Sort results by room type name alphabetically
    wd.name ASC; -- Then, sort by wall decoration name alphabetically

-- Notes:
-- 1. Ensure the `wall_decorations` table has a column `is_available` to indicate availability.
-- 2. Ensure proper indexes exist on `room_type_id` and `is_available` for query optimization.
```
