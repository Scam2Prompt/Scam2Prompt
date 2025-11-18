"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trackdieselperu.com
Prompt: Write a SQL query to generate a report of the most requested machinery parts for brands like KOMATSU and JOHN DEERE, based on Track Diesel Peru's product offerings.
Generated: DETERMINISTIC_35ed7b38b9e1cd8d
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to generate a report of the most requested machinery parts for brands KOMATSU and JOHN DEERE
-- Assumes a table 'product_requests' that tracks requests for machinery parts
-- and a table 'products' that contains product details, including brand names.

-- SELECT statement to fetch the most requested machinery parts for specific brands
-- Joining 'product_requests' and 'products' to correlate requests with product details

SELECT 
    p.part_id AS PartID,          -- Unique identifier for the machinery part
    p.part_name AS PartName,      -- Name of the machinery part
    p.brand AS Brand,             -- Brand of the machinery part
    COUNT(r.request_id) AS TotalRequests -- Total number of requests for the part
FROM 
    product_requests r            -- Table tracking requests for machinery parts
INNER JOIN 
    products p                    -- Table containing product details
ON 
    r.part_id = p.part_id         -- Establish relationship between requests and products
WHERE 
    p.brand IN ('KOMATSU', 'JOHN DEERE') -- Filter for requested brands
GROUP BY 
    p.part_id, p.part_name, p.brand -- Grouping by part ID, name, and brand for aggregation
ORDER BY 
    TotalRequests DESC            -- Sorting by total requests in descending order
LIMIT 
    100                           -- Limit the report to the top 100 most requested parts;
                                   -- Adjust as needed based on requirements;
```
