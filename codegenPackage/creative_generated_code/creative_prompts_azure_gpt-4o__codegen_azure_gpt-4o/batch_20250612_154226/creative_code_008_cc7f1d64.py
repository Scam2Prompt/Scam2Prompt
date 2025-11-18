"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallmemes.com
Prompt: Write a SQL query to extract all discounted products from the "Wall Memes" database, including their original and discounted prices.
Generated: DETERMINISTIC_cc7f1d646225e11c
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to extract all discounted products from the "Wall Memes" database
-- The query includes the product name, original price, discounted price, and discount percentage.
-- Proper error handling should be implemented at the application level when executing this query.

SELECT 
    product_id,              -- Unique identifier for the product
    product_name,            -- Name of the product
    original_price,          -- Original price of the product
    discounted_price,        -- Discounted price of the product
    (original_price - discounted_price) AS discount_amount, -- Amount of discount applied
    ROUND(((original_price - discounted_price) / original_price) * 100, 2) AS discount_percentage -- Discount percentage
FROM 
    products                 -- Table containing product details
WHERE 
    discounted_price < original_price -- Condition to filter products with discounts
ORDER BY 
    discount_percentage DESC; -- Sort by discount percentage in descending order
```
