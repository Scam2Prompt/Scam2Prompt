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
-- SQL Query to retrieve product information for lighting products with a 12x payment plan
-- This query assumes the existence of a `products` table with relevant columns.

SELECT 
    product_name,       -- Name of the product
    price,              -- Price of the product
    discount,           -- Discount applied to the product
    payment_plan        -- Payment plan associated with the product
FROM 
    products
WHERE 
    category = 'Lighting'               -- Filter for lighting products
    AND payment_plan = '12x'            -- Filter for products with a 12x payment plan
    AND product_name LIKE '%Lâmpada%'   -- Additional filter for products containing "Lâmpada" in the name
ORDER BY 
    product_name ASC;                   -- Sort results alphabetically by product name
```
