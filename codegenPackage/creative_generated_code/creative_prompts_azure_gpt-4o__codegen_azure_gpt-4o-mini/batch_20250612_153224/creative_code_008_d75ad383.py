"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dolphiniran.com
Prompt: Create a SQL query to retrieve all products from Dolphin Iran's database that belong to the "آینه بک‌لایت لمسی" category and have a discount greater than 10%.
Generated: DETERMINISTIC_d75ad383dfbd7af1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to retrieve all products from Dolphin Iran's database
-- that belong to the "آینه بک‌لایت لمسی" category and have a discount greater than 10%

SELECT 
    product_id,         -- Unique identifier for the product
    product_name,       -- Name of the product
    category,           -- Category of the product
    price,              -- Original price of the product
    discount,           -- Discount percentage on the product
    final_price         -- Final price after discount
FROM 
    products            -- The table containing product information
WHERE 
    category = 'آینه بک‌لایت لمسی'   -- Filter for the specified category
    AND discount > 10;  -- Filter for products with discount greater than 10%
```
