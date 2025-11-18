"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sit.d1jkap9jqfwf3j.amplifyapp.com
Prompt: Write a SQL query to retrieve all products from a database that belong to the "beauty" category and are priced below 150 OMR, including their names, prices, and stock status.
Generated: DETERMINISTIC_229d949025c28aad
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Query to fetch all products in the "beauty" category with a price below 150 OMR
-- Columns retrieved: product name, price, and stock status
-- Assumes a table structure with columns: id, name, category, price, stock_status

SELECT 
    name AS product_name,       -- Name of the product
    price AS product_price,     -- Price of the product in OMR
    stock_status                -- Stock status of the product
FROM 
    products                    -- Table containing product information
WHERE 
    category = 'beauty'         -- Filter for products in the "beauty" category
    AND price < 150;            -- Filter for products priced below 150 OMR
```
