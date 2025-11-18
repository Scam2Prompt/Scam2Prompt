"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dmsauto4x4.ro
Prompt: Generate a SQL query to retrieve all products related to "ARB" brand accessories, such as canisters, recovery gear, and interior storage solutions, as described on DMS Auto4x4.ro.
Generated: DETERMINISTIC_2cb11c7438bf3b1c
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to retrieve all products related to the "ARB" brand accessories
-- such as canisters, recovery gear, and interior storage solutions.

-- Assuming the table structure:
-- Table: Products
-- Columns:
-- - id (Primary Key)
-- - name (Product Name)
-- - description (Product Description)
-- - brand (Brand Name)
-- - category (Product Category)
-- - price (Product Price)
-- - stock_quantity (Quantity in Stock)

SELECT 
    id,
    name,
    description,
    price,
    stock_quantity
FROM 
    Products
WHERE 
    brand = 'ARB' -- Filter for ARB brand
    AND (
        category LIKE '%canister%' OR     -- Match canisters
        category LIKE '%recovery gear%' OR -- Match recovery gear
        category LIKE '%interior storage%' -- Match interior storage solutions
    )
ORDER BY 
    name ASC; -- Sort results alphabetically by product name
```
