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
-- SQL query to retrieve all products from the "beauty" category with a price below 150 OMR
SELECT 
    product_name,    -- Selects the name of the product
    price,           -- Selects the price of the product
    stock_status     -- Selects the stock status of the product
FROM 
    products         -- Specifies the table to query from
WHERE 
    category = 'beauty'  -- Filters results to include only products in the 'beauty' category
    AND price < 150;     -- Further filters to include only products priced below 150 OMR
```
