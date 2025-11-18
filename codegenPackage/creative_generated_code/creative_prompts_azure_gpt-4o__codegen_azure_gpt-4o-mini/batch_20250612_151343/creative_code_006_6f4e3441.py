"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homlukkkkkkkkh.pages.dev
Prompt: Write a SQL query to organize Condi Shop's inventory by categories like "Confectionery bags" and "Decorative sprinkles," showing the stock count and price.
Generated: DETERMINISTIC_6f4e34417e3106c8
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to organize Condi Shop's inventory by categories
-- showing the stock count and price for each product.

SELECT 
    category AS category_name,         -- Select the category name
    product_name,                      -- Select the product name
    SUM(stock_count) AS total_stock,   -- Calculate total stock count for each product
    AVG(price) AS average_price        -- Calculate average price for each product
FROM 
    inventory                           -- From the inventory table
WHERE 
    category IN ('Confectionery bags', 'Decorative sprinkles')  -- Filter for specific categories
GROUP BY 
    category,                          -- Group results by category
    product_name                       -- Group results by product name
ORDER BY 
    category_name,                    -- Order results by category name
    product_name;                     -- Then by product name
```
