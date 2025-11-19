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
SELECT 
    shoe_id,
    brand,
    model,
    type,
    color,
    size,
    price,
    stock_quantity,
    description,
    created_at,
    updated_at
FROM 
    shoes
WHERE 
    type IN ('chuteira', 'tenis de esporte')  -- Filter by shoe types
    AND stock_quantity > 0                    -- Only show items in stock
ORDER BY 
    brand ASC,                                -- Sort by brand alphabetically
    price DESC;                               -- Then by price descending
```
