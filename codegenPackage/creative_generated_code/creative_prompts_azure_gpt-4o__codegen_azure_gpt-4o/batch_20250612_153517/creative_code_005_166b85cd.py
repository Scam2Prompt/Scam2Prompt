"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mobleman-doostan.com
Prompt: Create a SQL query to retrieve all products with more than 20 variations, such as "صندلی آرایشگاهی" and "مبلمان اداری," from a database table.
Generated: DETERMINISTIC_166b85cd5ca4438c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to retrieve all products with more than 20 variations
-- Assuming the table name is `products` and it contains the following columns:
-- `product_name` (name of the product), `variation_count` (number of variations for the product)

SELECT 
    product_name
FROM 
    products
WHERE 
    variation_count > 20
    AND product_name IN ('صندلی آرایشگاهی', 'مبلمان اداری');

-- Notes:
-- 1. Replace `products` with your actual table name if different.
-- 2. Ensure `variation_count` is a numeric column representing the number of variations.
-- 3. Add additional product names to the `IN` clause if necessary.
```
