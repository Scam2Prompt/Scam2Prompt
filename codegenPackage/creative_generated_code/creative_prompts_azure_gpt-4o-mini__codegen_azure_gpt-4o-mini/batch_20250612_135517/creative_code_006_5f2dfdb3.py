"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beamtoken.org
Prompt: Create a SQL query to extract data on the most popular smart home products from a database that mirrors the Digital Trends product listings.
Generated: DETERMINISTIC_5f2dfdb321db043f
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to extract data on the most popular smart home products
-- from a database mirroring the Digital Trends product listings.

SELECT 
    p.product_id,                       -- Unique identifier for each product
    p.product_name,                     -- Name of the product
    p.category,                         -- Category of the product
    p.brand,                            -- Brand of the product
    p.price,                            -- Price of the product
    p.rating,                           -- Average user rating
    p.review_count,                     -- Number of reviews
    p.release_date                      -- Release date of the product
FROM 
    products p                         -- Table containing product listings
WHERE 
    p.category = 'Smart Home'          -- Filter for smart home products
    AND p.rating IS NOT NULL           -- Ensure rating is available
    AND p.review_count > 0             -- Ensure there are reviews
ORDER BY 
    p.rating DESC,                     -- Order by rating in descending order
    p.review_count DESC                 -- Then by review count in descending order
LIMIT 
    10;                                 -- Limit to the top 10 most popular products

-- Note: Ensure that the database connection and context
-- are properly established before running this query.
```
