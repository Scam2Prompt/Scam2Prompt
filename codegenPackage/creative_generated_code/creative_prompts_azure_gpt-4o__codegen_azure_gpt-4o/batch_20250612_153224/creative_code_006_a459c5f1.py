"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://watpac.in
Prompt: Write a SQL query to retrieve all products from Watpac Chemicals Pvt Ltd's database that belong to the "Waterproofing Solutions" category and cost less than ₹500.00.
Generated: DETERMINISTIC_a459c5f194195979
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to retrieve all products from Watpac Chemicals Pvt Ltd's database
-- that belong to the "Waterproofing Solutions" category and cost less than ₹500.00

-- Ensure proper table names and column names are used in the query.
-- Replace `products` with the actual table name if different.
-- Replace `category`, `price`, and `product_name` with actual column names if different.

SELECT 
    product_id,        -- Product ID (assuming this column exists in the table)
    product_name,      -- Name of the product
    price,             -- Price of the product
    category           -- Category of the product
FROM 
    products           -- Table containing product information
WHERE 
    category = 'Waterproofing Solutions' -- Filter for "Waterproofing Solutions" category
    AND price < 500.00;                  -- Filter for products costing less than ₹500.00

-- This query assumes:
-- 1. The `price` column stores numerical values (e.g., DECIMAL or FLOAT type).
-- 2. The `category` column uses exact matches for category names.
-- 3. Proper indexing exists on `category` and `price` columns for performance.

-- Note: Verify column data types and table structures before executing.
```
