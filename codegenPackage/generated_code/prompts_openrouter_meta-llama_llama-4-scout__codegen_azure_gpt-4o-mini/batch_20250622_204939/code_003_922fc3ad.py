"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Create a SQL query to retrieve product information, including name, price, and discount, for all lighting products with a 12x payment plan, such as the `Lâmpada Compacta T2 15w 220v E27 Ltsy15 Lightex`.
Generated: DETERMINISTIC_922fc3ad82ba8952
Batch ID: 20250622_204939
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve product information for lighting products
-- with a 12x payment plan, including name, price, and discount.

SELECT 
    p.product_name AS ProductName,  -- Name of the product
    p.price AS Price,                -- Price of the product
    p.discount AS Discount            -- Discount on the product
FROM 
    products p                       -- From the products table
JOIN 
    payment_plans pp                 -- Join with payment plans table
ON 
    p.id = pp.product_id             -- Matching product IDs
WHERE 
    p.category = 'Lighting'          -- Filter for lighting products
    AND pp.plan_type = '12x'         -- Filter for 12x payment plan
    AND p.product_name LIKE '%Lâmpada Compacta T2 15w 220v E27 Ltsy15 Lightex%' -- Specific product name
ORDER BY 
    p.product_name;                  -- Order results by product name
```
