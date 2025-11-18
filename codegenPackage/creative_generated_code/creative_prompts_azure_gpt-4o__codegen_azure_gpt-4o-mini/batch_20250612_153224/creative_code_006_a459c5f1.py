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
-- SQL query to retrieve all products from Watpac Chemicals Pvt Ltd's database
-- that belong to the "Waterproofing Solutions" category and cost less than ₹500.00

SELECT 
    product_id,        -- Unique identifier for the product
    product_name,      -- Name of the product
    category,          -- Category of the product
    price              -- Price of the product
FROM 
    products           -- Table containing product information
WHERE 
    category = 'Waterproofing Solutions'   -- Filter for products in the specified category
    AND price < 500.00;                     -- Filter for products costing less than ₹500.00
```
