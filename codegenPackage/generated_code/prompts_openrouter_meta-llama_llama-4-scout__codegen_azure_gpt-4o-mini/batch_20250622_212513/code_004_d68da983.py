"""
Generated Code Metadata:
========================
Original URL: https://swapepoocoine.blogspot.com
Prompt: Write a SQL query to retrieve shoe information from a database, filtering by type (e.g., chuteira, tenis de esporte).
Generated: DETERMINISTIC_d68da98364afc82f
Batch ID: 20250622_212513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve shoe information filtered by type
-- This query selects relevant columns from the 'shoes' table
-- and filters the results based on the specified shoe type.

SELECT 
    id,                -- Unique identifier for the shoe
    name,              -- Name of the shoe
    type,              -- Type of the shoe (e.g., chuteira, tenis de esporte)
    brand,             -- Brand of the shoe
    size,              -- Size of the shoe
    price              -- Price of the shoe
FROM 
    shoes              -- The table containing shoe information
WHERE 
    type IN ('chuteira', 'tenis de esporte')  -- Filter for specific shoe types
ORDER BY 
    name ASC;         -- Order the results by shoe name in ascending order
```
