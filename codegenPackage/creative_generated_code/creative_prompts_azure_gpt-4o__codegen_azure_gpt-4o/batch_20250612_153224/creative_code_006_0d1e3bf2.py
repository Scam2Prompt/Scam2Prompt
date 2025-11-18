"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sunnyhurghada.com
Prompt: Generate a SQL query to filter properties from sunnyhurghada.com’s database by location (e.g., Intercontinental, Sky Villa) and price range.
Generated: DETERMINISTIC_0d1e3bf240ac3ea8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to filter properties by location and price range

-- This query assumes a table named 'properties' with columns 'location', 'price', and other relevant fields.

-- Input parameters:
-- @locationFilter VARCHAR: The specific location to filter by (e.g., 'Intercontinental', 'Sky Villa').
-- @minPrice DECIMAL: The minimum price range.
-- @maxPrice DECIMAL: The maximum price range.

-- Ensure to replace placeholders with actual values or bind parameters in your application.

SELECT 
    property_id,        -- Unique identifier for the property
    property_name,      -- Name of the property
    location,           -- Location of the property
    price,              -- Price of the property
    description,        -- Description of the property
    other_columns       -- Additional columns as needed
FROM 
    properties          -- Name of the table containing properties
WHERE 
    location = @locationFilter         -- Filter by location
    AND price BETWEEN @minPrice AND @maxPrice  -- Filter by price range
ORDER BY 
    price ASC;           -- Sort properties by price in ascending order
```
