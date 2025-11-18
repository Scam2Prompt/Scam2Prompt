"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://barbudogrowler.cl
Prompt: Write a SQL query to retrieve all products from the "Sour, Gose & otras" category with a discount greater than 20%. Include columns for product name, original price, discounted price, and discount percentage.
Generated: DETERMINISTIC_735e23ad9a09c5b6
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Retrieve all products from the "Sour, Gose & otras" category with a discount greater than 20%
-- Columns included: product name, original price, discounted price, and discount percentage

SELECT 
    p.product_name AS "Product Name",          -- Name of the product
    p.original_price AS "Original Price",     -- Original price of the product
    (p.original_price * (1 - p.discount_percentage / 100)) AS "Discounted Price", -- Price after applying the discount
    p.discount_percentage AS "Discount Percentage" -- Percentage discount applied
FROM 
    products AS p                             -- Table containing product information
JOIN 
    categories AS c                           -- Table containing category information
ON 
    p.category_id = c.category_id             -- Join products with their respective categories
WHERE 
    c.category_name = 'Sour, Gose & otras'    -- Filter for the specific category
    AND p.discount_percentage > 20;          -- Filter for products with a discount greater than 20%
```
