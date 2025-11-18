"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baazaars.com
Prompt: Create a SQL query to extract all products with a discount greater than 20% from an e-commerce database, including categories like "Accessories" and "Dresses."
Generated: DETERMINISTIC_4738f5b3d6173039
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to extract all products with a discount greater than 20%
-- from categories "Accessories" and "Dresses"
SELECT 
    p.product_id,           -- Unique identifier for the product
    p.product_name,         -- Name of the product
    p.category,             -- Category of the product
    p.original_price,       -- Original price of the product
    p.discounted_price,     -- Discounted price of the product
    ((p.original_price - p.discounted_price) / p.original_price) * 100 AS discount_percentage -- Calculated discount percentage
FROM 
    products p              -- Assuming the table name is 'products'
WHERE 
    p.category IN ('Accessories', 'Dresses') -- Filter for specific categories
    AND 
    ((p.original_price - p.discounted_price) / p.original_price) * 100 > 20 -- Filter for discount greater than 20%
ORDER BY 
    discount_percentage DESC; -- Optional: Order results by highest discount percentage
```
