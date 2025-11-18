"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.navkarfurniture.com
Prompt: Write a SQL query to organize furniture inventory data into categories such as "Domestic Furniture," "Office Furniture," and "School Furniture," based on the product range described by Navkar Furniture.
Generated: DETERMINISTIC_83399e4fe200819a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to categorize furniture inventory into specified categories

SELECT 
    product_id, 
    product_name,
    product_type,
    -- Categorizing products based on their description
    CASE 
        WHEN product_type LIKE '%Sofa%' OR product_type LIKE '%Table%' OR product_type LIKE '%Chair%' THEN 'Domestic Furniture'
        WHEN product_type LIKE '%Desk%' OR product_type LIKE '%Office Chair%' OR product_type LIKE '%Filing%' THEN 'Office Furniture'
        WHEN product_type LIKE '%Desk%' OR product_type LIKE '%Classroom Chair%' OR product_type LIKE '%Whiteboard%' THEN 'School Furniture'
        ELSE 'Other'  -- Category for products that do not match any specified category
    END AS furniture_category
FROM 
    furniture_inventory
WHERE 
    product_type IS NOT NULL  -- Ensuring that we only include products with a defined type
ORDER BY 
    furniture_category,  -- Sort results by category
    product_name;  -- Then sort by product name within each category

-- Ensure proper error handling in your application layer when executing this query
```
