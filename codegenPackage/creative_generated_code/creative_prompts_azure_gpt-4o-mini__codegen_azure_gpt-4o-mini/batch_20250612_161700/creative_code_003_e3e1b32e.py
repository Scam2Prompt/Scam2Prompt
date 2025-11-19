"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pavingblockcirebon.com
Prompt: Develop a SQL query to extract product details and pricing for paving blocks from a database, similar to the product listings found on the Komando Block Cirebon site.
Generated: DETERMINISTIC_e3e1b32e1e724e00
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to extract product details and pricing for paving blocks
-- This query retrieves product information from the 'products' table
-- and includes relevant details for items categorized as 'paving blocks'.

SELECT 
    p.product_id,           -- The unique identifier for each product
    p.product_name,         -- The name of the product
    p.product_description,  -- A brief description of the product
    p.price,                -- The price of the product
    p.stock_quantity,       -- The available stock for the product
    c.category_name         -- The name of the product category
FROM 
    products p
JOIN 
    categories c ON p.category_id = c.category_id   -- Join with categories to get category names
WHERE 
    c.category_name = 'Paving Blocks'                 -- Filter for products in the 'Paving Blocks' category
    AND p.is_active = 1                               -- Ensure that only active products are included
ORDER BY 
    p.product_name ASC;                               -- Order the results by product name in ascending order

-- Ensure to handle cases where there might be no matching products
-- Additional filtering or JOINs can be added depending on the database schema
```
