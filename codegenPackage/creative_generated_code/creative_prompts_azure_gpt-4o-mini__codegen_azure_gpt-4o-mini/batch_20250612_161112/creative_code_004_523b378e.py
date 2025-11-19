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
-- Focusing on items categorized under "разпродажба" (sale)

SELECT 
    p.product_id,               -- Unique identifier for each product
    p.product_name,             -- Name of the product
    p.product_description,      -- Description of the product
    p.price,                    -- Price of the product
    p.discount_price,           -- Discounted price if applicable
    c.category_name,            -- Name of the category
    p.stock_quantity             -- Available stock for the product
FROM 
    products p                  -- Table containing product details
JOIN 
    categories c                -- Table containing category details
ON 
    p.category_id = c.category_id  -- Joining products with their respective categories
WHERE 
    c.category_name = 'разпродажба'  -- Filtering for products in the "разпродажба" category
    AND p.is_active = 1        -- Ensuring only active products are selected
ORDER BY 
    p.price DESC;              -- Ordering results by price in descending order
```
