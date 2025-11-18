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
-- SQL query to retrieve all products from the "Sour, Gose & otras" category
-- that have a discount greater than 20%. The result includes product name,
-- original price, discounted price, and discount percentage.

SELECT 
    product_name,                      -- Name of the product
    original_price,                    -- Original price before discount
    discounted_price,                  -- Price after discount
    ROUND(((original_price - discounted_price) / original_price) * 100, 2) AS discount_percentage -- Calculated discount percentage
FROM 
    products                            -- Table containing product information
WHERE 
    category = 'Sour, Gose & otras'    -- Filter for the specified category
    AND discounted_price < original_price * 0.8  -- Filter for products with a discount greater than 20%
ORDER BY 
    product_name;                      -- Order results by product name
```
