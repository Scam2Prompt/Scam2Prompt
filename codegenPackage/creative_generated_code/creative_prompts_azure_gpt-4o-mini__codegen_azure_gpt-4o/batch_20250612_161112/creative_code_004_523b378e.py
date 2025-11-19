"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loli.bg
Prompt: Construct a SQL query to extract product information from the LOLI.BG database, focusing on items under the "разпродажба" category.
Generated: DETERMINISTIC_523b378e29403851
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to extract product information from the LOLI.BG database
-- Focuses on items under the "разпродажба" category

-- Assumes the following:
-- - The database has a table named 'products'.
-- - The 'products' table contains columns: 'id', 'name', 'category', 'price', 'stock', 'description'.
-- - The 'category' column contains the category names, including "разпродажба".

SELECT 
    id,                -- Unique identifier for each product
    name,              -- Name of the product
    price,             -- Price of the product
    stock,             -- Number of items in stock
    description        -- Detailed description of the product
FROM 
    products           -- Table containing product information
WHERE 
    category = 'разпродажба'  -- Filtering products under the "разпродажба" category
ORDER BY 
    price ASC;         -- Sort the results by price in ascending order for better readability
```
