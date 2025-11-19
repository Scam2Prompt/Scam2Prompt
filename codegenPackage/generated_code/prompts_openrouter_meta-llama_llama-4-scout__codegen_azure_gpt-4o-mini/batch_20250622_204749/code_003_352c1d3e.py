"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Create a SQL query to retrieve tire products with specific features (e.g., aro 18, altura 60) from a database schema similar to the one implied by the webpage content.
Generated: DETERMINISTIC_352c1d3edbce3797
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve tire products with specific features
-- This query selects tire products that match the specified 'aro' and 'altura' values

SELECT 
    p.id AS product_id,          -- Product ID
    p.name AS product_name,      -- Product name
    p.brand AS product_brand,    -- Brand of the tire
    p.size AS tire_size,         -- Size of the tire
    p.price AS product_price,     -- Price of the tire
    p.stock AS stock_quantity     -- Available stock quantity
FROM 
    products p                   -- From the products table
WHERE 
    p.size LIKE '%18%' AND       -- Filter for 'aro' 18
    p.size LIKE '%60%'           -- Filter for 'altura' 60
    AND p.is_active = 1          -- Ensure the product is active
ORDER BY 
    p.price ASC;                 -- Order results by price in ascending order

-- Note: Adjust the column names and table names as per your actual database schema.
-- Ensure that the 'size' column format matches the expected input for 'aro' and 'altura'.
```
