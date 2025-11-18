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
-- SQL Query to extract products with discounts greater than 20%
-- This query assumes the existence of a 'products' table with 'price' and 'discounted_price' columns.

SELECT 
    product_id,                  -- Unique identifier for each product
    product_name,                -- Name of the product
    price,                       -- Original price of the product
    discounted_price,            -- Discounted price of the product
    (1 - (discounted_price / price)) * 100 AS discount_percentage  -- Calculate discount percentage
FROM 
    products                     -- Source table containing product information
WHERE 
    (1 - (discounted_price / price)) * 100 > 20;  -- Filter for discounts greater than 20%
```

```sql
-- Note: Ensure that 'discounted_price' is not NULL or zero to avoid division by zero errors.
-- Additional error handling can be implemented in application code if necessary.
```
