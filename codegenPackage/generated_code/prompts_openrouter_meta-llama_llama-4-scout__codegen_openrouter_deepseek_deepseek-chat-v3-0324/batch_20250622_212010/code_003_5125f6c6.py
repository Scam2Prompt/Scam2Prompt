"""
Generated Code Metadata:
========================
Original URL: https://ipolattibraz.blogspot.com
Prompt: Create a SQL query to retrieve product information for bicycles with specific features (e.g., aro 12, feminino) from a database like the one used by ipolattibraz.
Generated: DETERMINISTIC_5125f6c6f928c247
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve bicycle products with specific features
SELECT 
    p.product_id,
    p.product_name,
    p.description,
    p.price,
    p.stock_quantity,
    p.image_url,
    b.brand_name,
    c.category_name,
    f.frame_size,
    f.wheel_size,
    f.gender,
    f.color
FROM 
    products p
JOIN 
    brands b ON p.brand_id = b.brand_id
JOIN 
    categories c ON p.category_id = c.category_id
JOIN 
    product_features f ON p.product_id = f.product_id
WHERE 
    c.category_name = 'Bicicletas'
    AND f.wheel_size = 'aro 12'
    AND f.gender = 'feminino'
    AND p.is_active = 1
    AND p.stock_quantity > 0
ORDER BY 
    p.price ASC;
```
