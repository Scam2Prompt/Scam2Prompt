"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activesport.cz
Prompt: Develop a SQL query to extract all products with discounts greater than 20% from a database, similar to the discount system on ActiveSport.cz.
Generated: DETERMINISTIC_48cc2ed2a6472efc
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to extract all products with discounts greater than 20%
-- This assumes a table named 'products' with columns 'product_id', 'name', 'original_price', 'discount_price', and 'discount_percentage'.

-- Ensure the discount_percentage column correctly reflects the discount value
-- Example: discount_percentage = ((original_price - discount_price) / original_price) * 100

SELECT 
    product_id,            -- Unique identifier for the product
    name,                  -- Name of the product
    original_price,        -- Original price of the product
    discount_price,        -- Discounted price of the product
    discount_percentage    -- Pre-calculated discount percentage
FROM 
    products
WHERE 
    discount_percentage > 20; -- Filter for products with discounts greater than 20%
```

This query assumes that `discount_percentage` is a pre-calculated column in the table. If such a column is not present, you would need to compute it dynamically as part of the query. Let me know if you need that adjustment.
