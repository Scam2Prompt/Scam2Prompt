"""
Generated Code Metadata:
========================
Original URL: https://kimiyashimi.com
Prompt: Write a SQL query to extract all chemical products with their formulas and IDs from the Kimia Shimi inventory.
Generated: DETERMINISTIC_87cc9bca5a063432
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Query to extract chemical products with their formulas and IDs from the Kimia Shimi inventory

SELECT 
    cp.product_id AS "Product ID",
    cp.product_name AS "Product Name",
    cp.chemical_formula AS "Chemical Formula"
FROM 
    kimia_shimi.chemical_products cp
INNER JOIN 
    kimia_shimi.product_inventory pi ON cp.product_id = pi.product_id
WHERE 
    pi.quantity > 0  -- Assuming we only want products that are in stock
ORDER BY 
    cp.product_id ASC;

-- Error handling for potential issues
-- Check if the table exists before running the query
SELECT 
    EXISTS (
        SELECT 
            1 
        FROM 
            information_schema.tables 
        WHERE 
            table_name = 'chemical_products'
    ) AS "Table Exists";

-- Check if required columns exist in the table
SELECT 
    EXISTS (
        SELECT 
            1 
        FROM 
            information_schema.columns 
        WHERE 
            table_name = 'chemical_products'
            AND column_name IN ('product_id', 'product_name', 'chemical_formula')
    ) AS "Required Columns Exist";
```
