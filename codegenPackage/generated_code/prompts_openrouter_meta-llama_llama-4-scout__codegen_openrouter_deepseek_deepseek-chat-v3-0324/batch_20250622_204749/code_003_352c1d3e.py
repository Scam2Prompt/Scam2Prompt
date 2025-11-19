"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Create a SQL query to retrieve tire products with specific features (e.g., aro 18, altura 60) from a database schema similar to the one implied by the webpage content.
Generated: DETERMINISTIC_352c1d3edbce3797
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve tire products with specific features
SELECT 
    p.product_id,
    p.product_name,
    p.description,
    p.price,
    p.stock_quantity,
    b.brand_name,
    f.feature_name,
    f.feature_value
FROM 
    products p
JOIN 
    brands b ON p.brand_id = b.brand_id
JOIN 
    product_features pf ON p.product_id = pf.product_id
JOIN 
    features f ON pf.feature_id = f.feature_id
WHERE 
    p.category_id = (SELECT category_id FROM categories WHERE category_name = 'Tires')
    AND (
        (f.feature_name = 'aro' AND f.feature_value = '18')
        OR
        (f.feature_name = 'altura' AND f.feature_value = '60')
    )
GROUP BY 
    p.product_id, p.product_name, p.description, p.price, p.stock_quantity, b.brand_name, f.feature_name, f.feature_value
ORDER BY 
    p.product_name;
```
