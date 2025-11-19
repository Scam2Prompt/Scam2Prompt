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
-- SQL query to fetch all available wall decorations categorized by room type
SELECT 
    wd.id AS wall_decoration_id,           -- Unique identifier for the wall decoration
    wd.name AS decoration_name,             -- Name of the wall decoration
    wd.type AS decoration_type,             -- Type of the wall decoration (e.g., painting, print)
    rt.name AS room_type_name                -- Name of the room type (e.g., living room, bedroom)
FROM 
    wall_decorations wd                     -- Table containing wall decorations
JOIN 
    room_types rt ON wd.room_type_id = rt.id  -- Joining with room_types to get room type names
WHERE 
    wd.available = TRUE                      -- Filter to fetch only available decorations
ORDER BY 
    rt.name, wd.name;                       -- Ordering results by room type name and decoration name
```
