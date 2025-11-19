"""
Generated Code Metadata:
========================
Original URL: https://ipolattibraz.blogspot.com
Prompt: Create a SQL query to retrieve product information for bicycles with specific features (e.g., aro 12, feminino) from a database like the one used by ipolattibraz.
Generated: DETERMINISTIC_5125f6c6f928c247
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve product information for bicycles with specific features
-- from the ipolattibraz database.

SELECT 
    p.product_id,          -- Unique identifier for the product
    p.product_name,        -- Name of the product
    p.brand,               -- Brand of the bicycle
    p.price,               -- Price of the bicycle
    p.features,            -- Features of the bicycle
    p.category             -- Category of the product
FROM 
    products p            -- Selecting from the products table
WHERE 
    p.category = 'bicycle' -- Filter for bicycles
    AND p.features LIKE '%aro 12%'  -- Filter for bicycles with aro 12
    AND p.features LIKE '%feminino%'  -- Filter for feminine bicycles
ORDER BY 
    p.product_name;        -- Order results by product name
```
