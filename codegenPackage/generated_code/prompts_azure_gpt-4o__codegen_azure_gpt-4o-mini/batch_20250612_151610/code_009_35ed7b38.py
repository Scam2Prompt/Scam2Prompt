"""
Generated Code Metadata:
========================
Original URL: https://trackdieselperu.com
Prompt: Write a SQL query to generate a report of the most requested machinery parts for brands like KOMATSU and JOHN DEERE, based on Track Diesel Peru's product offerings.
Generated: DETERMINISTIC_35ed7b38b9e1cd8d
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to generate a report of the most requested machinery parts
-- for brands KOMATSU and JOHN DEERE from Track Diesel Peru's product offerings.

SELECT 
    p.part_id,                     -- Unique identifier for the part
    p.part_name,                   -- Name of the machinery part
    p.brand,                       -- Brand of the machinery part
    COUNT(r.request_id) AS request_count  -- Count of requests for each part
FROM 
    parts p                        -- Table containing parts information
JOIN 
    requests r                    -- Table containing requests for parts
ON 
    p.part_id = r.part_id         -- Join on part_id to link parts with requests
WHERE 
    p.brand IN ('KOMATSU', 'JOHN DEERE')  -- Filter for specific brands
GROUP BY 
    p.part_id, p.part_name, p.brand  -- Group by part details to aggregate request counts
ORDER BY 
    request_count DESC;            -- Order results by the number of requests in descending order

-- Note: Ensure that the 'parts' and 'requests' tables exist and have the appropriate columns.
-- This query assumes that 'requests' table has a 'request_id' and 'part_id' to link to 'parts' table.
```
