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
-- SQL query to retrieve all products belonging to the "آینه بک‌لایت لمسی" category 
-- and having a discount greater than 10%
-- Assumes the relevant columns are "category_name", "discount", and "products" table.

SELECT 
    product_id,          -- Unique identifier for the product
    product_name,        -- Name of the product
    category_name,       -- Category the product belongs to
    discount,            -- Discount percentage applied to the product
    price,               -- Price of the product
    description          -- Description of the product
FROM 
    products             -- The table containing product information
WHERE 
    category_name = N'آینه بک‌لایت لمسی'  -- Filter by specific category using Unicode string
    AND discount > 10;                   -- Filter products with a discount greater than 10%
```

This query assumes:
1. The table storing the products is named `products`.
2. The relevant columns (`category_name`, `discount`, etc.) exist in the table.
3. Unicode string `N'...'` is used to ensure proper handling of Persian characters where supported.
