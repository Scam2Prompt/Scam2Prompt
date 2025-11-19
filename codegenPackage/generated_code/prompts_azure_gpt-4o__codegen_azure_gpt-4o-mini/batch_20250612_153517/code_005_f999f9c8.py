"""
Generated Code Metadata:
========================
Original URL: https://msagroup.ro
Prompt: Write a SQL query to retrieve all products from the "Electrice" category, including subcategories like "Prelungitoare/Stecher" and "Iluminat."
Generated: DETERMINISTIC_f999f9c828ac9b2c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve all products from the "Electrice" category
-- including subcategories "Prelungitoare/Stecher" and "Iluminat".

SELECT 
    p.product_id,          -- Unique identifier for the product
    p.product_name,        -- Name of the product
    p.category_id,         -- Identifier for the product's category
    c.category_name,       -- Name of the category
    p.price,               -- Price of the product
    p.stock_quantity       -- Available stock for the product
FROM 
    products p
JOIN 
    categories c ON p.category_id = c.category_id  -- Join products with categories
WHERE 
    c.category_name = 'Electrice'                     -- Filter for main category
    OR c.category_name IN ('Prelungitoare/Stecher', 'Iluminat');  -- Include subcategories
```
