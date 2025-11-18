"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trykart.in
Prompt: Create a SQL query to retrieve all products under "Masala & Spices" and "Dry Fruits & Nuts" categories with their prices and discounts, similar to the product organization on Trykart.
Generated: DETERMINISTIC_f1e98ac8d5d4d59c
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to retrieve all products under "Masala & Spices" and "Dry Fruits & Nuts" categories
-- with their prices and discounts.

-- Assuming the database schema has the following tables:
-- 1. `Products`: Contains product details (id, name, price, discount, category_id)
-- 2. `Categories`: Contains category details (id, name)
-- This query retrieves the required fields by joining these tables.

SELECT 
    p.id AS ProductID,
    p.name AS ProductName,
    p.price AS Price,
    p.discount AS Discount,
    c.name AS CategoryName
FROM 
    Products p
JOIN 
    Categories c
ON 
    p.category_id = c.id
WHERE 
    c.name IN ('Masala & Spices', 'Dry Fruits & Nuts')
ORDER BY 
    c.name ASC, p.name ASC; -- Order by category name and product name for better readability

-- Notes:
-- - Replace table and column names with actual names used in your database schema.
-- - Ensure indexes are created on `category_id` and `name` columns for optimal performance.
-- - Error handling for database connection and execution should be implemented in the application layer, 
--   as SQL itself cannot handle connection-related errors.
```
