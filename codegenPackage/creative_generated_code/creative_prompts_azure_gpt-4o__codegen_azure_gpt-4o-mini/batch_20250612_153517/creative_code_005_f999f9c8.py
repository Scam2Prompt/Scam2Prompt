"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://msagroup.ro
Prompt: Write a SQL query to retrieve all products from the "Electrice" category, including subcategories like "Prelungitoare/Stecher" and "Iluminat."
Generated: DETERMINISTIC_f999f9c828ac9b2c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to retrieve all products from the "Electrice" category
-- This includes products in specified subcategories.

SELECT
    p.product_id,        -- ID of the product
    p.product_name,      -- Name of the product
    p.price,             -- Price of the product
    c.category_name      -- Name of the category the product belongs to
FROM
    products p           -- Main product table
JOIN
    categories c ON p.category_id = c.category_id  -- Join with category table
WHERE
    c.category_name = 'Electrice'                    -- Filter for main category
    OR c.category_name IN ('Prelungitoare/Stecher', 'Iluminat')  -- Include specified subcategories
ORDER BY
    p.product_name;      -- Order results by product name

-- Note: Ensure that the 'products' and 'categories' tables exist
-- and that the appropriate foreign key relationships are set up.
```
