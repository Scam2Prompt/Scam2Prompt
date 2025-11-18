"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shopeewise.com
Prompt: Write a SQL query to retrieve product details, such as "LUXXE RENEW (8 Berry Extract)," including price, stock status, and category from a database.
Generated: DETERMINISTIC_72f764cf3fa6247a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to retrieve product details including name, price, stock status, and category
SELECT 
    p.product_name AS "Product Name",     -- Selecting the product name
    p.price AS "Price",                    -- Selecting the product price
    p.stock_status AS "Stock Status",      -- Selecting the stock status of the product
    c.category_name AS "Category"          -- Selecting the category name from the related category table
FROM 
    products p                             -- From the products table
JOIN 
    categories c ON p.category_id = c.id  -- Joining with categories table to get the category name
WHERE 
    p.product_name = 'LUXXE RENEW (8 Berry Extract)'; -- Filtering for the specific product
```
