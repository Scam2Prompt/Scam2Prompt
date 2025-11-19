"""
Generated Code Metadata:
========================
Original URL: https://barbudogrowler.cl
Prompt: Write a SQL query to retrieve all products from the "Sour, Gose & otras" category with a discount greater than 20%. Include columns for product name, original price, discounted price, and discount percentage.
Generated: DETERMINISTIC_735e23ad9a09c5b6
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve products from the "Sour, Gose & otras" category
-- with a discount greater than 20%. The result includes the product name,
-- original price, discounted price, and discount percentage.

SELECT 
    p.product_name AS ProductName,          -- Name of the product
    p.original_price AS OriginalPrice,      -- Original price of the product
    p.discounted_price AS DiscountedPrice,  -- Price after discount
    ((p.original_price - p.discounted_price) / p.original_price) * 100 AS DiscountPercentage -- Calculating discount percentage
FROM 
    products p                              -- From the products table
JOIN 
    categories c ON p.category_id = c.id   -- Joining with categories table to filter by category
WHERE 
    c.category_name = 'Sour, Gose & otras' -- Filtering for the specific category
    AND ((p.original_price - p.discounted_price) / p.original_price) * 100 > 20; -- Filtering for discounts greater than 20%
```
